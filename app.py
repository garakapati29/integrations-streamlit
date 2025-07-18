import streamlit as st

# Load your HTML file
with open("siterecon.html", "r") as f:
    html_content = f.read()

# Display the HTML
st.components.v1.html(html_content, height=600, scrolling=True)
st.set_page_config(layout="wide")
