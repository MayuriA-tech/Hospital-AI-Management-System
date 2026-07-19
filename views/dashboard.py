import streamlit as st
from datetime import datetime

from components.cards import metric_card, section_title

from utils.dashboard_queries import (
    get_dashboard_data,
    get_full_dataset,
    get_recent_patients,
)

from components.charts import (
    gender_chart,
    condition_chart,
    billing_chart,
    admission_chart,
)

# ==========================================================
# Dashboard
# ==========================================================

def dashboard_page():

    # ------------------------------------------------------
    # Load Data
    # ------------------------------------------------------

    stats = get_dashboard_data()

    df = get_full_dataset()

    recent_df = get_recent_patients()

    # ------------------------------------------------------
    # Header
    # ------------------------------------------------------

    username = st.session_state.get("username", "User")

    today = datetime.now().strftime("%d %B %Y")

    left, right = st.columns([4, 1])

    with left:

        st.markdown(
            """
            <h1 style='color:#2563EB;margin-bottom:0px;'>
            🏥 Hospital AI Management System
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <h4 style="color:#64748B;margin-top:0px;">
            Welcome back, <span style="color:#2563EB;">{username}</span> 👋
            </h4>
            """,
            unsafe_allow_html=True,
        )

    with right:

        st.info(f"📅 {today}")

    st.divider()

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(
            "Patients",
            f"{stats['patients']:,}",
            "👨",
            "#2563EB",
        )

    with c2:

        metric_card(
            "Hospitals",
            f"{stats['hospitals']:,}",
            "🏥",
            "#10B981",
        )

    with c3:

        metric_card(
            "Doctors",
            f"{stats['doctors']:,}",
            "👨‍⚕️",
            "#F59E0B",
        )

    with c4:

        metric_card(
            "Avg Billing",
            f"${stats['billing']:,.0f}",
            "💰",
            "#EF4444",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DASHBOARD OVERVIEW
    # ------------------------------------------------------

    section_title("📊 Dashboard Overview")

    left_chart, right_chart = st.columns(2)

    with left_chart:

        st.markdown("#### Gender Distribution")

        gender_chart(df)

    with right_chart:

        st.markdown("#### Medical Conditions")

        condition_chart(df)

    st.markdown("<br>", unsafe_allow_html=True)

    left_chart, right_chart = st.columns(2)

    with left_chart:

        st.markdown("#### Admission Type")

        admission_chart(df)

    with right_chart:

        st.markdown("#### Billing Analysis")

        billing_chart(df)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # QUICK INSIGHTS
    # ------------------------------------------------------

    section_title("📈 Quick Insights")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="👨 Total Patients",
            value=f"{stats['patients']:,}"
    )

    with col2:
        st.metric(
            label="💰 Average Billing",
            value=f"${stats['billing']:,.0f}"
    )

    with col3:
        st.metric(
            label="🏥 Hospitals Covered",
            value=f"{stats['hospitals']:,}"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # RECENT PATIENTS
    # ------------------------------------------------------

    section_title("🧾 Recently Admitted Patients")

    st.dataframe(
        recent_df,
        use_container_width=True,
        hide_index=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DATASET SUMMARY
    # ------------------------------------------------------

    section_title("📋 Dataset Summary")

    total_records = len(df)

    male_count = len(df[df["Gender"] == "Male"]) if "Gender" in df.columns else 0
    female_count = len(df[df["Gender"] == "Female"]) if "Gender" in df.columns else 0

    average_age = round(df["Age"].mean(), 1) if "Age" in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📁 Total Records",
            f"{total_records:,}"
    )

    with col2:
        st.metric(
            "👨 Male Patients",
            f"{male_count:,}"
    )

    with col3:
        st.metric(
            "👩 Female Patients",
            f"{female_count:,}"
    )

    with col4:
        st.metric(
            "🎂 Average Age",
            f"{average_age} Years"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DATA PREVIEW
    # ------------------------------------------------------

    section_title("🗂 Complete Dataset Preview")

    preview_columns = st.multiselect(
        "Select Columns",
        options=df.columns.tolist(),
        default=df.columns.tolist()[:6],
    )

    if preview_columns:
        st.dataframe(
            df[preview_columns],
            use_container_width=True,
            hide_index=True,
            height=350,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DOWNLOAD SECTION
    # ------------------------------------------------------

    section_title("⬇ Export Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Dataset (CSV)",
        data=csv,
        file_name="hospital_dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # HOSPITAL ANALYTICS
    # ------------------------------------------------------

    with st.expander("🏥 Hospital Statistics", expanded=False):

        if "Hospital" in df.columns:

            hospital_df = (
                df["Hospital"]
                .value_counts()
                .reset_index()
            )

            hospital_df.columns = [
                "Hospital",
                "Patients"
            ]

            st.dataframe(
                hospital_df,
                use_container_width=True,
                hide_index=True,
                height=300,
            )

    with st.expander("👨‍⚕️ Doctor Statistics", expanded=False):

        if "Doctor" in df.columns:

            doctor_df = (
                df["Doctor"]
                .value_counts()
                .reset_index()
            )

            doctor_df.columns = [
                "Doctor",
                "Patients"
            ]

            st.dataframe(
                doctor_df,
                use_container_width=True,
                hide_index=True,
                height=300,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # SYSTEM INFORMATION
    # ------------------------------------------------------

    section_title("ℹ System Information")

    info_left, info_right = st.columns(2)

    with info_left:

        st.info(
            """
**Database**

• SQLite Database

• Hospital Records

• AI Enabled

• Secure Storage
"""
        )

    with info_right:

        st.success(
            f"""
**Dashboard Status**

✅ Total Records : {len(df):,}

✅ AI Assistant Ready

✅ SQL Agent Connected

✅ Analytics Available
"""
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # FOOTER
    # ------------------------------------------------------

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;
                    color:#6B7280;
                    font-size:14px;
                    padding:10px;'>

        🏥 Hospital AI Management System <br>

        Developed using Streamlit • Groq • LangChain • SQLite

        </div>
        """,
        unsafe_allow_html=True,
    )