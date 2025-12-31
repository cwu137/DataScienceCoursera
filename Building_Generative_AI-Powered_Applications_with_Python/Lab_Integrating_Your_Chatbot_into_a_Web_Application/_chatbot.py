from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []
# while True:
#     # Create conversation history string
#     history_string = "\n".join(conversation_history)
#     # Get the input data from the user
#     input_text = input("> ")
#     # Tokenize the input text and history
#     inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
#     # Generate the response from the model
#     outputs = model.generate(**inputs)
#     # Decode the response
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
#     print(response)
#     # Add interaction to conversation history
#     conversation_history.append(input_text)
#     conversation_history.append(response)

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Create conversation history string
    history = "\n".join(conversation_history)
    
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")
    
    # Generate the response from the model
    outputs = model.generate(**inputs, max_length= 60)  # max_length will cause the model to crash at some point as history grows
    
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)
    return response
    
if __name__ == '__main__':
    app.run()