from responses import responses
import re

def preprocess_text(text):
    # Remove special characters using regular expression
    return re.sub(r'[^\w\s]', '', text)

def get_bot_response(user_input):
    user_input = preprocess_text(user_input.lower())  # Convert user input to lowercase and remove special characters
    for response in responses:
        response_input = preprocess_text(response["input"].lower())  # Convert response input to lowercase and remove special characters
        if user_input in response_input:  # Check if user input is contained in response input
            return response["response"]
    return "I'm sorry, I am not trained to respond to that. Please ask me something else."

def main():
    print("Bot: Hello! I'm your mental health chatbot.")
    print("Bot: You can type 'bye' to exit at any time.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input == 'bye':
            print("Bot: Goodbye! Take care.")
            break
        
        bot_response = get_bot_response(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
