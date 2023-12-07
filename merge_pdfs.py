import os
import argparse
from PyPDF2 import PdfMerger


def merge_pdfs(directory):
    # Get a list of PDF files in the directory
    pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]

    # Sort the files if needed
    pdf_files.sort()

    # Initialize PDF merger
    merger = PdfMerger()

    # Merge PDF files
    for filename in pdf_files:
        merger.append(os.path.join(directory, filename))

    # Output file name and path in the same directory
    output_file = os.path.join(directory, 'merged_file.pdf')

    # Write merged PDF to output file
    merger.write(output_file)
    merger.close()

    print(f"\nMerged PDF file saved as '{output_file}' !!! \n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge multiple PDFs from a directory into one.')
    parser.add_argument('directory', help='Path to the directory containing PDF files')

    args = parser.parse_args()
    merge_pdfs(args.directory)
