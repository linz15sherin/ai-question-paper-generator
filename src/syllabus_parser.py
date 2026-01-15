import pdfplumber
import os
import re


def extract_syllabus_topics(pdf_path):
    """
    Extracts syllabus topics from a syllabus PDF.
    Returns a list of cleaned topic strings.
    """

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Syllabus PDF not found: {pdf_path}")

    full_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)

    combined_text = "\n".join(full_text)

    # Basic cleanup
    combined_text = re.sub(r"\s+", " ", combined_text)

    # Heuristic: split by Unit / Module / Roman numerals / numbering
    raw_topics = re.split(
        r"(?:UNIT\s+\w+|Unit\s+\w+|MODULE\s+\w+|Module\s+\w+|\d+\.)",
        combined_text
    )

    topics = [topic.strip() for topic in raw_topics if len(topic.strip()) > 20]

    print(f"Extracted {len(topics)} syllabus topic blocks.")
    return topics


if __name__ == "__main__":
    syllabus_pdf = "/home/linda/projects/ai-question-paper-generator/data/syllabus.pdf"

    topics = extract_syllabus_topics(syllabus_pdf)


    # Save topics to file
    output_path = "output/syllabus_topics.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        for topic in topics:
            f.write(topic + "\n\n")

   
