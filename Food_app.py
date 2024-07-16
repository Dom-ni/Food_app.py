import streamlit as st
from PIL import Image
import numpy as np

img = Image.open('Jus Chow logo.png')
st.image(img)

import streamlit as st

# Function to generate a chatbot response based on user input
def get_chatbot_response(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello! Welcome to our restaurant. How can I help you today?"
    elif "menu" in user_input.lower() or "I'll like to make an order" in user_input.lower() or "I'll want place an order" in user_input.lower() or "what's on the menu" in user_input.lower():
        return "Our menu includes spicy jollof, fried rice, assorted meat stew, pasta, salads, and milkshake. Would you like to place an order?"
    elif "yes" in user_input.lower():
        return "Sure! What would you like to order?"
    elif "spicy jollof" in user_input.lower() or "fried rice" in user_input.lower() or "assorted meat stew" in user_input.lower() or "pasta" in user_input.lower() or "salads" in user_input.lower() or "milkshake" in user_input.lower():
        return "We are open from 10 AM to 10 PM every day... And your order has been taken!"
    elif "no" in user_input.lower():
        return "Okay! We are open from 10 AM to 10 PM every day... We expect your order soon!"
    elif "location" in user_input.lower():
        return "We are located at 39 Saburi, Dei-Dei, Abuja."
    elif "thank you" in user_input.lower() or "thanks" in user_input.lower():
        return "You're welcome! Is there anything else I can help you with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Streamlit app
st.title("JusChow Service bot")

# Initialize the conversation history in session state if it doesn't exist
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Display the conversation history
for chat in st.session_state.conversation:
    if chat['role'] == 'user':
        st.write(f"**You:** {chat['message']}")
    else:
        st.write(f"**Dami:** {chat['message']}")

# Input field for the user's message
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Append the user's message to the conversation
        st.session_state.conversation.append({'role': 'user', 'message': user_input})

        # Generate and append the chatbot's response to the conversation
        bot_response = get_chatbot_response(user_input)
        st.session_state.conversation.append({'role': 'Dami', 'message': bot_response})

        # Clear the input field by resetting the key
        st.experimental_rerun()

# Add a button to clear the conversation history
if st.button("Clear Conversation"):
    st.session_state.conversation.clear()
    st.experimental_rerun()





