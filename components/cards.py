import streamlit as st


# ==========================================================
# KPI CARD
# ==========================================================

def metric_card(title, value, icon, color="#2563EB"):

    st.markdown(
        f"""
<div style="background:#FFFFFF;
padding:22px;
border-radius:18px;
border-top:5px solid {color};
box-shadow:0 6px 18px rgba(0,0,0,0.08);
margin-bottom:10px;">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div>

<p style="
margin:0;
font-size:16px;
font-weight:600;
color:#4B5563;">
{title}
</p>

<h1 style="
margin-top:10px;
margin-bottom:0;
font-size:34px;
font-weight:700;
color:#111827;">
{value}
</h1>

</div>

<div style="
font-size:40px;">
{icon}
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(title):

    st.markdown(
        f"""
<h2 style="
color:#111827;
font-size:28px;
font-weight:700;
margin-top:20px;
margin-bottom:8px;">
{title}
</h2>

<div style="
height:2px;
background:#E5E7EB;
margin-bottom:18px;">
</div>
""",
        unsafe_allow_html=True,
    )