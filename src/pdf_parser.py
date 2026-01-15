import pdfplumber
import os


def extract_text_from_pdf(pdf_path, output_txt_path):
    """
    Extracts text from a PDF file and saves it to a text file.
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    extracted_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                extracted_text.append(f"\n--- Page {page_number} ---\n")
                extracted_text.append(text)

    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(extracted_text))

    print(f"Text extraction completed. Output saved to {output_txt_path}")


if __name__ == "__main__":
    input_pdf = "/home/linda/projects/ai-question-paper-generator/data/dbms_textbook.pdf"
    output_text = "output/extracted_text.txt"

    extract_text_from_pdf(input_pdf, output_text)
