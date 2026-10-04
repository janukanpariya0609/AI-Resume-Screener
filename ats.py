# ==========================================================
# AI Resume Screening System
# ATS Score Calculator
# ==========================================================


# ==========================================================
# Skill Score
# ==========================================================

def calculate_skill_score(match_percentage):

    return round(
        match_percentage,
        2
    )



# ==========================================================
# Experience Score
# ==========================================================

def calculate_experience_score(years):

    if years is None:
        return 0

    if isinstance(years, str):
        cleaned = years.lower().replace("year", "").replace("years", "").replace("yr", "").replace("yrs", "").replace("+", "").strip()
        if not cleaned:
            return 0
        try:
            years = float(cleaned)
        except ValueError:
            return 0

    try:
        years = float(years)
    except (TypeError, ValueError):
        return 0

    if years <= 0:
        return 0

    elif years < 1:
        return 20

    elif years < 3:
        return 60

    elif years < 5:
        return 80

    else:
        return 100

# ==========================================================
# Education Score
# ==========================================================

def calculate_education_score(education):

    score = 0


    if not education:

        return 20



    for degree in education:


        degree = degree.lower()



        if "phd" in degree:

            score = max(score,100)


        elif "m.tech" in degree or "mba" in degree:

            score = max(score,90)


        elif "b.tech" in degree or "b.e" in degree:

            score = max(score,80)


        elif "bca" in degree or "b.sc" in degree:

            score = max(score,70)


        elif "diploma" in degree:

            score = max(score,60)



    return score



# ==========================================================
# Certification Score
# ==========================================================

def calculate_certification_score(certifications):


    if not certifications:

        return 20


    count = len(certifications)


    if count >= 3:

        return 100


    elif count == 2:

        return 80


    elif count == 1:

        return 60


    else:

        return 20




# ==========================================================
# Project Score
# ==========================================================

def calculate_project_score(projects):

    if isinstance(projects, list):
        count = len(projects)
    elif isinstance(projects, (int, float)):
        count = int(projects)
    else:
        try:
            count = int(projects)
        except (TypeError, ValueError):
            count = 0

    if count >= 5:

        return 100


    elif count >= 3:

        return 80


    elif count >= 1:

        return 60


    else:

        return 20




# ==========================================================
# Final ATS Score
# ==========================================================

def calculate_ats_score(

        skill_score,

        experience_score,

        education_score,

        certification_score,

        project_score

):


    final_score = (

        skill_score * 0.45 +

        experience_score * 0.20 +

        education_score * 0.15 +

        certification_score * 0.10 +

        project_score * 0.10

    )


    return round(
        final_score,
        2
    )




# ==========================================================
# ATS Report Generator
# ==========================================================

def generate_ats_report(candidate_data):


    skill_score = calculate_skill_score(
        candidate_data["skill_match"]
    )

    experience_score = calculate_experience_score(
        candidate_data["experience"]
    )


    education_score = calculate_education_score(
            candidate_data["education"]
        )


    certification_score = calculate_certification_score(
        candidate_data["certifications"]
    )


    project_score = calculate_project_score(
        candidate_data["projects"]
    )


    final_score = calculate_ats_score(

        skill_score,

        experience_score,

        education_score,

        certification_score,

        project_score

    )



    return {


        "Skill Score":

            skill_score,


        "Experience Score":

            experience_score,


        "Education Score":

            education_score,


        "Certification Score":

            certification_score,


        "Project Score":

            project_score,


        "ATS Score":

            final_score

    }