import streamlit as st
import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "omnicode",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        st.error("Error occurred: {}".format(response.text))

def main():
    st.title("Omnicode Chat")
    prompt = st.text_area("Enter your Prompt", height=200)
    if st.button("Generate Response"):
        response = generate_response(prompt)
        if response:
            st.write("Response:")
            st.write(response)

if __name__ == "__main__":
    main()
