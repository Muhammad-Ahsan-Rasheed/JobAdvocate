from credentials import email, password
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="JobAdvocate",
    page_icon="👋",
)

st.write("# Team PakDev! 👋")
st.write("## AI Job Coach")
st.markdown(
    """
    AI Job Coach is an AI powered platform designed to revolutionize the job search process. Our platform leverages the power of artificial intelligence to help job seekers create compelling cover letters, emails, and other job application materials.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
   st.markdown("### Cover Letter Generator")

with col2:
   st.markdown("### Email Generator")

with col3:
   st.markdown("### Job Search")


