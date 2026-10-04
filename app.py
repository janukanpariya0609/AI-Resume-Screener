# AI-Powered Resume Screening System
# Main Streamlit Application

import streamlit as st
import pandas as pd

from styles import apply_styles

from utils import (
    save_resume,
    create_profile_summary,
    normalize_project_count
)

from resume_parser import (
    extract_resume_text,
    candidate_summary
)

from skill_extractor import (
    extract_skills,
    skill_match,
    categorize_skills
)

from ats import (
    generate_ats_report
)

from recommendation import (
    recommendation_report
)

from charts import (
    ats_gauge_chart,
    skill_match_chart,
    skill_category_chart,
    ats_component_chart
)

# Page Configuration
st.set_page_config(
    page_title="AI-Powered Resume Screening System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom Theme
st.markdown(
    apply_styles(),
    unsafe_allow_html=True
)

# Header
st.title("AI-Powered Resume Screening System")

st.markdown("""
<div style="background: #ffffff; border: 1px solid #ffffff; border-radius: 12px;
padding: 16px 18px; margin: 8px 0 16px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05); width: 100%; box-sizing: border-box;">

<h3 style="color: #9d174d; margin-top: 0; margin-bottom: 8px;">Smart ATS Platform for HR Recruitment</h3>

<p style="color: #831843; margin-bottom: 0; line-height: 1.5;">
Upload any candidate resume and automatically analyze
skills, ATS score, experience, projects and hiring
recommendation.
</p>

</div>
""", unsafe_allow_html=True)

# Resume Upload
uploaded_file = st.file_uploader(
    "Upload Candidate Resume",
    type=["pdf", "docx", "txt"]
)

# Job Requirement Skills
st.subheader("Job Requirement Skills")

job_skills_input = st.text_input(
    "Required Skills (comma separated)",
    placeholder="Python, SQL, Machine Learning, AWS"
)

# Start Resume Analysis
if uploaded_file:

    # Save Resume
    file_path = save_resume(uploaded_file)

    # Extract Resume Text
    with st.spinner("Analyzing Resume..."):

        resume_text = extract_resume_text(uploaded_file)

    if resume_text == "":

        st.error("Unable to read the uploaded resume.")

        st.stop()

   
    # Candidate Summary
    candidate = candidate_summary(resume_text)

    # Skill Extraction
    detected_skills = extract_skills(resume_text)

    # Required Skills
    if job_skills_input.strip():

        required_skills = [

            skill.strip()

            for skill in job_skills_input.split(",")

            if skill.strip()

        ]

    else:

        required_skills = detected_skills

    # Skill Matching
    skill_analysis = skill_match(

        detected_skills,

        required_skills

    )

    # ATS Score
    project_value = candidate.get("Projects", [])
    project_count = normalize_project_count(project_value)

    ats_input = {

        "skill_match": skill_analysis["match_percentage"],

        "experience": candidate.get("Experience", 0),

        "education": candidate.get("Education", []),

        "certifications": candidate.get("Certifications", []),

        "projects": project_count

    }

    ats_result = generate_ats_report(ats_input)
    ats_score = ats_result["ATS Score"]

    # Recommendation
    recommendation = recommendation_report(

        ats_score,

        skill_analysis["matched_skills"],

        skill_analysis["missing_skills"],

        candidate.get("Experience", 0)

    )

    # Sidebar Navigation
    page = st.sidebar.radio(

        "Candidate Analysis",

        [

            "Resume Parsing",

            "Skill Extraction",

            "ATS Scoring",

            "Candidate Ranking",

            "Improvement Suggestions",

            "Visualization"

        ]

    )

    st.divider()

    # Resume Parsing Page
    if page == "Resume Parsing":

        st.header("📄 Resume Parsing")

        profile = create_profile_summary(candidate)

        st.markdown("### Candidate Profile")

        for key, value in profile.items():
            if key == "Projects":
                st.markdown(f"- **{key}:** {value}")
            else:
                st.markdown(f"- **{key}:** {value}")

        st.write("")

    # Skill Extraction Page
    elif page == "Skill Extraction":

        st.header("🛠 Skill Extraction")

        col1, col2 = st.columns([2, 1])

        with col1:

            if detected_skills:

                skill_df = pd.DataFrame(
                    {"Detected Skills": detected_skills}
                )

                st.dataframe(
                    skill_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.warning("No skills detected.")

        with col2:

            st.metric("Total Skills",len(detected_skills))

            st.metric("Matched Skills",len(skill_analysis["matched_skills"]))

            st.metric("Missing Skills",len(skill_analysis["missing_skills"]))
                                           
                                           
        st.subheader("Matched Skills")

        if skill_analysis["matched_skills"]:

            st.success(", ".join(skill_analysis["matched_skills"]))

        else:

            st.info("No matched skills.")

        st.subheader("Missing Skills")

        if skill_analysis["missing_skills"]:

            st.error(", ".join(skill_analysis["missing_skills"]))

        else:

            st.success("No missing skills.")

    
    # ATS Scoring Page
    elif page == "ATS Scoring":

        st.header("📊 ATS Score Analysis")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("ATS Score",f"{ats_score}%")

        col2.metric("Skill Match",f"{skill_analysis['match_percentage']}%")

        col3.metric("Matched Skills",len(skill_analysis["matched_skills"]))

        col4.metric("Missing Skills",len(skill_analysis["missing_skills"]))
        st.divider()

        st.subheader("ATS Components")

        ats_df = pd.DataFrame(

            [
                ["Skill Score", ats_result.get("Skill Score", 0)],
                ["Experience Score", ats_result.get("Experience Score", 0)],
                ["Education Score", ats_result.get("Education Score", 0)],
                ["Certification Score", ats_result.get("Certification Score", 0)],
                ["Project Score", ats_result.get("Project Score", 0)],
                ["ATS Score", ats_result.get("ATS Score", 0)]
            ],

            columns=[

                "Component",

                "Score"

            ]

        )

        ats_df["Score"] = ats_df["Score"].apply(
            lambda x: str(x)

        )
        st.dataframe(ats_df,use_container_width=True,hide_index=True)


    # Candidate Ranking Page
    elif page == "Candidate Ranking":
        st.header("🏆 Candidate Ranking")

        if ats_score >= 85:
            ranking = "Excellent Candidate"
            status = "Strongly Recommended"

        elif ats_score >= 70:
            ranking = "Good Candidate"
            status = "Recommended"

        else:
            ranking = "Needs Improvement"
            status = "Not Recommended"

        st.success(ranking)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("ATS Score",f"{ats_score}%")

        with col2:
            st.metric("Hiring Status",status)

        st.subheader("HR Hiring Recommendation")
        st.info(recommendation["Decision"])
        st.subheader("HR Feedback")

        for feedback in recommendation["HR Feedback"]:
            st.write("• " + feedback)

    # Improvement Suggestions Page
    elif page == "Improvement Suggestions":
        st.header("💡 Candidate Improvement Suggestions")

        st.subheader("Suggestions")

        for suggestion in recommendation["Student Suggestions"]:
            st.info(suggestion)


        st.subheader("Skills To Improve")

        missing = skill_analysis["missing_skills"]

        if missing:
            st.warning(", ".join(missing))

        else:
            st.success("Candidate has all required skills.")   

    # Visualization Page
    elif page == "Visualization":
        st.header("📈 Resume Analysis Visualization") 
        # ATS Gauge Chart
        st.subheader("ATS Score")
        st.plotly_chart(ats_gauge_chart(ats_score),use_container_width=True)
        st.divider()        
        # Skill Match Chart
        st.subheader("Skill Match Analysis")
        st.plotly_chart(skill_match_chart(skill_analysis["matched_skills"],skill_analysis["missing_skills"]),use_container_width=True)
        st.divider()

        # Skill Category Chart
        st.subheader("Skill Category Distribution")
        categories = categorize_skills(detected_skills)
        st.plotly_chart(skill_category_chart(categories),use_container_width=True)
        st.divider()

        # ATS Component Chart
        st.subheader("ATS Component Analysis")
        st.plotly_chart(ats_component_chart(ats_result),use_container_width=True)

# No Resume Uploaded
else:
    st.markdown(
        """
        <div style="background:#9d174d; color:#f5f3ff; padding:16px 18px;
        border-radius:12px; border:1px solid #f9a8d4; font-size:15px;">
            📄 Please upload a resume to start analysis.
        </div>
        """,unsafe_allow_html=True
    )