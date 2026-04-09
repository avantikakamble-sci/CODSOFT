import sys

def get_response(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! I am your friendly rule-based chatbot. How can I help you today?"

    elif "who are you" in user_input or "your name" in user_input:
        return "I'm a simple Python bot running on predefined rules!"

    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking! I don't have feelings, but my code is running smoothly."

    elif "weather" in user_input:
        return "I can't check the live weather yet, but it's always sunny inside my CPU!"

    elif "help" in user_input or "what can you do" in user_input:
        return "I can chat with you! Try asking about my name, how I am, or just say hello."

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I don't quite understand that. Could you try rephrasing?"

def chat():
    print("--- Rule-Based Chatbot ---")
    print("Type 'bye' to exit the conversation.")
    
    while True:
        user_input = input("You: ")
        
        response = get_response(user_input)
        print(f"Bot: {response}")
        
        # Break the loop if the user says goodbye
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    chat()
