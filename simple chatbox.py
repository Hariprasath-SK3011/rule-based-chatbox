def simple_chatbot():
    print("🤖 Hello! I’m your chatbot. Type 'exit' to stop chatting.")
    
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("🤖 Goodbye! Have a nice day...")
            break

        # Greetings
        elif user_input in ["hi", "hello", "hey", "heyy"]:
            print("🤖 Hey there! How can I help you today?")

        # Asking how the bot is
        elif "how are you" in user_input:
            print("🤖 I’m doing well. Thanks for asking!")

        # Asking the bot's name
        elif "your name" in user_input:
            print("🤖 You can call me Chatter!")

        # User telling their name
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip().capitalize()
            print(f"🤖 Nice to meet you, {name}!")

        # Asking about the weather
        elif "weather" in user_input:
            print("🤖 I can't check weather yet, but it’s always sunny in the code world!")
        
        elif "bye" in user_input:
            print("🤖 bye")
        # Default
        else:
            print("🤖 I'm not sure how to respond to that. Try saying something else.")

simple_chatbot()
