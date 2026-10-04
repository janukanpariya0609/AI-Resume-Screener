# ==========================================================
# AI Resume Screening System
# Candidate Recommendation Engine
# ==========================================================


# ==========================================================
# Hiring Decision
# ==========================================================

def hiring_decision(ats_score):


    if ats_score >= 85:

        return "Strong Candidate - Recommended for Interview"


    elif ats_score >= 70:

        return "Good Candidate - HR Review Required"


    elif ats_score >= 50:

        return "Average Candidate - Consider After Improvement"


    else:

        return "Not Recommended"





# ==========================================================
# HR Explanation
# ==========================================================

def generate_hr_feedback(

        ats_score,

        matched_skills,

        missing_skills,

        experience

):


    feedback = []



    if ats_score >= 85:

        feedback.append(
            "Candidate has strong alignment with job requirements."
        )


    elif ats_score >= 70:

        feedback.append(
            "Candidate matches most requirements but needs manual review."
        )


    else:

        feedback.append(
            "Candidate does not currently satisfy important requirements."
        )




    if experience >= 3:

        feedback.append(
            "Candidate has relevant professional experience."
        )

    else:

        feedback.append(
            "Candidate has limited experience."
        )




    if matched_skills:

        feedback.append(
            f"Strong skills detected: {', '.join(matched_skills)}"
        )



    if missing_skills:

        feedback.append(
            f"Missing skills: {', '.join(missing_skills)}"
        )



    return feedback





# ==========================================================
# Student Improvement Suggestions
# ==========================================================

def student_recommendations(

        missing_skills,

        ats_score

):


    suggestions = []



    if ats_score < 70:

        suggestions.append(
            "Improve your technical skill set to increase ATS ranking."
        )



    if missing_skills:


        for skill in missing_skills:


            suggestions.append(
                f"Learn {skill} to improve your job matching score."
            )



    else:

        suggestions.append(
            "Your skill profile matches the target role well."
        )




    suggestions.append(
        "Add more practical projects with GitHub links."
    )


    suggestions.append(
        "Include measurable achievements in your resume."
    )


    suggestions.append(
        "Keep certifications updated."
    )

    suggestions.append(
        "Learn more new technical skills."
    )



    return suggestions





# ==========================================================
# Complete Recommendation Report
# ==========================================================

def recommendation_report(

        ats_score,

        matched_skills,

        missing_skills,

        experience

):


    return {


        "Decision":

        hiring_decision(
            ats_score
        ),



        "HR Feedback":

        generate_hr_feedback(

            ats_score,

            matched_skills,

            missing_skills,

            experience

        ),



        "Student Suggestions":

        student_recommendations(

            missing_skills,

            ats_score

        )

    }