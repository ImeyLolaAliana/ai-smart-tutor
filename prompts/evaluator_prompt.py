def generate_evaluator_prompt(question, student_answer):

    return f"""
    You are a strict teacher.

    Evaluate the student's answer carefully.

    Question:
    {question}

    Student Answer:
    {student_answer}

    Provide evaluation using this format:

    1. Score (0-100)
    2. Correctness
    3. Strengths
    4. Mistakes
    5. Suggestions for Improvement
    6. Final Feedback

    Be supportive and educational.
    """