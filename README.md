# CHM to Markdown Converter

A Python utility for converting Compiled HTML Help (CHM) files to Markdown format. This tool extracts HTML files from CHM documents and converts them to well-formatted Markdown files, making technical documentation more accessible and version control friendly.

## Features

- Extracts CHM files using 7-Zip
- Converts HTML content to clean Markdown format
- Special handling for code snippets with language-specific syntax highlighting
- Preserves and fixes tables
- Updates internal links to maintain document references
- Processes files asynchronously for better performance
- Batch processing with progress reporting

## Requirements

- Python 3.7+
- 7-Zip installed in the default location (`C:\Program Files\7-Zip\7z.exe`)
- The following Python packages:
  - beautifulsoup4
  - html2text
  - aiofiles

## Installation

1. Clone or download this repository
2. Install required Python packages:

```bash
pip install -r requirements.txt
```

Or install them directly:

```bash
pip install beautifulsoup4 html2text aiofiles
```

## Usage

1. Edit the configuration variables in the `main()` function of `chm_to_markdown.py`:

```python
input_folder = r"C:\Path\To\Extracted\Files"  # Temporary folder for extracting CHM
output_folder = r"C:\Path\To\Output\Markdown"  # Where Markdown files will be saved
chm_file_path = r"C:\Path\To\Your\File.chm"    # Your CHM file path
```

2. Run the script:

```bash
python chm_to_markdown.py
```

3. The script will:
   - Clear the input and output folders
   - Extract CHM files to the input folder
   - Convert HTML files to Markdown
   - Save the Markdown files to the output folder

## Performance Tuning

You can adjust the following parameters in the `process_folder_async()` call to optimize performance for your system:

- `max_workers`: Number of worker threads for CPU-bound operations
- `semaphore_limit`: Maximum concurrent file I/O operations
- `batch_size`: Number of files to process in each batch

```python
await process_folder_async(
    input_folder, output_folder, max_workers=8, semaphore_limit=20, batch_size=50
)
```

## Customization

The script provides several customization options for content conversion:

### Removing Unwanted Elements

You can customize which HTML elements to remove by editing these lists:

```python
tags_to_remove = ["iframe", "object", "script", "br", "img"]
classes_to_remove = ["collapsibleAreaRegion", "collapsibleRegionTitle", ...]
ids_to_remove = ["PageFooter"]
```

### Code Snippets

The script handles code snippets with language-specific formatting. You can customize the language mapping:

```python
id_to_lang = {
    "IDAB_code_Div1": "csharp",
    "IDAB_code_Div2": "vb",
    "IDAB_code_Div3": "cpp",
    "IDAB_code_Div4": "fsharp",
}
```

## Troubleshooting

- **Missing modules error**: Make sure you've installed all required packages and your Python environment is correctly configured.
- **7-Zip not found**: Check that 7-Zip is installed in the default location or update the path in the script.
- **Permission errors**: Run your terminal or command prompt with administrator privileges.
- **Memory issues with large CHM files**: Try increasing the batch size and reducing max_workers to manage memory usage.

## License

This project is open source and available under the MIT License.
