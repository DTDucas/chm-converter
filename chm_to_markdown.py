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


def update_links(soup):
    for a in soup.find_all("a", href=True):
        if a["href"] == "#PageHeader":
            a.decompose()
        elif a["href"].lower().endswith((".htm", ".html")):
            base, _ = os.path.splitext(a["href"])
            a["href"] = base + ".md"
    return soup


def remove_unwanted_elements(soup):
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
    return soup


def replace_code_snippets(soup):
    id_to_lang = {
        "IDAB_code_Div1": "csharp",
        "IDAB_code_Div2": "vb",
        "IDAB_code_Div3": "cpp",
        "IDAB_code_Div4": "fsharp",
    }
    code_blocks = {}
    counter = 0
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
    return soup, code_blocks


def convert_html_to_markdown(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    soup = remove_unwanted_elements(soup)
    soup = update_links(soup)
    soup, code_blocks = replace_code_snippets(soup)
    modified_html = str(soup)
    h = html2text.HTML2Text()
    h.body_width = 0
    markdown_text = h.handle(modified_html)
    for placeholder, code_block in code_blocks.items():
        markdown_text = markdown_text.replace(placeholder, code_block)
    markdown_text = fix_tables(markdown_text)
    return markdown_text


def fix_tables(markdown_text):
    lines = markdown_text.splitlines()
    fixed_lines = []
    i = 0
    while i < len(lines):
        if (
            "|" in lines[i]
            and i + 1 < len(lines)
            and re.match(r"^[\s\-\|:]+$", lines[i + 1])
        ):
            table_lines = []
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            table_lines = fix_table_block(table_lines)
            fixed_lines.extend(table_lines)
        else:
            fixed_lines.append(lines[i])
            i += 1
    return "\n".join(fixed_lines)


def fix_table_block(table_lines):
    split_lines = [[cell.strip() for cell in line.split("|")] for line in table_lines]
    header = split_lines[0]
    if header and header[0] == "":
        header = header[1:]
    remove_first = header and (header[0] == "-" or header[0] == "")
    if remove_first:
        new_split_lines = []
        for row in split_lines:
            if row and row[0] == "":
                row = row[1:]
            new_split_lines.append(row[1:])
    else:
        new_split_lines = split_lines
    new_lines = []
    for row in new_split_lines:
        new_line = "| " + " | ".join(row) + " |"
        new_lines.append(new_line)
    return new_lines


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


async def process_file(executor, input_path, output_path, semaphore, file_dictionary):
    """Process a single HTML file asynchronously and add its info to the dictionary."""
    loop = asyncio.get_running_loop()
    file_id = os.path.basename(output_path)
    base_filename, _ = os.path.splitext(file_id)
    
    try:
        async with semaphore:
            async with aiofiles.open(input_path, "r", encoding="utf-8") as f:
                html_content = await f.read()
        
        # Extract title for the dictionary before converting to markdown
        soup = BeautifulSoup(html_content, "html.parser")
        title = extract_page_title(soup)
        
        # Add entry to dictionary
        if title:
            file_dictionary[base_filename] = {
                "title": title,
                "filename": file_id
            }
        else:
            file_dictionary[base_filename] = {
                "title": "Untitled Document",
                "filename": file_id
            }
            
        markdown_content = await loop.run_in_executor(
            executor, convert_html_to_markdown, html_content
        )
        
        async with semaphore:
            async with aiofiles.open(output_path, "w", encoding="utf-8") as f:
                await f.write(markdown_content)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


async def process_folder_async(
    input_folder, output_folder, max_workers=4, semaphore_limit=20, batch_size=10
):
    """
    Asynchronously process HTML files in batches and create a dictionary mapping.
    """
    html_folder = os.path.join(input_folder, "html")
    if not os.path.exists(html_folder):
        print(f"HTML folder does not exist: {html_folder}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = [
        f for f in os.listdir(html_folder) if f.lower().endswith((".htm", ".html"))
    ]
    total_files = len(file_list)
    print(f"Found {total_files} HTML files to process in {html_folder}")

    # Dictionary to store file mappings (id -> title)
    file_dictionary = {}

    semaphore = asyncio.Semaphore(semaphore_limit)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(0, total_files, batch_size):
            batch_files = file_list[i : i + batch_size]
            batch_tasks = []
            for filename in batch_files:
                input_path = os.path.join(html_folder, filename)
                base, _ = os.path.splitext(filename)
                output_filename = base + ".md"
                output_path = os.path.join(output_folder, output_filename)
                batch_tasks.append(
                    process_file(executor, input_path, output_path, semaphore, file_dictionary)
                )
            await asyncio.gather(*batch_tasks)
            batch_number = (i // batch_size) + 1
            processed_in_batch = len(batch_files)
            remaining = total_files - (i + processed_in_batch)
            print(
                f"Batch {batch_number}: Processed {processed_in_batch} files. {remaining} files remaining."
            )
    
    # Write dictionary to a JSON file
    dictionary_path = os.path.join(output_folder, "file_index.json")
    async with aiofiles.open(dictionary_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(file_dictionary, indent=4, ensure_ascii=False))
    
    print(f"Created file index dictionary at {dictionary_path}")
    
    # Create a human-readable index file in Markdown format
    md_index_path = os.path.join(output_folder, "index.md")
    async with aiofiles.open(md_index_path, "w", encoding="utf-8") as f:
        await f.write("# Document Index\n\n")
        
        # Sort entries by title for the index
        sorted_entries = sorted(file_dictionary.items(), key=lambda x: x[1]['title'])
        
        for file_id, info in sorted_entries:
            title = info['title']
            filename = info['filename']
            await f.write(f"- [{title}](./{filename})\n")
    
    print(f"Created Markdown index at {md_index_path}")


async def main():
    # --- Configuration ---
    input_folder = r"C:\Users\extracted"
    output_folder = r"C:\Users\output"
    chm_file_path = r"C:\Users\2024.chm"  # Set your CHM file path here

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

    print("Converting HTML files to Markdown asynchronously in batches...")
    await process_folder_async(
        input_folder, output_folder, max_workers=8, semaphore_limit=20, batch_size=50
    )


if __name__ == "__main__":
    asyncio.run(main())