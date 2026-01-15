# ai-question-paper-generator
AI-based system to generate question papers using syllabus and textbook PDFs
# AI-Based Question Paper Generator

## Project Status
- [x] Project repository created on GitHub
- [x] Initial project structure (`src/`, `data/`, `output/`, `main.py`)
- [x] Python virtual environment created
- [x] Dependency `pdfplumber` installed
- [x] PDF text extraction module implemented (`src/pdf_parser.py`)
- [ ] Syllabus parsing module (Next)
- [ ] AI/ML question generation logic (Next)
- [ ] Output formatting (question paper generation)

## Current Functionality
- Extracts text from a PDF textbook
- Saves the extracted text to `output/extracted_text.txt`

## Next Steps
- Implement keyword/topic extraction from extracted text
- Map extracted topics to syllabus units
- Generate questions based on selected pattern and complexity
