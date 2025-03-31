import pathlib
import sys

import pymupdf4llm


def pdf_to_markdown(input_file, output_path):
    md_text = pymupdf4llm.to_markdown(input_file)

    pathlib.Path(output_path).write_bytes(md_text.encode())


def main(input_path):
    output_path = "output.md"  # Path to save the Markdown file
    pdf_to_markdown(input_path, output_path)


if __name__ == "__main__":
    main(sys.argv[1])
