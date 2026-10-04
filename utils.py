# ==========================================================
# AI Resume Screening System
# Utility Functions
# ==========================================================

import os
import re
import uuid
from datetime import datetime



# ==========================================================
# Create Required Folders
# ==========================================================

def create_directories():

    folders = [

        "uploaded_resumes",

        "assets"

    ]


    for folder in folders:

        if not os.path.exists(folder):

            os.makedirs(folder)





# ==========================================================
# Save Uploaded Resume
# ==========================================================

def save_resume(uploaded_file):


    create_directories()


    file_extension = uploaded_file.name.split(".")[-1]


    unique_name = (

        str(uuid.uuid4())

        +

        "_"

        +

        datetime.now()
        .strftime("%Y%m%d%H%M%S")

        +

        "."

        +

        file_extension

    )



    file_path = os.path.join(

        "uploaded_resumes",

        unique_name

    )



    with open(

        file_path,

        "wb"

    ) as f:


        f.write(

            uploaded_file.getbuffer()

        )



    return file_path





# ==========================================================
# Clean Text
# ==========================================================

def clean_text(text):


    text = text.replace(

        "\n",

        " "

    )


    text = re.sub(

        r"\s+",

        " ",

        text

    )


    return text.strip()





# ==========================================================
# Convert List To Text
# ==========================================================

def list_to_string(data):


    if not data:

        return "None"



    return ", ".join(data)


def normalize_project_count(projects):

    if projects is None:
        return 0

    if isinstance(projects, (int, float)):
        return int(projects)

    if isinstance(projects, list):
        return len(projects)

    if isinstance(projects, str):
        text = projects.strip()
        if not text:
            return 0

        digits = re.findall(r"\d+", text)
        if digits:
            return int(digits[0])

        return 0

    return 0


def _format_project_value(projects):

    return str(normalize_project_count(projects))





# ==========================================================
# Percentage Formatter
# ==========================================================

def format_percentage(value):


    return f"{value:.2f}%"





# ==========================================================
# Candidate Profile Summary
# ==========================================================

def create_profile_summary(candidate):


    summary = {


        "Candidate Name":

        candidate.get(
            "Name",
            "Not Available"
        ),



        "Email":

        candidate.get(
            "Email",
            "Not Available"
        ),



        "Phone":

        candidate.get(
            "Phone",
            "Not Available"
        ),



        "Experience":

        str(
            candidate.get(
                "Experience",
                0
            )
        )

        +

        " Years",



        "Education":

        list_to_string(

            candidate.get(

                "Education",

                []

            )

        ),



        "Certifications":

        list_to_string(

            candidate.get(

                "Certifications",

                []

            )

        ),

        "Projects":

        _format_project_value(

            candidate.get(

                "Projects",

                candidate.get(

                    "projects",

                    []

                )

            )

        )

    }



    return summary