def generate_quiz_prompt(topic):

    return f"""
    You are an educational quiz generator.

    Create 5 multiple-choice questions about:
    {topic}

    Rules:
    - Each question must have 4 options
    - Include the correct answer
    - Include short explanations
    - Make the quiz interactive and educational
    """