from tkinter import *
import re
from responses import responses  # Importing responses from responses.py

def preprocess_text(text):
    """Removes special characters using regular expression"""
    return re.sub(r'[^\w\s]', '', text)

def get_bot_response(user_input):
    user_input = preprocess_text(user_input.lower())
    for response in responses:
        response_input = preprocess_text(response["input"].lower())
        if user_input in response_input:
            return response["response"]
    return "I'm sorry, I am not trained to respond to that. Please ask me something else."

def send_message(event=None):
    user_input = entry_field.get().strip()
    entry_field.delete(0, END)

    if user_input.lower() == 'goodbye':
        bot_response = "Goodbye! If you need assistance in the future, don't hesitate to come back. Take care!"
        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"Bot: {bot_response}\n", "bot_text")
        chat_history.config(state=DISABLED)
        chat_history.see(END)
        window.after(3000, window.destroy)  # Close the window after 3 seconds
        return

    if user_input.lower() == 'hello':
        bot_response = "Hello! I'm here to assist you. How can I help you today?\n"
        bot_response += "Type 'goodbye' if you want to end this conversation."
    else:
        bot_response = get_bot_response(user_input)

    if user_input != '':
        chat_history.config(state=NORMAL)

        # Insert user input with customized font
        chat_history.insert(END, "You: ", "user")
        chat_history.insert(END, user_input + "\n", "user_text")

        # Insert bot response with customized font
        chat_history.insert(END, "Bot: ", "bot")
        chat_history.insert(END, bot_response + "\n", "bot_text")

        chat_history.config(state=DISABLED)
        chat_history.see(END)

def clear_chat():
    chat_history.config(state=NORMAL)
    chat_history.delete(1.0, END)
    chat_history.config(state=DISABLED)

def about_chatbot():
    # You can replace this with your desired action for the About button
    # For example, opening a new window with chatbot information
    about_window = Tk()
    about_window.title("About Mental Health Chatbot")
    about_label = Label(about_window, text="This is a mental health chatbot designed to provide basic support and resources.")
    about_label.pack()
    about_window.mainloop()

def on_closing():
    window.destroy()

# Create the main window
window = Tk()
window.title("Mental Health Chatbot")
window.configure(background="#e5ddd5")  # Set background color similar to WhatsApp

# Chat history display
chat_history = Text(window, bd=0, width=50, height=20, state=DISABLED, wrap=WORD)
chat_history.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Add tags for different response types
chat_history.tag_config("user", foreground="blue", justify='right')
chat_history.tag_config("bot", foreground="green", justify='left')

# Create frame for user input and send button
input_frame = Frame(window)
input_frame.pack(side=TOP, fill=X)

# User input field
entry_field = Entry(input_frame, width=50)
entry_field.bind("<Return>", send_message)
entry_field.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

# Send button
send_button = Button(input_frame, text="Send", command=send_message, bg="#25D366", fg="white")
send_button.pack(side=RIGHT, padx=10, pady=10, fill=X)

# Create frame for Clear Chat, About, and Exit buttons
button_frame = Frame(window)
button_frame.pack(side=TOP, fill=X)

# Clear chat button
clear_button = Button(button_frame, text="Clear Chat", command=clear_chat, bg="#FFFF00", fg="black")
clear_button.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

# About button
about_button = Button(button_frame, text="About", command=about_chatbot, bg="#ADD8E6", fg="black")
about_button.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

# Exit button
exit_button = Button(button_frame, text="Exit", command=on_closing)
exit_button.pack(side=LEFT, padx=10, pady=10, fill=X, expand=True)

# Add custom font configurations
chat_history.tag_config("user_text", font=("Arial", 10, "bold", "italic"))  # Change "Arial" to your desired font family and 10 to your desired font size
chat_history.tag_config("bot_text", font=("Roboto", 10, "bold"))  # Change "Roboto" to your desired font family and 10 to your desired font size

# Welcome message
welcome_message = "Hello! I'm your Mental Health Chatbot. How can I assist you today?\n"
welcome_message += "Type 'goodbye' if you want to end this conversation.\n"
chat_history.config(state=NORMAL)
chat_history.insert(END, welcome_message, "bot_text")
chat_history.config(state=DISABLED)
chat_history.see(END)

# Run the main loop
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
