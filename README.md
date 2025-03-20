# Math Riddle Generator

## Overview
The **Math Riddle Generator** is a Streamlit-based web application that generates unique math riddles based on user input. It leverages a fine-tuned GPT-2 model to create engaging and challenging riddles for users.

## Features
- Generates math riddles based on user hints
- Interactive UI with a modern, clean design
- Uses a fine-tuned GPT-2 model for text generation
- Styled using custom CSS for an improved user experience

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python (Transformers, PyTorch)
- **Deployment:** Ngrok (for tunneling)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Pip

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Math-Riddle-Generator.git
   cd Math-Riddle-Generator
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

4. If using Ngrok for public access:
   ```sh
   ngrok authtoken YOUR_NGROK_TOKEN
   ngrok http 8501
   ```

## Usage
- Enter a hint or topic for the riddle.
- Click "Generate Riddle" to receive a generated math riddle.
- Share the riddles with friends or use them in educational activities.

## License
This project is licensed under the MIT License.

## Author
**Usman Saleem**

---
Enjoy solving and sharing math riddles! 🚀

![image](https://github.com/user-attachments/assets/c0a5b5d7-8d3f-4038-ab97-6f22310730ed)
