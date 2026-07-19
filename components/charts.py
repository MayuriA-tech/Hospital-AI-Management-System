import plotly.express as px
import streamlit as st


# ==========================================================
# Common Chart Layout
# ==========================================================

def _style_chart(fig, title):

    fig.update_layout(

        title={
            "text": title,
            "x": 0.5,
            "font": {
                "size": 22,
                "color": "#1E3A8A"
            }
        },

        template="plotly_white",

        height=420,

        paper_bgcolor="white",

        plot_bgcolor="white",

        font=dict(
            family="Segoe UI",
            size=14,
            color="#111827"
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False,
        linecolor="#D1D5DB"

    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False,
        linecolor="#D1D5DB"

    )

    return fig


# ==========================================================
# Gender Distribution
# ==========================================================

def gender_chart(df):

    gender = (
        df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = [
        "Gender",
        "Patients"
    ]

    fig = px.pie(

        gender,

        names="Gender",

        values="Patients",

        hole=.55,

        color_discrete_sequence=[
            "#2563EB",
            "#10B981",
            "#F59E0B",
            "#EF4444"
        ]
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    _style_chart(
        fig,
        "Gender Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# Medical Conditions
# ==========================================================

def condition_chart(df):

    condition = (
        df["Medical Condition"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    condition.columns = [
        "Condition",
        "Patients"
    ]

    fig = px.bar(

        condition,

        x="Condition",

        y="Patients",

        text="Patients",

        color="Patients",

        color_continuous_scale="Blues"

    )

    fig.update_traces(
        textposition="outside"
    )

    _style_chart(
        fig,
        "Top Medical Conditions"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# Admission Types
# ==========================================================

def admission_chart(df):

    admission = (
        df["Admission Type"]
        .value_counts()
        .reset_index()
    )

    admission.columns = [
        "Admission",
        "Patients"
    ]

    fig = px.bar(

        admission,

        x="Admission",

        y="Patients",

        text="Patients",

        color="Admission",

        color_discrete_sequence=px.colors.qualitative.Set2

    )

    fig.update_traces(
        textposition="outside"
    )

    _style_chart(
        fig,
        "Admission Types"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# Billing Distribution
# ==========================================================

def billing_chart(df):

    fig = px.histogram(

        df,

        x="Billing Amount",

        nbins=35,

        color_discrete_sequence=["#2563EB"]

    )

    _style_chart(
        fig,
        "Billing Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# Top Hospitals
# ==========================================================

def hospital_chart(df):

    hospital = (
        df["Hospital"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    hospital.columns = [
        "Hospital",
        "Patients"
    ]

    fig = px.bar(

        hospital,

        x="Patients",

        y="Hospital",

        orientation="h",

        text="Patients",

        color="Patients",

        color_continuous_scale="Teal"

    )

    _style_chart(
        fig,
        "Top Hospitals"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# Top Doctors
# ==========================================================

def doctor_chart(df):

    doctor = (
        df["Doctor"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    doctor.columns = [
        "Doctor",
        "Patients"
    ]

    fig = px.bar(

        doctor,

        x="Doctor",

        y="Patients",

        text="Patients",

        color="Patients",

        color_continuous_scale="Mint"

    )

    fig.update_traces(
        textposition="outside"
    )

    _style_chart(
        fig,
        "Top Doctors"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )