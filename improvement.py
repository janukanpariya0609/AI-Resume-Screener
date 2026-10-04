def improvement_suggestions(resume_text):

    suggestions = []

    text = resume_text.lower()

    if "project" not in text:
        suggestions.append(
            "Add project details to showcase practical skills."
        )

    if "experience" not in text and "internship" not in text:
        suggestions.append(
            "Add internship or work experience details."
        )

    if "skill" not in text:
        suggestions.append(
            "Add a dedicated technical skills section."
        )

    if len(resume_text.split()) < 200:
        suggestions.append(
            "Resume content is short. Add more details about achievements."
        )

    if len(suggestions) == 0:
        suggestions.append(
            "Resume looks good. Keep improving with measurable achievements."
        )

    return suggestions