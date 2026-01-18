import random
import os
from question_patterns import QUESTION_TEMPLATES


def load_topic_content_map(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    topic_map = {}
    current_topic = None

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line == "=== TOPIC ===":
                current_topic = None
            elif current_topic is None:
                current_topic = line
                topic_map[current_topic] = []
            elif line:
                topic_map[current_topic].append(line)

    return topic_map


def generate_questions(topic_map, difficulty="medium", questions_per_topic=1):
    questions = []

    templates = QUESTION_TEMPLATES.get(difficulty, [])

    for topic in topic_map:
        for _ in range(questions_per_topic):
            template = random.choice(templates)
            question = template.format(topic=topic)
            questions.append(question)

    return questions


if __name__ == "__main__":
    input_file = "output/topic_content_map.txt"
    output_file = "output/generated_questions.txt"

    topic_map = load_topic_content_map(input_file)

    questions = generate_questions(
        topic_map,
        difficulty="medium",
        questions_per_topic=1
    )

    with open(output_file, "w", encoding="utf-8") as f:
        for q in questions:
            f.write(q + "\n")

