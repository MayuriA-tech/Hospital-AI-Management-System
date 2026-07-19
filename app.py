import streamlit as st

from components.login import login
from components.sidebar import sidebar

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Hospital AI Management System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# HIDE DEFAULT STREAMLIT MULTIPAGE NAVIGATION
# =====================================================

st.markdown("""
<style>

/* Hide Streamlit Multipage Navigation */
[data-testid="stSidebarNav"]{
    display:none;
}

/* Hide Streamlit Header */
header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD CSS
# =====================================================

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =====================================================
# SESSION
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = None

# =====================================================
# LOGIN
# =====================================================

if not st.session_state.logged_in:
    login()
    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    menu = sidebar(st.session_state.role)

# =====================================================
# LOGOUT
# =====================================================

if menu == "🚪 Logout":

    st.session_state.clear()
    st.rerun()

# =====================================================
# IMPORT PAGES
# =====================================================

from views.dashboard import dashboard_page
from views.ai_assistant import ai_assistant_page
from views.patient_database import patient_database_page
from views.patient_report import patient_report_page
from views.analytics import analytics_page
from views.policies import policies_page
from views.help import help_page
from views.contact import contact_page

# =====================================================
# VISITOR
# =====================================================

if st.session_state.role == "Visitor":

    if menu == "🏠 Dashboard":
        dashboard_page()

    elif menu == "🤖 AI Assistant":
        ai_assistant_page()

    elif menu == "📚 Hospital Policies":
        policies_page()

    elif menu == "❓ Help":
        help_page()

    elif menu == "📞 Contact":
        contact_page()

# =====================================================
# ADMIN / DOCTOR / STAFF
# =====================================================

else:

    if menu == "🏠 Dashboard":
        dashboard_page()

    elif menu == "🤖 AI Assistant":
        ai_assistant_page()

    elif menu == "👨‍⚕️ Patient Database":
        patient_database_page()

    elif menu == "📄 Reports":
        patient_report_page()

    elif menu == "📊 Analytics":
        analytics_page()

    elif menu == "📚 Hospital Policies":
        policies_page()

    elif menu == "❓ Help":
        help_page()

    elif menu == "📞 Contact":
        contact_page()