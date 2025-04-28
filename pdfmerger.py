import os
import sys
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdfmerger.py <folder_path>")
        sys.exit(1)
        
    pdf_folder = sys.argv[1]
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    # Sort files in ascending order
    pdf_files.sort(key=str.lower)  # Case-insensitive sorting
    
    # Add full path
    pdf_files = [os.path.join(pdf_folder, f) for f in pdf_files]
    
    output_file = "merged_output.pdf"
    merge_pdfs(pdf_files, output_file)
    
    print(f"Successfully merged {len(pdf_files)} PDFs into '{output_file}'.")