import os
import re


def load_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def split_into_paragraphs(text):
    paragraphs = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paragraphs if len(p.strip()) > 100]


def map_topics_to_content(topics, textbook_text):
    topic_content_map = {}

    paragraphs = split_into_paragraphs(textbook_text)

    for topic in topics:
        topic_keywords = set(topic.lower().split()[:10])
        matched_paragraphs = []

        for para in paragraphs:
            para_lower = para.lower()
            if any(keyword in para_lower for keyword in topic_keywords):
                matched_paragraphs.append(para)

        topic_content_map[topic] = matched_paragraphs

    return topic_content_map


if __name__ == "__main__":
    syllabus_file = "output/syllabus_topics.txt"
    textbook_file = "output/extracted_text.txt"
    output_file = "output/topic_content_map.txt"

    syllabus_text = load_text(syllabus_file)
    topics = [t.strip() for t in syllabus_text.split("\n\n") if t.strip()]

    textbook_text = load_text(textbook_file)

    topic_content = map_topics_to_content(topics, textbook_text)

    with open(output_file, "w", encoding="utf-8") as f:
        for topic, paras in topic_content.items():
            f.write(f"\n=== TOPIC ===\n{topic}\n")
            for p in paras:
                f.write(p + "\n\n")
