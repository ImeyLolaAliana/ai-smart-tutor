import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def compare_prompts(question):

    prompt = f"""
    Compare these prompting techniques for this topic:

    Topic:
    {question}

    Create responses for:

    1. Basic Prompt
    2. Role Prompt
    3. Structured Prompt
    4. Few-Shot Prompt

    Separate each result clearly.
    """

    response = model.generate_content(prompt)

    return response.text