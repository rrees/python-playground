import os
import pathlib
import sys

import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text


def pdf_to_text(pdf_path, output_path):
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    pathlib.Path(output_path).write_text(pdf_text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: extract_text.py input_pdf output_path")
        os.exit(1)

    pdf_to_text(sys.argv[1], sys.argv[2])
