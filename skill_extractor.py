# ==========================================================
# AI Resume Screening System
# Skill Extractor
# ==========================================================

import re
from skills_database import SKILLS_DATABASE


# ==========================================================
# Normalize Text
# ==========================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9+#.\s]",
        " ",
        text
    )

    return text



# ==========================================================
# Extract Skills From Resume
# ==========================================================

def extract_skills(text):

    text_clean = clean_text(text)

    detected_skills = []


    for skill in SKILLS_DATABASE:

        skill_lower = skill.lower()

        # exact matching
        if skill_lower in text_clean:

            detected_skills.append(skill)



    return list(set(detected_skills))



# ==========================================================
# Skill Match With Job Requirement
# ==========================================================

def skill_match(candidate_skills, required_skills):

    candidate = set(
        [skill.lower() for skill in candidate_skills]
    )

    required = set(
        [skill.lower() for skill in required_skills]
    )


    matched = candidate.intersection(required)

    missing = required.difference(candidate)


    if len(required) > 0:

        percentage = (
            len(matched)
            /
            len(required)
        ) * 100

    else:

        percentage = 0



    return {

        "matched_skills": list(matched),

        "missing_skills": list(missing),

        "match_percentage": round(
            percentage,
            2
        )

    }



# ==========================================================
# Skill Category
# ==========================================================

def categorize_skills(skills):

    categories = {


        "Programming": [
            "Python",
            "Java",
            "C",
            "C++",
            "JavaScript"
        ],


        "Data Science": [
            "Machine Learning",
            "Deep Learning",
            "Pandas",
            "NumPy",
            "TensorFlow"
        ],


        "Database": [
            "SQL",
            "MySQL",
            "MongoDB"
        ],


        "Cloud": [
            "AWS",
            "Azure",
            "Google Cloud"
        ],


        "Web Development": [
            "HTML",
            "CSS",
            "React",
            "Django",
            "Flask"
        ]


    }



    result = {}



    for category, items in categories.items():

        found = []

        for skill in skills:

            if skill in items:

                found.append(skill)



        if found:

            result[category] = found



    return result