import streamlit as st
import pandas as pd

from agents.orchestrator import orchestrate


# ==========================================================
# AI ASSISTANT PAGE
# ==========================================================

def ai_assistant_page():

    # ------------------------------------------------------
    # SESSION
    # ------------------------------------------------------

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ------------------------------------------------------
    # HEADER
    # ------------------------------------------------------

    st.markdown(
        """
        <h1 style="color:#2563EB;margin-bottom:0px;">
            🤖 Hospital AI Assistant
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p style="color:#4B5563;font-size:17px;margin-top:0px;">
            Ask anything related to hospital records, patient information or hospital policies.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([8, 1])

    with col2:
        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

    st.divider()

    # ------------------------------------------------------
    # DISPLAY CHAT HISTORY
    # ------------------------------------------------------

    for chat in st.session_state.chat_history:

        with st.chat_message(chat["role"]):

            if isinstance(chat["content"], pd.DataFrame):

                st.success(f"✅ {len(chat['content'])} record(s) found")

                st.dataframe(
                    chat["content"],
                    use_container_width=True,
                    hide_index=True,
                )

            else:
                st.markdown(chat["content"])

    # ------------------------------------------------------
    # USER INPUT
    # ------------------------------------------------------

    prompt = st.chat_input("Ask your question...")

    if prompt:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # --------------------------------------------------
        # VISITOR SECURITY
        # --------------------------------------------------

        restricted_keywords = [
            "patient",
            "patients",
            "doctor",
            "hospital records",
            "medical condition",
            "age",
            "gender",
            "blood",
            "billing",
            "insurance",
            "room",
            "admission",
            "discharge",
            "medication",
            "test result",
            "database",
            "count",
            "average",
            "maximum",
            "minimum",
        ]

        if st.session_state.role == "Visitor":

            question = prompt.lower()

            if any(
                word in question
                for word in restricted_keywords
            ):

                answer = """
### 🔒 Access Denied

Patient information is confidential.

Please login as **Doctor**, **Staff** or **Administrator**
to access hospital records.
"""

                with st.chat_message("assistant"):
                    st.error(answer)

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

                return

        # --------------------------------------------------
        # AI RESPONSE
        # --------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("🧠 AI is analysing your request..."):

                try:

                    response = orchestrate(prompt)

                    if isinstance(response, pd.DataFrame):

                        st.success(f"✅ Found {len(response)} record(s)")

                        st.dataframe(
                            response,
                            use_container_width=True,
                            hide_index=True,
                        )

                        csv = response.to_csv(index=False).encode("utf-8")

                        st.download_button(
                            "📥 Download Result (CSV)",
                            csv,
                            "query_result.csv",
                            "text/csv",
                            use_container_width=True,
                        )

                        st.session_state.chat_history.append(
                            {
                                "role": "assistant",
                                "content": response,
                            }
                        )

                    else:

                        st.markdown(response)

                        st.session_state.chat_history.append(
                            {
                                "role": "assistant",
                                "content": response,
                            }
                        )

                except Exception as e:

                    st.error(f"❌ Error: {str(e)}")

                    st.session_state.chat_history.append(
                        {
                            "role": "assistant",
                            "content": f"❌ Error: {str(e)}",
                        }
                    )