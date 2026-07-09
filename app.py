from chatbot.ai_engine import AIChatbot

def main():

    bot = AIChatbot()

    print("OpenMind AI Assistant Started")
    print("Type 'exit' to stop")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            break

        response = bot.generate_response(user_message)

        print("AI:", response)


if _name_ == "_main_":
    main()
