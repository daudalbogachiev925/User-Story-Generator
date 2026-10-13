import streamlit as st
from generator import generate
from templates import STORIES

st.title("📝 User Story Generator")
cat = st.selectbox("Категория", ["all"] + list(STORIES.keys()))
md = generate(None if cat == "all" else cat)
st.markdown(md)
st.download_button("Скачать Markdown", md, file_name="user_stories.md")
