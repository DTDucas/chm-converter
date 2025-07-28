import os
import re
import json
import shutil
import asyncio
import argparse
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import html2text
import aiofiles

tags_to_remove = ["iframe", "object", "script", "br", "img", "meta", "link", "input"]
classes_to_remove = [
    "collapsibleAreaRegion",
    "collapsibleRegionTitle",
    "collapseToggle",
    "codeSnippetContainerTab",
    "codeSnippetToolBar",
    "codeSnippetContainerTabs",
    "pageHeader",
    "feedbackLink",
    "userDataStyle",
]
ids_to_remove = [
    "PageFooter",
    "PageHeader",
    "TopicContent",
    "userDataCache",
    "HT_MailLink",
]
DTDUCAS_LOGO = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ________    | || |  _________   | || |  ________    | || | _____  _____ | || |     ______   | || |      __      | || |    _______   | |
| | |_   ___ `.  | || | |  _   _  |  | || | |_   ___ `.  | || ||_   _||_   _|| || |   .' ___  |  | || |     /  \     | || |   /  ___  |  | |
| |   | |   `. \ | || | |_/ | | \_|  | || |   | |   `. \ | || |  | |    | |  | || |  / .'   \_|  | || |    / /\ \    | || |  |  (__ \_|  | |
| |   | |    | | | || |     | |      | || |   | |    | | | || |  | '    ' |  | || |  | |         | || |   / ____ \   | || |   '.___`-.   | |
| |  _| |___.' / | || |    _| |_     | || |  _| |___.' / | || |   \ `--' /   | || |  \ `.___.'\  | || | _/ /    \ \_ | || |  |`\____) |  | |
| | |________.'  | || |   |_____|    | || | |________.'  | || |    `.__.'    | || |   `._____.'  | || ||____|  |____|| || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
Duong Tran Quang - DTDucas (baymax.contact@gmail.com)
"""

def extract_page_title(soup):
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        title = title_tag.string.strip()
        return title
    h1_tag = soup.find("h1")
    if h1_tag and h1_tag.get_text():
        title = h1_tag.get_text().strip()
        return title
    for heading_level in range(2, 7):
        heading = soup.find(f"h{heading_level}")
        if heading and heading.get_text():
            title = heading.get_text().strip()
            return title
    return None


def extract_keywords(title):
    if not title:
        return []
    stopwords = {
        "a",
        "an",
        "the",
        "and",
        "or",
        "of",
        "to",
        "in",
        "for",
        "with",
        "on",
        "at",
        "by",
        "is",
        "are",
        "was",
        "were",
    }
    words = re.findall(r"\b\w+\b", title.lower())
    keywords = [word for word in words if word not in stopwords and len(word) > 2]
    if title.lower() not in keywords:
        keywords.append(title.lower())
    return keywords


def update_links(soup, file_dictionary=None):
    for a in soup.find_all("a", href=True):
        if a["href"] == "#PageHeader":
            a.decompose()
        elif a["href"].lower().endswith((".htm", ".html")):
            # Grab this from memory and make a copy
            href = a["href"]
            # Get the relative path, but without the .htm/.html file extension
            # (e.g. mysubdirectory/anothersubdirectory/actualFile )
            # Note that these links will be relative to their parent file, NOT relative to the main html folder
            relPath, relPath_ext = os.path.splitext(href)
            a["href"] = relPath + ".md"
            if file_dictionary and relPath in file_dictionary:
                display_name = file_dictionary[relPath].get("title")
                if display_name:
                    a["title"] = display_name
    return soup


def remove_unwanted_elements(soup):
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
    for a in soup.find_all(
        "a", href=lambda href: href and "javascript:" in str(href).lower()
    ):
        a.decompose()
    for a in soup.find_all(
        "a", href=lambda href: href and "mailto:" in str(href).lower()
    ):
        a.decompose()
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
    for pre_tag in soup.find_all("pre"):
        counter += 1
        code_text = pre_tag.get_text()
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
    markdown_text = re.sub(r"\n{3,}", "\n\n", markdown_text)
    lines = markdown_text.splitlines()
    for i in range(len(lines)):
        for level in range(1, 7):
            header_pattern = r"^#{" + str(level) + r"}([^\s])"
            if re.match(header_pattern, lines[i]):
                lines[i] = re.sub(header_pattern, "#" * level + r" \1", lines[i])
    formatted_text = "\n".join(lines)
    formatted_text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f"[{m.group(1)}]({m.group(2)})",
        formatted_text,
    )
    guid_pattern = (
        r"\(([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\.md\)"
    )
    formatted_text = re.sub(guid_pattern, r"(reference-\1.md)", formatted_text)
    formatted_text = re.sub(r"\[.*?\]\(javascript:.*?\)", "", formatted_text)
    formatted_text = re.sub(r"See Also \[Send Feedback\].*?---", "---", formatted_text)
    formatted_text = re.sub(r"Collapse AllExpand All", "", formatted_text)
    formatted_text = re.sub(r"Code: All Code: Multiple.*?---", "---", formatted_text)
    formatted_text = re.sub(r"\[Send comments.*?\].*?\)", "", formatted_text)
    formatted_text = re.sub(r"---\s*---", "---", formatted_text)
    return formatted_text


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
            fixed_table_lines = fix_table_block(table_lines)
            fixed_lines.extend(fixed_table_lines)
            fixed_lines.append("")
        else:
            fixed_lines.append(lines[i])
            i += 1
    return "\n".join(fixed_lines)


def fix_table_block(table_lines):
    split_lines = [[cell.strip() for cell in line.split("|")] for line in table_lines]
    processed_lines = []
    for row in split_lines:
        if row and row[0] == "":
            row = row[1:]
        if row and row[-1] == "":
            row = row[:-1]
        processed_lines.append(row)
    formatted_lines = []
    for i, row in enumerate(processed_lines):
        line = "| " + " | ".join(row) + " |"
        formatted_lines.append(line)
        if i == 0:
            separator = "| " + " | ".join(["---" for _ in row]) + " |"
            formatted_lines.append(separator)
    return formatted_lines


def convert_html_to_markdown(html_content, file_dictionary=None, version=None):
    soup = BeautifulSoup(html_content, "html.parser")
    main_title = extract_page_title(soup)
    soup = remove_unwanted_elements(soup)
    soup = update_links(soup, file_dictionary)
    soup, code_blocks = replace_code_snippets(soup)
    modified_html = str(soup)
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_tables = False
    h.single_line_break = True
    h.unicode_snob = True
    markdown_text = h.handle(modified_html)
    if main_title:
        if version:
            markdown_text = f"# {main_title} ({version})\n\n{markdown_text}"
        else:
            markdown_text = f"# {main_title}\n\n{markdown_text}"
    for placeholder, code_block in code_blocks.items():
        markdown_text = markdown_text.replace(placeholder, code_block)
    markdown_text = fix_tables(markdown_text)
    markdown_text = clean_markdown_formatting(markdown_text)
    return markdown_text


def clear_folder(folder_path):
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
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
    clear_folder(export_folder)
    seven_zip = r"C:\Program Files\7-Zip\7z.exe"
    if not os.path.exists(seven_zip):
        print(
            "7z.exe not found. Please install 7-Zip and update the seven_zip path accordingly."
        )
        return False
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
        if process.returncode != 0:
            print(f"Error extracting {chm_path}:")
            print(stderr.decode())
            return False
        return True
    except Exception as e:
        print(f"Error extracting CHM file using 7z.exe: {e}")
        return False


async def build_file_dictionary(input_folder, version=None):
    html_parent_folder = os.path.join(input_folder, "html")
    if not os.path.exists(html_parent_folder):
        print(f"HTML folder does not exist: {html_parent_folder}")
        return {}
    file_dictionary = {}
    semaphore = asyncio.Semaphore(20)

    async def process_file_for_dict(fileRelPath):
        input_path = os.path.join(html_parent_folder, fileRelPath)
        base, _ = os.path.splitext(fileRelPath)
        try:
            async with semaphore:
                async with aiofiles.open(
                    input_path, "r", encoding="utf-8", errors="ignore"
                ) as f:
                    html_content = await f.read()
            soup = BeautifulSoup(html_content, "html.parser")
            title = extract_page_title(soup)
            file_info = {
                "title": title if title else "Untitled Document",
                "filename": base + ".md",
            }
            if version:
                file_info["version"] = version
            return base, file_info
        except Exception as e:
            print(f"Error processing {input_path} for dictionary: {e}")
            return base, {
                "title": "Error Document",
                "filename": base + ".md",
                "version": version if version else None,
            }

    file_list = [
        # Commenting this out while I try to get it to traverse directory trees
        #f for f in os.listdir(html_parent_folder) if f.lower().endswith((".htm", ".html"))
    ]

    for root, dirs, files in os.walk(html_parent_folder):
        for file in files:
            if file.endswith((".html", ".htm")):
                file_list.append(
                    os.path.relpath(
                        os.path.join(root, file),
                        html_parent_folder
                    )
                )

    print(f"Building dictionary from {len(file_list)} HTML files...")
    tasks = [process_file_for_dict(fileRelPath) for fileRelPath in file_list]
    results = await asyncio.gather(*tasks)
    for base, info in results:
        file_dictionary[base] = info
    print(f"Dictionary built with {len(file_dictionary)} entries")
    return file_dictionary


async def convert_files_with_dictionary(
    input_folder,
    output_folder,
    data_folder,
    core_folder,
    file_dictionary,
    version=None,
    max_workers=4,
    semaphore_limit=20,
    batch_size=10,
):
    html_parent_folder = os.path.join(input_folder, "html")
    if not os.path.exists(html_parent_folder):
        print(f"HTML folder does not exist: {html_parent_folder}")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    if not os.path.exists(core_folder):
        os.makedirs(core_folder)

    file_list = []
    for root, dirs, files in os.walk(html_parent_folder):
        for file in files:
            if file.endswith((".html", ".htm")):
                file_list.append(
                    os.path.relpath(
                        os.path.join(root, file),
                        html_parent_folder
                    )
                )

    
    total_files = len(file_list)
    print(f"Converting {total_files} HTML files to Markdown...")
    semaphore = asyncio.Semaphore(semaphore_limit)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(0, total_files, batch_size):
            batch_files = file_list[i : i + batch_size]
            batch_tasks = []
            for filename in batch_files:
                input_path = os.path.join(html_parent_folder, filename)
                base, _ = os.path.splitext(filename)
                output_path = os.path.join(data_folder, base + ".md")
                batch_tasks.append(
                    process_file(
                        executor,
                        input_path,
                        output_path,
                        semaphore,
                        file_dictionary,
                        version,
                    )
                )
            await asyncio.gather(*batch_tasks)
            batch_number = (i // batch_size) + 1
            processed = min(i + batch_size, total_files)
            remaining = total_files - processed
            print(
                f"Batch {batch_number}: Processed {len(batch_files)} files. {remaining} remaining."
            )
    await create_index_files(core_folder, file_dictionary, version)


async def process_file(
    executor, input_path, output_path, semaphore, file_dictionary, version=None
):
    loop = asyncio.get_running_loop()
    try:
        async with semaphore:
            async with aiofiles.open(
                input_path, "r", encoding="utf-8", errors="ignore"
            ) as f:
                html_content = await f.read()
        markdown_content = await loop.run_in_executor(
            executor, convert_html_to_markdown, html_content, file_dictionary, version
        )
        async with semaphore:
            parent_dir = os.path.dirname(output_path)
            await aiofiles.os.makedirs(parent_dir, exist_ok=True)
            async with aiofiles.open(output_path, "w", encoding="utf-8") as f:
                await f.write(markdown_content)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")


async def create_index_files(core_folder, file_dictionary, version=None):
    dictionary_path = os.path.join(core_folder, "file_index.json")
    async with aiofiles.open(dictionary_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(file_dictionary, indent=4, ensure_ascii=False))
    print(f"Created file index dictionary at {dictionary_path}")
    id_lookup = {}
    for file_id, info in file_dictionary.items():
        clean_id = file_id.lower()
        id_lookup[clean_id] = {
            "title": info["title"],
            "filename": info["filename"],
            "keywords": extract_keywords(info["title"]),
        }
        if version:
            id_lookup[clean_id]["version"] = version
        elif "version" in info:
            id_lookup[clean_id]["version"] = info["version"]
    id_lookup_path = os.path.join(core_folder, "id_lookup.json")
    async with aiofiles.open(id_lookup_path, "w", encoding="utf-8") as f:
        await f.write(json.dumps(id_lookup, indent=4, ensure_ascii=False))
    print(f"Created ID-based lookup dictionary at {id_lookup_path}")
    md_index_path = os.path.join(core_folder, "index.md")

    async with aiofiles.open(md_index_path, "w", encoding="utf-8") as f:
        if version:
            await f.write(f"# API Documentation Index - Version {version}\n\n")
        else:
            await f.write("# API Documentation Index\n\n")
        sorted_entries = sorted(
            file_dictionary.items(), key=lambda x: x[1]["title"].lower()
        )
        current_letter = None
        all_first_letters = sorted(
            set(
                entry[1]["title"][0].upper()
                for entry in sorted_entries
                if entry[1]["title"]
            )
        )
        alpha_links = [f"[{letter}](#{letter.lower()})" for letter in all_first_letters]
        await f.write("## Quick Navigation\n\n")
        await f.write(" | ".join(alpha_links) + "\n\n")
        for file_id, info in sorted_entries:
            title = info["title"]
            if not title:
                continue
            first_letter = title[0].upper()
            if first_letter != current_letter:
                current_letter = first_letter
                await f.write(
                    f"\n## {current_letter}\n<a id='{current_letter.lower()}'></a>\n\n"
                )
            filename = info["filename"]
            await f.write(f"- [{title}](../data/{filename})\n")
    print(f"Created Markdown index at {md_index_path}")


async def process_chm_file(
    chm_file_path,
    base_input_folder,
    base_output_folder,
    max_workers=4,
    semaphore_limit=20,
    batch_size=10,
):
    version = os.path.splitext(os.path.basename(chm_file_path))[0]
    print(f"\n=== Processing {version} ===")
    input_folder = os.path.join(base_input_folder, version)
    output_folder = os.path.join(base_output_folder, version)
    data_folder = os.path.join(output_folder, "data")
    core_folder = os.path.join(output_folder, "core")
    for folder in [input_folder, output_folder, data_folder, core_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    print(f"Extracting {chm_file_path} to {input_folder}...")
    success = await export_chm_to_htm(chm_file_path, input_folder + "/html")
    if not success:
        print(f"Failed to extract {chm_file_path}. Skipping this version.")
        return False
    file_dictionary = await build_file_dictionary(input_folder, version)
    await convert_files_with_dictionary(
        input_folder,
        output_folder,
        data_folder,
        core_folder,
        file_dictionary,
        version,
        max_workers,
        semaphore_limit,
        batch_size,
    )
    shutil.rmtree(os.path.join(input_folder, "html"), ignore_errors=True)
    print(f"\n=== Completed processing {version} ===")
    return True


async def process_all_chm_files(
    resources_folder,
    base_input_folder,
    base_output_folder,
    max_workers=8,
    semaphore_limit=20,
    batch_size=50,
):
    chm_files = [
        os.path.join(resources_folder, f)
        for f in os.listdir(resources_folder)
        if f.lower().endswith(".chm")
    ]
    if not chm_files:
        print(f"No CHM files found in {resources_folder}.")
        return
    print(f"Found {len(chm_files)} CHM files to process.")
    results = []
    for chm_file in chm_files:
        result = await process_chm_file(
            chm_file,
            base_input_folder,
            base_output_folder,
            max_workers,
            semaphore_limit,
            batch_size,
        )
        results.append((chm_file, result))
    print("\n=== Processing Summary ===")
    success_count = sum(1 for _, result in results if result)
    print(f"Successfully processed {success_count} out of {len(chm_files)} CHM files.")
    if success_count < len(chm_files):
        print("Failed to process the following CHM files:")
        for chm_file, result in results:
            if not result:
                print(f"  - {os.path.basename(chm_file)}")


async def main():
    print(DTDUCAS_LOGO)
    parser = argparse.ArgumentParser(description="Convert CHM files to Markdown format")
    parser.add_argument("--single", "-s", help="Process a single CHM file")
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Process all CHM files in resources folder",
    )
    parser.add_argument(
        "--keep-html",
        "-k",
        action="store_true",
        help="Keep HTML files after conversion",
    )
    parser.add_argument(
        "--workers", "-w", type=int, default=8, help="Number of worker threads"
    )
    parser.add_argument(
        "--batch-size", "-b", type=int, default=50, help="Batch size for processing"
    )
    parser.add_argument(
        "--semaphore",
        type=int,
        default=20,
        help="Semaphore limit for concurrent operations",
    )
    args = parser.parse_args()
    resources_folder = r"resources"
    base_input_folder = r"extracted"
    base_output_folder = r"output"
    if not os.path.exists(base_output_folder):
        os.makedirs(base_output_folder)
    if args.single:
        chm_file_path = args.single
        if not os.path.exists(chm_file_path):
            chm_file_path = os.path.join(resources_folder, chm_file_path)
            if not os.path.exists(chm_file_path):
                print(f"CHM file not found: {args.single}")
                return
        await process_chm_file(
            chm_file_path,
            base_input_folder,
            base_output_folder,
            args.workers,
            args.semaphore,
            args.batch_size,
        )
    elif args.all:
        await process_all_chm_files(
            resources_folder,
            base_input_folder,
            base_output_folder,
            args.workers,
            args.semaphore,
            args.batch_size,
        )
    else:
        chm_files = [
            f for f in os.listdir(resources_folder) if f.lower().endswith(".chm")
        ]
        if not chm_files:
            print(
                f"No CHM files found in {resources_folder}. Please add CHM files to this folder."
            )
            return
        print("Available CHM files:")
        for i, chm_file in enumerate(chm_files, 1):
            print(f"{i}. {chm_file}")
        try:
            choice = input(
                "\nEnter the number of the CHM file to process (or 'a' for all): "
            )
            if choice.lower() in ["a", "all"]:
                await process_all_chm_files(
                    resources_folder,
                    base_input_folder,
                    base_output_folder,
                    args.workers,
                    args.semaphore,
                    args.batch_size,
                )
            else:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(chm_files):
                        await process_chm_file(
                            os.path.join(resources_folder, chm_files[index]),
                            base_input_folder,
                            base_output_folder,
                            args.workers,
                            args.semaphore,
                            args.batch_size,
                        )
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'a'.")
        except Exception as e:
            print(f"Error during processing: {e}")
    if not args.keep_html and os.path.exists(base_input_folder):
        shutil.rmtree(base_input_folder)
    print("Conversion completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
