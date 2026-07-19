import streamlit as st

# ---------------------------------------------------
# Dummy Users (Replace with DB authentication later)
# ---------------------------------------------------

USERS = {
    "Admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "Doctor": {
        "password": "doctor123",
        "role": "Doctor"
    },
    "Staff": {
        "password": "staff123",
        "role": "Staff"
    }
}


# ---------------------------------------------------
# Login Function
# ---------------------------------------------------

def login():

    # Hide sidebar completely
    st.markdown("""
        <style>
            section[data-testid="stSidebar"]{
                display:none;
            }
        </style>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='login-box'>
                <h1 style='text-align:center;'>🏥</h1>
                <h2 style='text-align:center;color:#2563EB;'>
                    Hospital AI Management System
                </h2>
                <p style='text-align:center;color:gray;'>
                    Please login to continue
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        username = st.selectbox(
            "Username",
            ["Admin", "Doctor", "Staff"]
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        st.write("")

        if st.button("🔐 Login", use_container_width=True):

            if password == USERS[username]["password"]:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = USERS[username]["role"]

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Invalid Password")

        st.write("")

        st.markdown("---")

        st.write("")

        if st.button("👤 Continue as Visitor", use_container_width=True):

            st.session_state.logged_in = True
            st.session_state.username = "Visitor"
            st.session_state.role = "Visitor"

            st.rerun()