# PDF Merger

A simple Python script to merge multiple PDF files from a specified folder into a single PDF file.

## Features

- Merges all PDF files from a specified folder
- Sorts files in ascending order (case-insensitive)
- Creates a single output PDF file named `merged_output.pdf`

## Requirements

- Python 3.x
- PyPDF2

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line, providing the path to the folder containing PDF files:

```bash
python pdfmerger.py /path/to/your/pdf/folder
```

The script will:
1. Find all PDF files in the specified folder
2. Sort them in ascending order
3. Merge them into a single PDF file named `merged_output.pdf` in the current directory

## Example

If you have PDF files in a folder called `documents`, you would run:

```bash
python pdfmerger.py documents
```

The script will create `merged_output.pdf` containing all PDFs from the `documents` folder in sorted order.

## Notes

- The output file will be created in the current directory where the script is run
- Only files with `.pdf` extension will be included in the merge
- Files are sorted case-insensitively 