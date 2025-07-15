import openai
import pdfminer
from pdfminer.high_level import extract_text

def extract_cv_text(uploaded_cv_file):
    try:
        # Save the uploaded PDF to a temporary path and extract text
        text = extract_text(uploaded_cv_file)
        return text
    except Exception as e:
        return "Error reading PDF: " + str(e)

def get_cover_letter(linkedin_url, uploaded_cv_file, api_key):
    openai.api_key = api_key

    cv_text = extract_cv_text(uploaded_cv_file)

    if "Error" in cv_text:
        return cv_text

    prompt = f"""
    You are an expert HR assistant.

    Generate a professional and personalized cover letter based on the following resume and LinkedIn job posting.

    ----
    Resume (CV):
    {cv_text}

    ----
    LinkedIn Job Description:
    {linkedin_url}

    ----
    Keep the tone confident and slightly formal. Do not mention this was AI-generated.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use gpt-4 if available
            messages=[
                {"role": "system", "content": "You are a cover letter writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ Error generating cover letter: {e}"
