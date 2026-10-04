# ==========================================================
# AI Resume Screening System
# Visualization Module
# ==========================================================

import plotly.graph_objects as go
import plotly.express as px



# ==========================================================
# ATS Score Gauge Chart
# ==========================================================

def ats_gauge_chart(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text": "ATS Score"
            },

            gauge={

                "axis": {

                    "range": [
                        0,
                        100
                    ]

                },

                "steps": [

                    {
                        "range": [
                            0,
                            50
                        ],

                        "color": "#ffcccc"
                    },

                    {
                        "range": [
                            50,
                            75
                        ],

                        "color": "#fff2cc"
                    },

                    {
                        "range": [
                            75,
                            100
                        ],

                        "color": "#ccffcc"
                    }

                ]

            }

        )

    )


    fig.update_layout(

        height=350

    )


    return fig




# ==========================================================
# Skill Match Pie Chart
# ==========================================================

def skill_match_chart(

        matched,

        missing

):


    labels = [

        "Matched Skills",

        "Missing Skills"

    ]


    values = [

        len(matched),

        len(missing)

    ]


    fig = px.pie(

        names=labels,

        values=values,

        title="Skill Match Analysis"

    )


    return fig




# ==========================================================
# Skill Category Bar Chart
# ==========================================================

def skill_category_chart(categories):


    category_names = list(
        categories.keys()
    )


    counts = [

        len(value)

        for value in categories.values()

    ]



    fig = px.bar(

        x=category_names,

        y=counts,

        labels={

            "x":"Skill Category",

            "y":"Number of Skills"

        },

        title="Skills Distribution"

    )


    return fig




# ==========================================================
# ATS Component Score Chart
# ==========================================================

def ats_component_chart(scores):


    components = [

        key

        for key in scores.keys()

        if key != "ATS Score"

    ]


    values = [

        scores[key]

        for key in components

    ]



    fig = px.bar(

        x=components,

        y=values,

        title="ATS Score Breakdown",

        labels={

            "x":"Evaluation Factor",

            "y":"Score"

        }

    )


    fig.update_layout(

        xaxis_tickangle=-45

    )


    return fig