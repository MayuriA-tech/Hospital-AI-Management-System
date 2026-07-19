import streamlit as st


def policies_page():

    st.title("📜 Hospital Policies")

    st.markdown(
        """
        Welcome to the **Hospital AI Management System Policy Center**.

        Please read the following policies carefully before using the application.
        """
    )

    st.divider()

    # ---------------------------------------------------------
    # Patient Privacy
    # ---------------------------------------------------------

    with st.expander("🔒 Patient Privacy Policy", expanded=True):

        st.markdown("""
- Patient information is confidential.
- Only authorized users can access medical records.
- Personal information is never shared with unauthorized individuals.
- Patient data is protected using secure database storage.
        """)

    # ---------------------------------------------------------
    # Data Security
    # ---------------------------------------------------------

    with st.expander("🛡 Data Security Policy"):

        st.markdown("""
- All patient records are stored securely.
- Database access is restricted.
- AI responses never expose confidential information.
- Regular backups are recommended.
        """)

    # ---------------------------------------------------------
    # AI Disclaimer
    # ---------------------------------------------------------

    with st.expander("🤖 AI Usage Disclaimer"):

        st.markdown("""
The AI Assistant is designed to assist healthcare professionals.

- AI-generated responses are informational.
- AI should not replace licensed medical professionals.
- Doctors should verify important recommendations before clinical use.
        """)

    # ---------------------------------------------------------
    # Medical Disclaimer
    # ---------------------------------------------------------

    with st.expander("🏥 Medical Disclaimer"):

        st.markdown("""
- This application is intended for educational and hospital management purposes.
- Medical decisions should always be made by qualified healthcare professionals.
- The developers are not responsible for misuse of the application.
        """)

    # ---------------------------------------------------------
    # Emergency Policy
    # ---------------------------------------------------------

    with st.expander("🚑 Emergency Guidelines"):

        st.markdown("""
In case of medical emergencies:

- Contact the nearest emergency department.
- Call local emergency services immediately.
- Do not rely solely on AI-generated responses.
        """)

    # ---------------------------------------------------------
    # User Responsibilities
    # ---------------------------------------------------------

    with st.expander("👨‍⚕ User Responsibilities"):

        st.markdown("""
Users must:

- Keep login credentials secure.
- Maintain patient confidentiality.
- Use the application ethically.
- Follow hospital regulations.
- Report any incorrect AI responses.
        """)

    st.divider()

    agree = st.checkbox(
        "I have read and understood all hospital policies."
    )

    if agree:

        st.success(
            "✅ Thank you for accepting the Hospital Policies."
        )