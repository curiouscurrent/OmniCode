import gradio as gr

# Importing the required libraries
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load model directly
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

# System message
system_message = '''
I am a code teaching assistant named as OmniCode created 
by Anusha K. I will answer all the code related questions being asked."
'''


def generate_response(prompt, max_length=1000, temperature=1.0):
    input_text = system_message + "\n" + prompt
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate response
    output = model.generate(input_ids,
                             max_length=max_length,
                             temperature=temperature,
                             pad_token_id=tokenizer.eos_token_id,
                             num_return_sequences=1)

    # Decode and return the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


# Create Gradio interface
def chat_with_omnicode(prompt):
    response = generate_response(prompt, max_length=1000)  # Adjust max_length as needed
    return response


iface = gr.Interface(fn=chat_with_omnicode, inputs="text", outputs="text", title="OmniCode")
iface.launch()
