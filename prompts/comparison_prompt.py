def get_prompt(question, prompt_type):

    if prompt_type == "Basic":

        return f"""
        Explain:
        {question}
        """

    elif prompt_type == "Role":

        return f"""
        You are a professional tutor.

        Explain:
        {question}
        """

    elif prompt_type == "Structured":

        return f"""
        Explain with format:

        1. Definition
        2. Example
        3. Conclusion

        Topic:
        {question}
        """

    elif prompt_type == "Few-Shot":

        return f"""
        Example:

        Question:
        What is HTML?

        Answer:
        Definition:
        HTML creates web pages.

        Example:
        Websites use HTML.

        Conclusion:
        HTML structures web content.

        ------------------

        Question:
        {question}
        """