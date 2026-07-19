import streamlit as st
import pandas as pd

from utils.dashboard_queries import get_full_dataset


# ==========================================================
# ANALYTICS PAGE
# ==========================================================

def analytics_page():

    st.markdown(
        """
        <h1 style="color:#2563EB;margin-bottom:0px;">
            📊 Hospital Analytics
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="color:#6B7280;font-size:17px;">
            Explore detailed insights and statistical analysis of hospital records.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ======================================================
    # LOAD DATA
    # ======================================================

    df = get_full_dataset()

    # ======================================================
    # NUMERICAL ANALYSIS
    # ======================================================

    st.subheader("📈 Numerical Statistics")

    numeric_df = df.select_dtypes(include="number")

    st.dataframe(
        numeric_df.describe().round(2),
        use_container_width=True,
    )

    st.divider()

    # ======================================================
    # TOP HOSPITALS
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🏥 Top 10 Hospitals")

        hospital_df = (
            df["Hospital"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        hospital_df.columns = [
            "Hospital",
            "Patients",
        ]

        st.dataframe(
            hospital_df,
            use_container_width=True,
            hide_index=True,
        )

    # ======================================================
    # TOP DOCTORS
    # ======================================================

    with col2:

        st.subheader("👨‍⚕️ Top 10 Doctors")

        doctor_df = (
            df["Doctor"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        doctor_df.columns = [
            "Doctor",
            "Patients",
        ]

        st.dataframe(
            doctor_df,
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    # ======================================================
    # MEDICAL CONDITIONS
    # ======================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🩺 Medical Conditions")

        condition_df = (
            df["Medical Condition"]
            .value_counts()
            .reset_index()
        )

        condition_df.columns = [
            "Condition",
            "Patients",
        ]

        st.dataframe(
            condition_df,
            use_container_width=True,
            hide_index=True,
        )

    # ======================================================
    # ADMISSION TYPES
    # ======================================================

    with col2:

        st.subheader("🚑 Admission Types")

        admission_df = (
            df["Admission Type"]
            .value_counts()
            .reset_index()
        )

        admission_df.columns = [
            "Admission Type",
            "Patients",
        ]

        st.dataframe(
            admission_df,
            use_container_width=True,
            hide_index=True,
        )

    st.divider()

    # ======================================================
    # CORRELATION
    # ======================================================

    st.subheader("📌 Correlation Matrix")

    if len(numeric_df.columns) > 1:

        corr = numeric_df.corr().round(2)

        st.dataframe(
            corr,
            use_container_width=True,
        )

    else:

        st.info("Not enough numerical columns available.")

    st.divider()

    # ======================================================
    # DATA QUALITY
    # ======================================================

    st.subheader("✅ Data Quality Report")

    quality = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Values": df.isnull().sum().values,
            "Data Type": df.dtypes.astype(str).values,
        }
    )

    st.dataframe(
        quality,
        use_container_width=True,
        hide_index=True,
    )