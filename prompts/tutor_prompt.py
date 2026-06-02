def generate_prompt(question, level):

    # =========================================
    # BEGINNER
    # =========================================
    if level == "Beginner":

        return f"""
        You are a friendly AI tutor for beginners.

        Here is an example format:

        Question:
        What is HTML?

        Answer:
        1. Definition:
        HTML is a language used to create web pages.

        2. Simple Explanation:
        HTML helps structure content like text, images, and buttons on websites.

        3. Real-Life Example:
        Websites like YouTube and Google use HTML.

        4. Summary:
        HTML is the foundation of web pages.

        -----------------------------------

        Now answer this question using the SAME format:

        Question:
        {question}
        """

    # =========================================
    # INTERMEDIATE
    # =========================================
    elif level == "Intermediate":

        return f"""
        You are an AI tutor.

        Example:

        Question:
        What is Python?

        Answer:
        1. Definition:
        Python is a high-level programming language.

        2. Main Concepts:
        Python is used for web development, AI, automation, and data science.

        3. Example:
        Python can be used to build chatbots.

        4. Important Notes:
        Python is beginner-friendly and widely used.

        -----------------------------------

        Now answer this question using the SAME format:

        Question:
        {question}
        """

    # =========================================
    # ADVANCED
    # =========================================
    elif level == "Advanced":

        return f"""
        You are an expert academic tutor.

        Example:

        Question:
        What is Artificial Intelligence?

        Answer:
        1. Formal Definition:
        Artificial Intelligence is a branch of computer science focused on creating systems capable of simulating human intelligence.

        2. Deep Explanation:
        AI involves machine learning, neural networks, and natural language processing.

        3. Technical Example:
        AI is used in recommendation systems and autonomous vehicles.

        4. Advantages and Disadvantages:
        AI improves efficiency but may introduce ethical concerns.

        5. Conclusion:
        AI is transforming modern technology and industries.

        -----------------------------------

        Now answer this question using the SAME format:

        Question:
        {question}
        """