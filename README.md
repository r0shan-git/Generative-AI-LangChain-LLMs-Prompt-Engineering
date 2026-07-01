# 🎬 CineSage - AI Movie Information Extractor

An AI-powered Movie Information Extractor built using **LangChain**, **Large Language Models (LLMs)**, and **Streamlit**. The application extracts structured movie information from an unstructured movie description using modern prompt engineering techniques.

---

## 🚀 Features

- 🎥 Extract movie title
- 📅 Detect release year
- 🎭 Identify movie genres
- 🎬 Extract director name
- ⭐ Extract cast/actors
- 🤖 Powered by Large Language Models
- 🎨 Interactive Streamlit UI
- ⚡ Built with LangChain Prompt Engineering

---

## 🛠️ Tech Stack

- Python 3.11
- LangChain
- Streamlit
- Mistral AI
- Hugging Face Embeddings
- Pydantic
- python-dotenv
- UV Package Manager

---

## 📂 Project Structure

```text
Generative-AI/
│
├── CineSage/
│   ├── UIcore.py
│   └── core.py
│
├── chatmodels/
├── embeddingmodels/
│
├── .env
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/r0shan-git/Generative-AI-LangChain-LLMs-Prompt-Engineering.git
```

Move into the project folder

```bash
cd Generative-AI-LangChain-LLMs-Prompt-Engineering
```

---

### Create Virtual Environment

Using UV

```bash
uv venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### Install Dependencies

Using UV

```bash
uv sync
```

or using pip

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run CineSage/UIcore.py
```

or

```bash
python -m streamlit run CineSage/UIcore.py
```

---

## 📸 Application Preview

### Home Page

- Paste a movie description.
- Click **Extract Information**.
- View structured movie details.

Example input:

```text
Inception is a 2010 science fiction action thriller directed by Christopher Nolan. The movie stars Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy, Ken Watanabe, and Cillian Murphy.
```

Example output

```
Title: Inception

Release Year: 2010

Genre:
- Science Fiction
- Action
- Thriller

Director:
- Christopher Nolan

Actors:
- Leonardo DiCaprio
- Joseph Gordon-Levitt
- Elliot Page
- Tom Hardy
- Ken Watanabe
- Cillian Murphy
```

---

## 📚 Learning Objectives

This project demonstrates:

- Prompt Engineering
- LangChain Prompt Templates
- Structured Output Parsing
- Pydantic Models
- Streamlit Application Development
- Environment Variable Management
- LLM Integration
- Python Project Structure

---

## 🔮 Future Improvements

- Movie Poster Integration
- IMDb Rating
- TMDB API Support
- Multi-LLM Support
- Voice Input
- PDF Export
- RAG-based Movie Chatbot
- Multi-language Support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

- GitHub: https://github.com/r0shan-git

---

⭐ If you found this project useful, please consider giving it a Star.