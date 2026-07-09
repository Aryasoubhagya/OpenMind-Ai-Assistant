class Memory:

    def __init__(self):
        self.conversation_history = []


    def save_message(self, message):

        self.conversation_history.append({
            "role": "user",
            "message": message
        })


    def get_history(self):

        return self.conversation_history


    def clear_memory(self):

        self.conversation_history = []
