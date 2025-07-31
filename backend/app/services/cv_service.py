import io
import re
from docx import Document
import PyPDF2

def check_sections(text: str, required_sections: list) -> dict:
    """
    Check if required CV sections are present in the parsed text.
    Returns dict with sections found/missing lists.
    """
    text_lower = text.lower()
    found = []
    missing = []

    for section in required_sections:
        # Use simple case-insensitive search with word boundary for accuracy
        if re.search(r"\b" + re.escape(section.lower()) + r"\b", text_lower):
            found.append(section)
        else:
            missing.append(section)

    return {"found_sections": found, "missing_sections": missing}

def parse_resume(file_content: bytes, filename: str) -> dict:
    """
    Parses the resume content based on file extension.
    Supports .pdf, .docx, and plain text files.
    Checks for required CV sections.
    Returns extracted info and summary.
    """
    text = ""
    lower_fname = filename.lower()

    try:
        if lower_fname.endswith(".docx"):
            doc = Document(io.BytesIO(file_content))
            text = "\n".join([para.text for para in doc.paragraphs])

        elif lower_fname.endswith(".pdf"):
            reader = PyPDF2.PdfReader(io.BytesIO(file_content))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        elif lower_fname.endswith(".txt"):
            text = file_content.decode("utf-8")

        else:
            return {
                "filename": filename,
                "message": "Unsupported file type. Please upload a .pdf, .docx, or .txt file."
            }

        word_count = len(text.split())
        preview = text[:500]

        # Customize list based on CV expectations
        required_sections = [
            "Contact Information",
            "Summary",
            "Work Experience",
            "Education",
            "Skills",
            "Certifications",
            "Projects"
        ]

        sections_check = check_sections(text, required_sections)

        return {
            "filename": filename,
            "word_count": word_count,
            "preview": preview,
            "sections_found": sections_check["found_sections"],
            "sections_missing": sections_check["missing_sections"],
            "message": "Resume parsed successfully."
        }

    except Exception as e:
        return {
            "filename": filename,
            "message": f"Error parsing resume: {str(e)}"
        }

