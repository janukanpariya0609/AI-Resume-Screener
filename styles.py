# ==========================================================
# AI Resume Screening System
# Streamlit UI Styling
# Clear Purple Professional Theme
# ==========================================================

import streamlit as st

def apply_styles():

    return """

    <style>

    /* ============================= */
    /* MAIN APP BACKGROUND */
    /* ============================= */

    .stApp {

        background: linear-gradient(
            135deg,
            #fdf2f8,
            #fce7f3,
            #fbcfe8
        );

        color: #4a102a;

    }


    /* ============================= */
    /* MAIN TITLE */
    /* ============================= */

    h1 {

        color: #be185d !important;

        text-align: center;

        font-size: 45px;

        font-weight: 800;

    }


    h2, h3 {

        color: #9d174d !important;

    }


    /* ============================= */
    /* CUSTOM CARDS */
    /* ============================= */

    .card {

        background: #ffffff;

        padding: 25px;

        border-radius: 20px;

        box-shadow:
            0px 5px 20px
            rgba(190, 24, 93, 0.15);

        margin: 15px;

    }


    /* ============================= */
    /* SIDEBAR */
    /* ============================= */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #9d174d,
            #db2777
        );

    }


    section[data-testid="stSidebar"] * {

        color: white !important;

        font-size: 17px;

    }


    /* Sidebar Heading */

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {

        color: white !important;

    }


    /* ============================= */
    /* METRICS */
    /* ============================= */

    div[data-testid="metric-container"] {

        background: #ffffff;

        padding: 20px;

        border-radius: 15px;

        border: 1px solid #f9a8d4;

        box-shadow:
            0px 4px 15px
            rgba(190, 24, 93, 0.15);

    }


    div[data-testid="metric-container"] label {

        color: #be185d !important;

        font-weight: bold;

    }


    div[data-testid="metric-container"] div {

        color: #831843 !important;

        font-size: 28px;

        font-weight: bold;

    }


    /* ============================= */
    /* UPLOAD BOX */
    /* ============================= */

    section[data-testid="stFileUploader"] {

        background: #ffffff;

        padding: 20px;

        border-radius: 20px;

        border: 1px solid #f9a8d4;

        box-shadow:
            0px 4px 15px
            rgba(190, 24, 93, 0.15);

    }


    /* ============================= */
    /* BUTTONS */
    /* ============================= */

    .stButton button {

        background: linear-gradient(
            90deg,
            #db2777,
            #be185d
        );

        color: white;

        border: none;

        border-radius: 30px;

        padding: 12px 30px;

        font-weight: bold;

    }


    .stButton button:hover {

        background: #9d174d;

        color: white;

    }


    /* ============================= */
    /* TEXT VISIBILITY */
    /* ============================= */

    p, li {

        color: #4a102a !important;

        font-size: 16px;

    }


    /* ============================= */
    /* SUCCESS */
    /* ============================= */

    .stSuccess {

        background: #fce7f3;

        color: #9d174d;

        border-radius: 15px;

        border: 1px solid #f9a8d4;

    }


    /* ============================= */
    /* WARNING */
    /* ============================= */

    .stWarning {

        background: #fdf2f8;

        color: #9d174d;

        border-radius: 15px;

        border: 1px solid #f9a8d4;

    }


    /* ============================= */
    /* INFO */
    /* ============================= */

    .stInfo {

        background: #fce7f3;

        color: #9d174d;

        border-radius: 15px;

        border: 1px solid #f9a8d4;

    }


    /* ============================= */
    /* FILE UPLOADER TEXT */
    /* ============================= */

    [data-testid="stFileUploaderDropzone"] span {

        color: #831843 !important;

    }


    [data-testid="stFileUploaderDropzone"] button div p {

        color: #831843 !important;

    }


    [data-testid="stFileUploaderDropzone"] svg {

        color: #db2777 !important;

        fill: #db2777 !important;

    }


    /* ============================= */
    /* TEXT INPUT */
    /* ============================= */

    input {

        border: 1px solid #f9a8d4 !important;

    }


    input:focus {

        border: 2px solid #db2777 !important;

        box-shadow: 0 0 5px #f9a8d4 !important;

    }


    /* ============================= */
    /* DATAFRAME / TABLE */
    /* ============================= */

    [data-testid="stDataFrame"] {

        border: 1px solid #f9a8d4;

        border-radius: 12px;

    }


    /* ============================= */
    /* DIVIDER */
    /* ============================= */

    hr {

        border-color: #f9a8d4 !important;

    }


    </style>

    """
