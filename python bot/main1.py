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

    if user_input != '':
        bot_response = get_bot_response(user_input)
        chat_history.config(state=NORMAL)
        
        chat_history.insert(END, f"You: {user_input}\n", "user")
        chat_history.insert(END, f"Bot: {bot_response}\n", "bot")
        
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
chat_history.tag_config("bot", foreground="black", justify='left')

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

# Run the main loop
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
