def generate_study_plan_prompt(topic, days):

    return f"""
    You are an expert study planner.

    Create a detailed {days}-day study plan for learning:
    {topic}

    For each day include:
    1. Topic to study
    2. Learning objective
    3. Practice activity
    4. Study tips

    Make the plan beginner-friendly and organized.
    """