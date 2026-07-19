import streamlit as st
import pandas as pd

from utils.dashboard_queries import get_full_dataset


# ==========================================================
# PATIENT DATABASE
# ==========================================================

def patient_database_page():

    st.markdown(
        """
        <h1 style="color:#2563EB;margin-bottom:0px;">
            👨‍⚕️ Patient Database
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="color:#6B7280;font-size:17px;">
            Search, filter and explore hospital patient records.
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
    # SEARCH
    # ======================================================

    search = st.text_input(
        "🔍 Search Patient Name",
        placeholder="Enter patient name..."
    )

    # ======================================================
    # FILTERS
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["All"] + sorted(df["Gender"].dropna().unique().tolist())
        )

    with col2:

        admission = st.selectbox(
            "Admission Type",
            ["All"] + sorted(df["Admission Type"].dropna().unique().tolist())
        )

    with col3:

        blood = st.selectbox(
            "Blood Group",
            ["All"] + sorted(df["Blood Type"].dropna().unique().tolist())
        )

    # ======================================================
    # APPLY FILTERS
    # ======================================================

    filtered_df = df.copy()

    if search:

        filtered_df = filtered_df[
            filtered_df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if gender != "All":

        filtered_df = filtered_df[
            filtered_df["Gender"] == gender
        ]

    if admission != "All":

        filtered_df = filtered_df[
            filtered_df["Admission Type"] == admission
        ]

    if blood != "All":

        filtered_df = filtered_df[
            filtered_df["Blood Type"] == blood
        ]

    # ======================================================
    # RECORD COUNT
    # ======================================================

    st.success(
        f"📋 Showing {len(filtered_df):,} Patient Records"
    )

    # ======================================================
    # TABLE
    # ======================================================

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        height=500,
    )

    # ======================================================
    # DOWNLOAD
    # ======================================================

    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Filtered Dataset",
        csv,
        "patient_database.csv",
        "text/csv",
        use_container_width=True,
    )