import streamlit as st
from transformers import pipeline

# Load your model from Hugging Face
model = pipeline("text-generation", model="curiouscurrent/omnicode")

def generate_response(prompt):
    # Generate response using the loaded model
    response = model(prompt, max_length=50, do_sample=False)[0]['generated_text']
    return response

def main():
    st.title("Code Generation")

    prompt = st.text_area("Enter your Prompt", height=150)

    if st.button("Generate"):
        response = generate_response(prompt)
        st.text_area("Generated Code", value=response, height=500)

if __name__ == "__main__":
    main()
