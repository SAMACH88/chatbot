import streamlit as st
import pickle

# Load the pickled sentences list
with open('sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

def get_most_relevant_sentence(query, sentences):
    # ... your get_most_relevant_sentence logic ...
    return sentences[0]  # Example, replace with your actual logic

def chatbot(query):
    response = get_most_relevant_sentence(query, sentences)
    return response

def main():
    st.title("Text-Based Chatbot")
    st.write("Ask me anything related to the topic!")

    user_input = st.text_input("Your question:")

    if user_input:
        response = chatbot(user_input)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()