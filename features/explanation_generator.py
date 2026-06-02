import google.generativeai as genai
from config import GEMINI_API_KEY

# Konfigurasi Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_explanation(prompt):

    response = model.generate_content(prompt)

    return response.text