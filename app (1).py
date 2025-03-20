
import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the fine-tuned model and tokenizer
model_path = "./math-riddle-model"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Custom Styling
page_bg_color = '''
<style>
    body {
        background: linear-gradient(to right, #f0f8ff, #e6f7ff);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: linear-gradient(to right, #f0f8ff, #e6f7ff);
    }
    .stTextInput>div>div>input {
        border: 2px solid #007BFF;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: scale(1.05);
    }
    .generated-riddle {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: #333;
    }
    .red-title {
        color: red;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
    }
</style>
'''

st.markdown(page_bg_color, unsafe_allow_html=True)

# Updated red title
st.markdown("<h1 class='red-title'>🧩 Math Riddle Generator</h1>", unsafe_allow_html=True)

user_input = st.text_input("💡 Enter a hint to generate a math riddle:")

if st.button("Generate Riddle"):
    input_text = f"Riddle: {user_input}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, temperature=0.7)
    generated_riddle = tokenizer.decode(output[0], skip_special_tokens=True)

    st.markdown('<div class="generated-riddle">📜 <b>Generated Riddle:</b><br>' + generated_riddle + '</div>', unsafe_allow_html=True)

# Footer Section
st.markdown('<div class="footer">🚀 Built by <b>Usman Saleem</b></div>', unsafe_allow_html=True)
