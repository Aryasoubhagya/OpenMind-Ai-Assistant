from chatbot.memory import Memory


class AIChatbot:

    def __init__(self):
        self.memory = Memory()


    def generate_response(self, user_input):

        self.memory.save_message(user_input)

        response = f"""
Hello, I received your message:

{user_input}

I am OpenMind AI Assistant, an open-source chatbot
designed to support intelligent conversations.
"""

        return response
