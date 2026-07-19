import streamlit as st
from datetime import datetime


def contact_page():

    st.title("📞 Contact Us")

    st.markdown("""
Need assistance or have feedback?

Our support team is here to help. Fill out the form below and we'll get back to you.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")

        email = st.text_input("📧 Email Address")

    with col2:

        department = st.selectbox(
            "🏢 Department",
            [
                "General Inquiry",
                "Technical Support",
                "Patient Records",
                "AI Assistant",
                "Analytics",
                "Feedback"
            ]
        )

        priority = st.selectbox(
            "⚡ Priority",
            [
                "Low",
                "Medium",
                "High",
                "Urgent"
            ]
        )

    subject = st.text_input("📝 Subject")

    message = st.text_area(
        "💬 Message",
        placeholder="Describe your issue or feedback here...",
        height=180
    )

    if st.button("📨 Submit Request", use_container_width=True):

        if not name or not email or not subject or not message:

            st.warning("Please fill in all required fields.")

        else:

            st.success("✅ Your request has been submitted successfully!")

            st.info(f"""
**Submission Details**

👤 Name: {name}

📧 Email: {email}

🏢 Department: {department}

⚡ Priority: {priority}

🕒 Submitted On: {datetime.now().strftime("%d-%m-%Y %I:%M %p")}
""")

    st.divider()

    st.subheader("🏥 Hospital Contact Information")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
**📍 Address**

Hospital AI Management System

Jaipur, Rajasthan

India
""")

        st.markdown("""
**☎ Phone**

+91-9876543210
""")

    with col2:

        st.markdown("""
**📧 Email**

support@hospitalai.com
""")

        st.markdown("""
**🕒 Working Hours**

24×7 Emergency & Support Services
""")

    st.divider()

    st.caption(
        "Hospital AI Management System | Version 1.0 | © 2026"
    )