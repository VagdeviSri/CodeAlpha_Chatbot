import tkinter as tk
from tkinter import scrolledtext

# FAQ Database
faq = {
    "hello": "Hello! How can I help you?",
    "what is your name": "I am an FAQ Chatbot.",
    "how can i contact support": "You can contact support at support@example.com",
    "what courses do you offer": "We offer Python, AI, ML, Data Science and Web Development.",
    "working hours": "Our working hours are 9 AM to 6 PM.",
    "bye": "Goodbye! Have a great day."
}

# Function
def send_message():
    user_msg = entry.get().lower()

    chat_area.insert(tk.END, f"You: {user_msg}\n")

    response = faq.get(user_msg, "Sorry, I don't understand that question.")

    chat_area.insert(tk.END, f"Bot: {response}\n\n")

    entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x500")

chat_area = scrolledtext.ScrolledText(root, width=70, height=20)
chat_area.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

root.mainloop()