import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "curiouscurrent/omnicode"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

    # Generate response using the loaded model
    output = model.generate(**inputs, max_length=150, num_return_sequences=1)

    # Decode the generated response
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def main():
    st.title("Code Generation")

    prompt = st.text_area("Enter your Prompt", height=150)

    if st.button("Generate"):
        response = generate_response(prompt)
        st.text_area("Generated Code", value=response, height=500)

if __name__ == "__main__":
    main()
