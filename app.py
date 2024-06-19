import streamlit as st

# load the README file and display it

with open("README.md", "r") as f:
    readme = f.read()

st.markdown(readme)