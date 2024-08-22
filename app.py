import streamlit as st
import google-generativeai as genai

# Set the title of the Streamlit app
st.title("Wanna Go For A Brain Safari ?")

# Get the API key from the user
api_key = st.text_input("Enter your API key", type="password")

# Check if the API key is provided
if api_key:
    # Configure the Generative AI API with the user's API key
    genai.configure(api_key=api_key)

    # Create a text input for the user to enter their question
    text = st.text_input("Enter your question")

    # Initialize the Generative Model and start the chat
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    # Create a button that, when clicked, will send the user's input to the model
    if st.button("Click me"):
        # Send the user's message to the chat model
        response = chat.send_message(text)

        # Display the model's response in the Streamlit app
        st.write(response.text)
else:
    st.write("Please enter your API key to continue.")
