PDFExamGrader

PDFExamGrader is an automated tool designed to grade exams from PDF files.

Features:
- Reads answers from PDF exam files
- Automatically compares student answers with the answer key
- Generates PDFs with grading results

Installation:
1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/PDFExamGrader.git

2. Navigate to the project directory:
   cd PDFExamGrader

3. Create a virtual environment and install the dependencies:
   python -m venv .venv
   .venv\Scripts\activate  # On Windows 
   pip install -r requirements.txt

Usage:
1. Place the answer PDF files in the 'pdfs' directory.
2. Run the main script to read and grade the answers:
   python recive-answers.py

3. The grading results will be generated in the 'results' directory.

Configuration:
You can adjust paths and other settings in the 'config.json' file.

Contributing:
Contributions are welcome! Feel free to open issues and pull requests.

License:
This project is licensed under the APACHE 2.0. See the LICENSE file for more details.
