# PDF Summarizer AI 🤖

A simple web application that lets you upload any PDF document and get an AI-powered summary using Google's Gemini model — all in your browser.

## ✨ Features

- **PDF Upload** — Drag-and-drop or browse to upload a PDF file
- **Text Extraction** — Automatically extracts text from all pages using PyPDF2
- **AI Summarization** — Sends the extracted text to Google Gemini 3.5 Flash for a clear, concise summary
- **Text Preview** — Shows a quick preview of the extracted content before summarizing
- **Secure API Key Input** — Enter your own Google Gemini API key (masked input, never stored)

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | [Streamlit](https://streamlit.io/) |
| PDF Parsing | [PyPDF2](https://pypi.org/project/PyPDF2/) |
| AI Model | [Google Gemini 3.5 Flash](https://ai.google.dev/) |

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mbadrawy1/AI-PDF-Summarizer.git
   cd AI-PDF-Summarizer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit google-generativeai PyPDF2
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open the URL shown in your terminal (usually `http://localhost:8501`), upload a PDF, enter your Gemini API key, and hit **Summarize PDF 🚀**.

## 📸 How It Works

1. Upload a PDF file through the browser UI.
2. The app extracts all text from the PDF pages.
3. A preview of the first 500 characters is displayed.
4. Enter your Google Gemini API key and click **Summarize**.
5. The AI reads the full text and returns a concise summary.

## 📁 Project Structure

```
AI-PDF-Summarizer/
├── app.py          # Main Streamlit application
├── README.md
└── venv/           # Python virtual environment (not committed)
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Mohamad Badrawy**

- GitHub: [@mbadrawy1](https://github.com/mbadrawy1)
