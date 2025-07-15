import streamlit as st
from main import get_cover_letter

# Page config
st.set_page_config(page_title="AI Cover Letter Generator", layout="centered")

# App Title
st.title("📄 Cover Letter Generator")
st.markdown("Generate smart, customized cover letters using your **CV** and a **LinkedIn job URL** — powered by OpenAI.")

# Sidebar for API Key
st.sidebar.header("🔐 OpenAI Configuration")
openai_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
st.sidebar.markdown(
    "💡 [Get your API key](https://platform.openai.com/account/api-keys) from OpenAI"
)

# Cover Letter Generator Function
def generate_response(linkedin_url, uploaded_cv, api_key):
    if uploaded_cv is not None:
        output = get_cover_letter(linkedin_url, uploaded_cv, api_key)
        st.subheader("✉️ Generated Cover Letter:")
        st.write(output)
    else:
        st.warning("Please upload a CV file (PDF format).", icon="⚠️")

# Input Form
with st.form("cover_letter_form"):
    linkedin_url = st.text_area("🔗 Paste LinkedIn Job URL", placeholder="https://www.linkedin.com/jobs/view/...")
    uploaded_cv = st.file_uploader("📎 Upload Your CV (PDF only)", type=["pdf"])
    submitted = st.form_submit_button("🚀 Generate Cover Letter")

    if submitted:
        if not openai_api_key.startswith("sk-"):
            st.error("Please enter a valid OpenAI API Key in the sidebar.")
        elif not linkedin_url.strip():
            st.error("Please paste a LinkedIn job URL.")
        else:
            generate_response(linkedin_url, uploaded_cv, openai_api_key)
