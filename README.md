# 🤖 AI Interview Assistant

An AI-powered Interview Preparation Assistant built using **Streamlit** and **Hugging Face Inference API**. This application helps users practice interview questions, improve communication skills, and receive AI-generated responses through both text and voice input.

## 🚀 Features

- 💬 AI-generated interview answers
- 🎤 Speech-to-Text (Voice Input)
- ⌨️ Text-based question input
- 🤖 Powered by Hugging Face Inference API
- 🎨 User-friendly Streamlit interface
- ⚡ Fast and interactive responses

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- streamlit-mic-recorder

## 📁 Project Structure

```
AI_Interview_Assistant/
│── app.py
│── requirements.txt
│── README.md
```

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/suguna-44/AI_Interview_Assistant.git
```

2. Navigate to the project folder

```bash
cd AI_Interview_Assistant
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add your Hugging Face Token

Create a `.streamlit/secrets.toml` file:

```toml
HF_TOKEN = "your_huggingface_token"
```

5. Run the application

```bash
streamlit run app.py
```

## 📸 Application Workflow

1. Launch the application.
2. Enter an interview question or use voice input.
3. The speech is converted to text (if voice input is used).
4. The question is sent to the Hugging Face model.
5. AI generates an interview response.
6. The response is displayed to the user.

## 🎯 Future Enhancements

- Interview performance scoring
- Resume analysis
- Multiple interview domains
- Voice output
- Interview history

## 👩‍💻 Author

Neela suguna


## 📄 License

This project is developed for educational and learning purposes.
