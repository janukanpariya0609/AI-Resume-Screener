# ==========================================================
# AI Resume Screening System
# Resume Parser
# Supports PDF, DOCX and TXT
# ==========================================================

import fitz                     # PyMuPDF
import pdfplumber
import docx
import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# ==========================================================
# Read PDF
# ==========================================================

def read_pdf(file):

    text = ""

    try:
        pdf = fitz.open(stream=file.read(), filetype="pdf")

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except:
        file.seek(0)

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text

    return text


# ==========================================================
# Read DOCX
# ==========================================================

def read_docx(file):

    doc = docx.Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


# ==========================================================
# Read TXT
# ==========================================================

def read_txt(file):

    return file.read().decode("utf-8")


# ==========================================================
# Main Resume Reader
# ==========================================================

def extract_resume_text(uploaded_file):

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "pdf":
        return read_pdf(uploaded_file)

    elif extension == "docx":
        return read_docx(uploaded_file)

    elif extension == "txt":
        return read_txt(uploaded_file)

    else:
        return ""


# ==========================================================
# Extract Email
# ==========================================================

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    emails = re.findall(pattern, text)

    if emails:
        return emails[0]

    return "Not Found"


# ==========================================================
# Extract Phone Number
# ==========================================================

def extract_phone(text):

    pattern = r'(\+?\d[\d\-\s]{8,15}\d)'

    phones = re.findall(pattern, text)

    if phones:
        return phones[0]

    return "Not Found"


# ==========================================================
# Extract Name using NLP
# ==========================================================

# ==========================================================
# Extract Full Name
# ==========================================================

def extract_name(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    ignore_words = [
        "resume", "curriculum", "vitae",
        "email", "phone", "mobile",
        "address", "linkedin", "github",
        "education", "experience", "skills",
        "projects", "certifications",
        "objective", "summary", "profile"
    ]

    # 1. Check "Name :" field
    for line in lines[:15]:
        if line.lower().startswith("name"):
            parts = re.split(r":|-", line, maxsplit=1)
            if len(parts) > 1:
                return parts[1].strip()

    # 2. Check first few lines
    for line in lines[:10]:

        lower = line.lower()

        if any(word in lower for word in ignore_words):
            continue

        # Skip lines with numbers or email
        if any(char.isdigit() for char in line):
            continue

        if "@" in line:
            continue

        words = line.split()

        # 2 to 4 capitalized words
        if (
            2 <= len(words) <= 4
            and all(
                w[0].isupper() for w in words
                if w[0].isalpha()
            )
        ):
            return line

    # 3. spaCy fallback
    doc = nlp(text[:1000])

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if len(ent.text.split()) >= 2:
                return ent.text

    return "Not Found"


# ==========================================================
# Experience
# ==========================================================

def extract_experience(text):

    text = text.lower()

    # Fresher keywords
    fresher_words = [
        "fresher",
        "no experience",
        "entry level",
        "entry-level"
    ]

    for word in fresher_words:
        if word in text:
            return 0

    # Match patterns like:
    # 2 years
    # 2+ years
    # 2 yrs
    # 2 yr

    pattern = r'(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)'

    matches = re.findall(pattern, text)

    if matches:

        values = [float(x) for x in matches]

        return max(values)

    return 0


# ==========================================================
# Education
# ==========================================================

def extract_education(text):

    education_patterns = {
        "Bachelor of Engineering (B.E.)": r"\b(bachelor of engineering|b\.?\s*e\.?)\b",
        "Bachelor of Technology (B.Tech)": r"\b(bachelor of technology|b\.?\s*tech\.?)\b",
        "Bachelor of Computer Applications (BCA)": r"\b(bachelor of computer applications|bca)\b",
        "Bachelor of Science (B.Sc.)": r"\b(bachelor of science|b\.?\s*sc\.?)\b",
        "Master of Technology (M.Tech)": r"\b(master of technology|m\.?\s*tech\.?)\b",
        "Master of Business Administration (MBA)": r"\b(master of business administration|mba)\b",
        "Master of Computer Applications (MCA)": r"\b(master of computer applications|mca)\b",
        "Master of Science (M.Sc.)": r"\b(master of science|m\.?\s*sc\.?)\b",
        "Diploma": r"\bdiploma\b",
        "PhD": r"\b(phd|doctor of philosophy)\b"
    }

    found = []

    lower_text = text.lower()

    for degree, pattern in education_patterns.items():

        if re.search(pattern, lower_text):
            found.append(degree)

    return found

# ==========================================================
# Certifications
# ==========================================================

def extract_certifications(text):

    patterns = [
        ("AWS", ["aws"]),
        ("Google", ["google"]),
        ("Microsoft", ["microsoft"]),
        ("IBM", ["ibm"]),
        ("Cisco", ["cisco"]),
        ("Oracle", ["oracle"]),
        ("NPTEL", ["nptel"]),
        ("Coursera", ["coursera"]),
        ("Udemy", ["udemy"]),
        ("Edunet", ["edunet"]),
        ("Knowledge Consortium of Gujarat", ["knowledge consortium of gujarat", "kcg"]),
        ("CSRBOX", ["csrbox", "csr box"]),
        ("AICTE", ["aicte"])
    ]

    found = []
    normalized_text = re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()

    for cert, aliases in patterns:
        if any(alias in normalized_text for alias in aliases):
            found.append(cert)

    return list(set(found))


# ==========================================================
# Projects
# ==========================================================

def extract_projects(text):

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    project_entries = []

    for line in lines:
        lower_line = line.lower()
        if any(keyword in lower_line for keyword in ["project", "projects", "developed", "built", "created", "implemented"]):
            if not any(marker in lower_line for marker in ["education", "experience", "skills", "certification", "certifications"]):
                project_entries.append(line.strip())

    if not project_entries:
        return 0

    unique_projects = []
    seen = set()

    for entry in project_entries:
        cleaned = re.sub(r"\s+", " ", entry).strip()
        cleaned = cleaned.rstrip(":")
        cleaned = re.sub(r"^[-*•]\s*", "", cleaned)
        cleaned = re.sub(r"^projects\s*:", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"^project\s*:", "", cleaned, flags=re.IGNORECASE)
        cleaned = cleaned.strip()

        if cleaned.lower() in {"projects", "project"}:
            continue

        if not cleaned:
            continue

        if cleaned.lower() not in seen:
            seen.add(cleaned.lower())
            unique_projects.append(cleaned)

    return len(unique_projects)


# ==========================================================
# Candidate Summary
# ==========================================================

def candidate_summary(text):

    return {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "Experience": extract_experience(text),

        "Education": extract_education(text),

        "Certifications": extract_certifications(text),

        "Projects": extract_projects(text)

    }

def parse_resume(uploaded_file):
    return extract_resume_text(uploaded_file)