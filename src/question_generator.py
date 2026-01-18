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


def generate_questions(topics, difficulty, count):
    templates = QUESTION_TEMPLATES[difficulty]
    selected_topics = random.sample(topics, min(count, len(topics)))

    questions = []
    for topic in selected_topics:
        template = random.choice(templates)
        questions.append(template.format(topic=topic))

    return questions
