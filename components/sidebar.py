import streamlit as st
from streamlit_option_menu import option_menu


def sidebar(role):

    # ----------------------------------------------------
    # Header
    # ----------------------------------------------------

    st.markdown(
        """
        <div style="text-align:center;padding:10px 0;">
            <h2 style="color:#2563EB;margin-bottom:0;">
                🏥 Hospital AI
            </h2>
            <p style="color:#6B7280;margin-top:2px;">
                Management System
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ----------------------------------------------------
    # User Information
    # ----------------------------------------------------

    username = st.session_state.get("username", "User")

    st.markdown(
        f"""
        <div style="
            background:#F8FAFC;
            border-radius:12px;
            padding:15px;
            margin-bottom:20px;
            border:1px solid #E5E7EB;
        ">

        <h4 style="margin:0;color:#111827;">
            👤 {username}
        </h4>

        <p style="margin:5px 0 0 0;color:#6B7280;">
            Role : <b>{role}</b>
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------
    # Visitor Menu
    # ----------------------------------------------------

    if role == "Visitor":

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "AI Assistant",
                "Hospital Policies",
                "Help",
                "Contact",
                "Logout",
            ],
            icons=[
                "house",
                "robot",
                "book",
                "question-circle",
                "telephone",
                "box-arrow-right",
            ],
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#FFFFFF",
                },
                "icon": {
                    "color": "#2563EB",
                    "font-size": "18px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#EFF6FF",
                    "border-radius": "10px",
                },
                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "white",
                },
            },
        )

        mapping = {
            "Dashboard": "🏠 Dashboard",
            "AI Assistant": "🤖 AI Assistant",
            "Hospital Policies": "📚 Hospital Policies",
            "Help": "❓ Help",
            "Contact": "📞 Contact",
            "Logout": "🚪 Logout",
        }

    # ----------------------------------------------------
    # Admin / Doctor / Staff
    # ----------------------------------------------------

    else:

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "AI Assistant",
                "Patient Database",
                "Reports",
                "Analytics",
                "Hospital Policies",
                "Help",
                "Contact",
                "Logout",
            ],
            icons=[
                "house",
                "robot",
                "people",
                "file-earmark-text",
                "bar-chart",
                "book",
                "question-circle",
                "telephone",
                "box-arrow-right",
            ],
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#FFFFFF",
                },
                "icon": {
                    "color": "#2563EB",
                    "font-size": "18px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#EFF6FF",
                    "border-radius": "10px",
                },
                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "white",
                },
            },
        )

        mapping = {
            "Dashboard": "🏠 Dashboard",
            "AI Assistant": "🤖 AI Assistant",
            "Patient Database": "👨‍⚕️ Patient Database",
            "Reports": "📄 Reports",
            "Analytics": "📊 Analytics",
            "Hospital Policies": "📚 Hospital Policies",
            "Help": "❓ Help",
            "Contact": "📞 Contact",
            "Logout": "🚪 Logout",
        }

    st.divider()

    st.caption("© 2026 Hospital AI")

    return mapping[selected]