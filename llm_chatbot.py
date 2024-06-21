

import streamlit as st
import requests
import json

# Function to parse the multi-line JSON response
def parse_multiline_json(response_text):
    for line in response_text.strip().split('\n'):
        yield json.loads(line)

# Function to query the local LLM service
def query_llm(messages):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3",
        "messages": messages
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        try:
            full_response = ""
            for response_data in parse_multiline_json(response.text):
                message_content = response_data.get("message", {}).get("content", "")
                full_response += message_content + " "
            return full_response.strip()
        except json.JSONDecodeError as e:
            st.error(f"JSONDecodeError: {e.msg}")
            st.write(f"Response content: {response.content}")
            return "Error: Unable to parse JSON response from the model"
    else:
        st.error(f"Error: {response.status_code}")
        return "Error: Unable to get a response from the model"

def get_model_response(user_message):
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    st.session_state.conversation.append({"role": "user", "content": user_message})
    response = query_llm(st.session_state.conversation)
    st.session_state.conversation.append({"role": "assistant", "content": response})
    return response

# Streamlit application
def main():
    st.title("Chat with Local LLM - llama3")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    def clear_conversation():
        st.session_state.conversation = []

    st.button("Clear Conversation", on_click=clear_conversation)

    with st.form(key='chat_form'):
        user_input = st.text_input("You:", "")
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            response = get_model_response(user_input)
            st.experimental_rerun()

    if st.session_state.conversation:
        for message in st.session_state.conversation:
            if message["role"] == "user":
                st.write(f"👤: {message['content']}")
            else:
                st.write(f"🤖: {message['content']}")

if __name__ == "__main__":
    main()
