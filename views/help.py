import streamlit as st


def help_page():

    st.title("❓ Help Center")

    st.markdown("""
Welcome to the **Hospital AI Management System Help Center**.

Find answers to frequently asked questions and learn how to use the system effectively.
""")

    st.divider()

    search = st.text_input(
        "🔍 Search Help Topics",
        placeholder="Search here..."
    )

    st.divider()

    with st.expander("🤖 How do I use the AI Assistant?", expanded=True):

        st.markdown("""
1. Open the **AI Assistant** page.
2. Enter your medical or database-related question.
3. Click **Ask AI**.
4. The AI Assistant will generate a response using the available hospital data and documents.
""")

    with st.expander("👨‍⚕️ How do I search patient records?"):

        st.markdown("""
- Open the **Patient Database** page.
- Use the search bar to find a patient.
- Apply filters such as Gender, Blood Group or Admission Type.
- The filtered records can also be downloaded.
""")

    with st.expander("📄 How do I generate a Patient Report?"):

        st.markdown("""
- Go to **Patient Reports**.
- Select a patient.
- Click **Generate AI Medical Report**.
- Review the AI-generated summary.
- Download the report as a professional PDF.
""")

    with st.expander("📊 What information is available in Analytics?"):

        st.markdown("""
The Analytics page provides:

- Patient statistics
- Top hospitals
- Top doctors
- Medical condition analysis
- Admission statistics
- Correlation matrix
- Data quality report
""")

    with st.expander("🔒 Is patient data secure?"):

        st.markdown("""
Yes.

The application uses:

- SQLite Database
- Restricted database access
- AI-generated responses without exposing confidential information
- Secure hospital data management practices
""")

    with st.expander("⚠️ Why can't I access some features?"):

        st.markdown("""
Some pages or actions may depend on your assigned role.

Different users can have different permissions within the Hospital AI Management System.
""")

    st.divider()

    st.subheader("📘 Quick User Guide")

    st.markdown("""
1️⃣ Dashboard → View hospital overview.

2️⃣ Patient Database → Search patient records.

3️⃣ Analytics → Explore hospital statistics.

4️⃣ AI Assistant → Ask hospital-related questions.

5️⃣ Patient Reports → Generate AI-powered PDF reports.

6️⃣ Policies → Read hospital policies and guidelines.
""")

    st.divider()

    st.subheader("💡 Tips")

    st.info(
        """
• Use specific questions while chatting with the AI Assistant.

• Verify AI-generated medical summaries before clinical use.

• Download reports in PDF format for professional documentation.

• Keep patient information confidential.
        """
    )

    st.divider()

    st.subheader("📞 Need More Help?")

    col1, col2 = st.columns(2)

    with col1:

        st.success("📧 support@hospitalai.com")

    with col2:

        st.success("☎ +91-9876543210")

    st.caption(
        "Hospital AI Management System • Version 1.0"
    )