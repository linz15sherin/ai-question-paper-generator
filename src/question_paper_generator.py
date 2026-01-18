from question_generator import load_topic_content_map, generate_questions
from question_paper_pattern import QUESTION_PAPER_PATTERN


def generate_question_paper(topic_content_map):
    question_paper = {}

    topics = list(topic_content_map.keys())

    for section, config in QUESTION_PAPER_PATTERN.items():
        questions = generate_questions(
            topics=topics,
            difficulty=config["difficulty"],
            count=config["num_questions"]
        )
        question_paper[section] = {
            "marks_each": config["marks_each"],
            "questions": questions
        }

    return question_paper


if __name__ == "__main__":
    input_file = "output/topic_content_map.txt"
    output_file = "output/question_paper.txt"

    topic_map = load_topic_content_map(input_file)
    question_paper = generate_question_paper(topic_map)

    with open(output_file, "w", encoding="utf-8") as f:
        for section, details in question_paper.items():
            f.write(f"\n{section} ({details['marks_each']} Marks Each)\n")
            f.write("-" * 40 + "\n")
            for i, q in enumerate(details["questions"], start=1):
                f.write(f"{i}. {q}\n")
