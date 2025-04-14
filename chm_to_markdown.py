import os
import re
import json
import shutil
import asyncio
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import html2text
import aiofiles

# Lists to customize removals.
tags_to_remove = ["iframe", "object", "script", "br", "img"]

classes_to_remove = [
    "collapsibleAreaRegion",
    "collapsibleRegionTitle",
    "collapseToggle",
    "codeSnippetContainerTab",
    "codeSnippetToolBar",
    "codeSnippetContainerTabs",
]

ids_to_remove = [
    "PageFooter",
]


def extract_page_title(soup):
    """Extract the page title from HTML content for use in the dictionary."""
    # First try to get the title from the title tag
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        title = title_tag.string.strip()
        return title
    
    # If no title tag, try h1
    h1_tag = soup.find('h1')
    if h1_tag and h1_tag.get_text():
        title = h1_tag.get_text().strip()
        return title
    
    # If no h1, try the first heading of any level
    for heading_level in range(2, 7):
        heading = soup.find(f'h{heading_level}')
        if heading and heading.get_text():
            title = heading.get_text().strip()
            return title
    
    # If all else fails, return None
    return None


def extract_keywords(title):
    """Extract potential keywords from the title for better search capabilities."""
    if not title:
        return []
        
    # Remove common stopwords and punctuation
    stopwords = {"a", "an", "the", "and", "or", "of", "to", "in", "for", "with", "on", "at", "by", "is", "are", "was", "were"}
    words = re.findall(r'\b\w+\b', title.lower())
    keywords = [word for word in words if word not in stopwords and len(word) > 2]
    
    # Add the complete title as a keyword for exact matching
    if title.lower() not in keywords:
        keywords.append(title.lower())
        
    return keywords


def update_links(soup, file_dictionary=None):
    """Update links in the HTML to point to markdown files with meaningful descriptions."""
    for a in soup.find_all("a", href=True):
        if a["href"] == "#PageHeader":
            a.decompose()
        elif a["href"].lower().endswith((".htm", ".html")):
            href = a["href"]
            # Handle potential relative paths with directories
            base_href = os.path.basename(href)
            base, _ = os.path.splitext(base_href)
            
            # Update link to point to markdown file
            a["href"] = base + ".md"
            
            # Add title attribute for better hovering if available in dictionary
            if file_dictionary and base in file_dictionary:
                display_name = file_dictionary[base].get("title")
                if display_name:
                    a["title"] = display_name
    return soup


def remove_unwanted_elements(soup):
    """Remove unwanted HTML elements to clean up the output."""
    for script in soup.find_all("script"):
        script.decompose()
    for tag in tags_to_remove:
        for element in soup.find_all(tag):
            element.decompose()
    for tag in soup.find_all(
        lambda tag: tag.has_attr("class")
        and any(cls in tag.get("class") for cls in classes_to_remove)
    ):
        tag.decompose()
    for element_id in ids_to_remove:
        for tag in soup.find_all(id=element_id):
            tag.decompose()
            
    # Remove feedback links and other common clutter
    for a in soup.find_all("a", href=lambda href: href and "javascript:" in str(href).lower()):
        a.decompose()
    
    return soup


def replace_code_snippets(soup):
    """Replace code snippets with placeholders for later insertion."""
    id_to_lang = {
        "IDAB_code_Div1": "csharp",
        "IDAB_code_Div2": "vb",
        "IDAB_code_Div3": "cpp",
        "IDAB_code_Div4": "fsharp",
    }
    code_blocks = {}
    counter = 0
    
    # Handle specifically tagged code blocks first
    for div_id, lang in id_to_lang.items():
        for code_div in soup.find_all("div", id=div_id):
            counter += 1
            pre_tag = code_div.find("pre")
            if pre_tag:
                code_text = pre_tag.get_text()
            else:
                code_text = code_div.get_text()
            placeholder = f"<<CODE_BLOCK_{counter}>>"
            code_block_markdown = f"```{lang}\n{code_text}\n```\n"
            code_blocks[placeholder] = code_block_markdown
            new_node = soup.new_string(placeholder)
            code_div.replace_with(new_node)
    
    # Handle generic pre tags that might contain code
    for pre_tag in soup.find_all("pre"):
        counter += 1
        code_text = pre_tag.get_text()
        # Try to detect language, default to plain text
        lang = "text"
        class_attr = pre_tag.get("class", [])
        if class_attr:
            class_str = " ".join(class_attr)
            if "csharp" in class_str or "cs" in class_str:
                lang = "csharp"
            elif "vb" in class_str:
                lang = "vb"
            elif "cpp" in class_str or "c++" in class_str:
                lang = "cpp"
            elif "fsharp" in class_str or "fs" in class_str:
                lang = "fsharp"
            elif "xml" in class_str or "html" in class_str:
                lang = "xml"
            elif "json" in class_str:
                lang = "json"
        
        placeholder = f"<<CODE_BLOCK_{counter}>>"
        code_block_markdown = f"```{lang}\n{code_text}\n```\n"
        code_blocks[placeholder] = code_block_markdown
        new_node = soup.new_string(placeholder)
        pre_tag.replace_with(new_node)
    
    return soup, code_blocks


def clean_markdown_formatting(markdown_text):
    """Clean up the markdown formatting for better readability."""
    # Remove excessive blank lines
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    
    # Improve header formatting
    lines = markdown_text.splitlines()
    for i in range(len(lines)):
        # Ensure proper spacing after header markers
        for level in range(1, 7):
            header_pattern = r'^#{' + str(level) + r'}([^\s])'
            if re.match(header_pattern, lines[i]):
                lines[i] = re.sub(header_pattern, '#' * level + r' \1', lines[i])
    
    formatted_text = '\n'.join(lines)
    
    # Clean up link formatting
    formatted_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'[{m.group(1)}]({m.group(2)})', formatted_text)
    
    # Make GUID links more readable
    guid_pattern = r'\(([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\.md\)'
    formatted_text = re.sub(guid_pattern, r'(reference-\1.md)', formatted_text)
    
    # Remove any remaining JavaScript links
    formatted_text = re.sub(r'\[.*?\]\(javascript:.*?\)', '', formatted_text)
    
    # Remove "See Also Send Feedback" text which often appears in the API docs
    formatted_text = re.sub(r'See Also \[Send Feedback\].*?---', '---', formatted_text)
    
    # Clean up collapse/expand sections
    formatted_text = re.sub(r'Collapse AllExpand All', '', formatted_text)
    formatted_text = re.sub(r'Code: All Code: Multiple.*?---', '---', formatted_text)
    
    # Remove any email links that contain feedback
    formatted_text = re.sub(r'\[Send comments.*?\].*?\)', '', formatted_text)
    
    # Remove excess horizontal rules
    formatted_text = re.sub(r'---\s*---', '---', formatted_text)
    
    return formatted_text


def fix_tables(markdown_text):
    """Improve table formatting in the markdown."""
    lines = markdown_text.splitlines()
    fixed_lines = []
    i = 0
    in_table = False
    
    while i < len(lines):
        # Detect potential table start
        if "|" in lines[i] and i + 1 < len(lines) and re.match(r"^[\s\-\|:]+$", lines[i + 1]):
            in_table = True
            table_lines = []
            # Collect all table lines
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            
            # Fix and format the table
            fixed_table_lines = fix_table_block(table_lines)
            fixed_lines.extend(fixed_table_lines)
            
            # Add an extra newline after the table
            fixed_lines.append("")
            in_table = False
        else:
            fixed_lines.append(lines[i])
            i += 1
    
    return "\n".join(fixed_lines)


def fix_table_block(table_lines):
    """Fix an individual table block for better markdown rendering."""
    # Process and normalize the table structure
    split_lines = [[cell.strip() for cell in line.split("|")] for line in table_lines]
    
    # Strip empty cells from the beginning and end
    processed_lines = []
    for row in split_lines:
        # Remove empty cells at the beginning and end
        if row and row[0] == "":
            row = row[1:]
        if row and row[-1] == "":
            row = row[:-1]
        processed_lines.append(row)
    
    # Generate properly formatted markdown table
    formatted_lines = []
    for i, row in enumerate(processed_lines):
        # Create the table row
        line = "| " + " | ".join(row) + " |"
        formatted_lines.append(line)
        
        # Add the header separator after the first row
        if i == 0:
            separator = "| " + " | ".join(["---" for _ in row]) + " |"
            formatted_lines.append(separator)
    
    return formatted_lines


def convert_html_to_markdown(html_content, file_dictionary=None):
    """Convert HTML content to clean markdown format."""
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the main title to add at the top of markdown
    main_title = extract_page_title(soup)
    
    # Clean up the HTML
    soup = remove_unwanted_elements(soup)
    soup = update_links(soup, file_dictionary)
    soup, code_blocks = replace_code_snippets(soup)
    
    # Convert to markdown
    modified_html = str(soup)
    h = html2text.HTML2Text()
    h.body_width = 0  # No wrapping
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_tables = False
    h.single_line_break = True  # Use only one line break
    h.unicode_snob = True  # Keep Unicode characters
    
    markdown_text = h.handle(modified_html)
    
    # Add the main title at the top if available
    if main_title:
        markdown_text = f"# {main_title}\n\n{markdown_text}"
    
    # Replace code block placeholders
    for placeholder, code_block in code_blocks.items():
        markdown_text = markdown_text.replace(placeholder, code_block)
    
    # Fix tables and clean up formatting
    markdown_text = fix_tables(markdown_text)
    markdown_text = clean_markdown_formatting(markdown_text)
    
    return markdown_text


def clear_folder(folder_path):
    """Delete all files and folders within the specified folder."""
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        os.makedirs(folder_path)


async def export_chm_to_htm(chm_path, export_folder):
    """
    Export HTML files from a CHM file using 7-Zip asynchronously.
    """
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    clear_folder(export_folder)

    seven_zip = r"C:\Program Files\7-Zip\7z.exe"
    if not os.path.exists(seven_zip):
        print(
            "7z.exe not found. Please install 7-Zip and update the seven_zip path accordingly."
        )
        return

    try:
        process = await asyncio.create_subprocess_exec(
            seven_zip,
            "x",
            chm_path,
            f"-o{export_folder}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        print(stdout.decode())
        if stderr:
            print(stderr.decode())
    except Exception as e:
        print(f"Error extracting CHM file using 7z.exe: {e}")


async def build_file_dictionary(input_folder):
    """
    First pass to build a dictionary of all HTML files with their titles.
    This helps in creating meaningful references later.
    """
    html_folder = os.path.join(input_folder, "html")
    if not os.path.exists(html_folder):
        print(f"HTML folder does not exist: {html_folder}")
        return {}
        
    file_dictionary = {}
    semaphore = asyncio.Semaphore(20)  # Limit concurrent file operations
    
    async def process_file_for_dict(filename):
        input_path = os.path.join(html_folder, filename)
        base, _ = os.path.splitext(filename)
        
        try:
            async with semaphore:
                async with aiofiles.open(input_path, "r", encoding="utf-8") as f:
                    html_content = await f.read()
            
            soup = BeautifulSoup(html_content, "html.parser")
            title = extract_page_title(soup)
            
            return base, {
                "title": title if title else "Untitled Document",
                "filename": base + ".md"
            }
        except Exception as e:
            print(f"Error processing {input_path} for dictionary: {e}")
            return base, {
                "title": "Error Document",
                "filename": base + ".md"
            }
    
    # Get all HTML files
    file_list = [f for f in os.listdir(html_folder) if f.lower().endswith((".htm", ".html"))]
    print(f"Building dictionary from {len(file_list)} HTML files...")
    
    # Process all files to build the dictionary
    tasks = [process_file_for_dict(filename) for filename in file_list]
    results = await asyncio.gather(*tasks)
    
    # Build the dictionary from results
    for base, info in results:
        file_dictionary[base] = info
    
    print(f"Dictionary built with {len(file_dictionary)} entries")
    return file_dictionary


async def convert_files_with_dictionary(
    input_folder, output_folder, file_dictionary, 
    max_workers=4, semaphore_limit=20, batch_size=10
):
    """
    Second pass to convert all HTML files to Markdown using the file dictionary.
    """
    html_folder = os.path.join(input_folder, "html")
    if not os.path.exists(html_folder):
        print(f"HTML folder does not exist: {html_folder}")
        return
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    file_list = [f for f in os.listdir(html_folder) if f.lower().endswith((".htm", ".html"))]
    total_files = len(file_list)
    print(f"Converting {total_files} HTML files to Markdown...")
    
    semaphore = asyncio.Semaphore(semaphore_limit)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(0, total_files, batch_size):
            batch_files = file_list[i:i + batch_size]
            batch_tasks = []
            
            for filename in batch_files:
                input_path = os.path.join(html_folder, filename)
                base, _ = os.path.splitext(filename)
                output_path = os.path.join(output_folder, base + ".md")
                
                # Use the already built dictionary for conversion
                batch_tasks.append(
                    process_file(executor, input_path, output_path, semaphore, file_dictionary)
                )
                
            # Process this batch
            await asyncio.gather(*batch_tasks)
            batch_number = (i // batch_size) + 1
            processed = min(i + batch_size, total_files)
            remaining = total_files - processed
            print(f"Batch {batch_number}: Processed {len(batch_files)} files. {remaining} remaining.")
            
    # Create the index files
    await create_index_files(output_folder, file_dictionary)


async def process_file(executor, input_path, output_path, semaphore, file_dictionary):
    """Process a single HTML file asynchronously."""
    loop = asyncio.get_running_loop()
    file_id = os.path.basename(output_path)
    base_filename, _ = os.path.splitext(file_id)
    
    try:
        async with semaphore:
            async with aiofiles.open(input_path, "r", encoding="utf-8") as f:
                html_content = await f.read()
        
        # Convert HTML to Markdown using the file dictionary
        markdown_content = await loop.run_in_executor(
            executor, convert_html_to_markdown, html_content, file_dictionary
        )
        
        async with semaphore:
            async with aiofiles.open(output_path, "w", encoding="utf-8") as f:
                await f.write(markdown_content)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


async def create_index_files(output_folder, file_dictionary):
    """Create JSON and Markdown index files along with an ID-based lookup dictionary."""
    # Create JSON index
    dictionary_path = os.path.join(output_folder, "file_index.json")
    async with aiofiles.open(dictionary_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(file_dictionary, indent=4, ensure_ascii=False))
    
    print(f"Created file index dictionary at {dictionary_path}")
    
    # Create ID-based lookup dictionary
    id_lookup = {}
    for file_id, info in file_dictionary.items():
        # Clean up the ID if needed (e.g., remove file extensions)
        clean_id = file_id.lower()  # Using lowercase for case-insensitive matching
        id_lookup[clean_id] = {
            "title": info['title'],
            "filename": info['filename'],
            "keywords": extract_keywords(info['title'])  # Add keywords for better semantic search
        }
    
    # Save the ID-based lookup dictionary
    id_lookup_path = os.path.join(output_folder, "id_lookup.json")
    async with aiofiles.open(id_lookup_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(id_lookup, indent=4, ensure_ascii=False))
    
    print(f"Created ID-based lookup dictionary at {id_lookup_path}")
    
    # Create Markdown index
    md_index_path = os.path.join(output_folder, "index.md")
    async with aiofiles.open(md_index_path, "w", encoding="utf-8") as f:
        await f.write("# API Documentation Index\n\n")
        
        # Group items by first letter for alphabetical navigation
        sorted_entries = sorted(file_dictionary.items(), key=lambda x: x[1]['title'].lower())
        current_letter = None
        
        # Add alphabetical index at the top
        all_first_letters = sorted(set(entry[1]['title'][0].upper() for entry in sorted_entries if entry[1]['title']))
        alpha_links = [f"[{letter}](#{letter.lower()})" for letter in all_first_letters]
        await f.write("## Quick Navigation\n\n")
        await f.write(" | ".join(alpha_links) + "\n\n")
        
        # Write entries grouped by first letter
        for file_id, info in sorted_entries:
            title = info['title']
            if not title:
                continue
                
            first_letter = title[0].upper()
            if first_letter != current_letter:
                current_letter = first_letter
                await f.write(f"\n## {current_letter}\n<a id='{current_letter.lower()}'></a>\n\n")
            
            filename = info['filename']
            await f.write(f"- [{title}](./{filename})\n")
    
    print(f"Created Markdown index at {md_index_path}")


async def process_folder_async(
    input_folder, output_folder, max_workers=4, semaphore_limit=20, batch_size=10
):
    """
    Main processing function with two passes:
    1. Build a dictionary of all files with their titles
    2. Convert all files using this dictionary for better cross-references
    """
    # First pass: build the file dictionary
    file_dictionary = await build_file_dictionary(input_folder)
    
    # Second pass: convert files with the dictionary
    await convert_files_with_dictionary(
        input_folder, output_folder, file_dictionary,
        max_workers, semaphore_limit, batch_size
    )


async def main():
    # --- Configuration ---
    input_folder = r"C:\Users\duong\Documents\DTDucas\Git\DT\DTRepository\chm-to-markdown\extracted"
    output_folder = r"C:\Users\duong\Documents\DTDucas\Git\DT\DTRepository\chm-to-markdown\extracted\output"
    chm_file_path = r"C:\Users\duong\Documents\DTDucas\Git\DT\DTRepository\chm-to-markdown\resources\2024.chm"  # Set your CHM file path here

    print("Starting CHM to Markdown conversion process...")
    print("Clearing existing folders...")
    clear_folder(input_folder)
    clear_folder(output_folder)

    if (
        chm_file_path
        and os.path.exists(chm_file_path)
        and chm_file_path.lower().endswith(".chm")
    ):
        print(f"Exporting CHM file {chm_file_path} to HTML...")
        await export_chm_to_htm(chm_file_path, input_folder)
    elif chm_file_path:
        print("Provided CHM file does not exist or is not a CHM file.")

    print("Converting HTML files to Markdown with improved formatting...")
    await process_folder_async(
        input_folder, output_folder, max_workers=8, semaphore_limit=20, batch_size=50
    )
    
    print("Conversion completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())