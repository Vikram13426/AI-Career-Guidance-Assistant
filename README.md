
**AI-Powered Career Guidance Assistant** built with **Flask + LangChain + Gemini Flash**.

CareerPilot AI helps users discover personalized career paths, skill recommendations, structured learning roadmaps, project ideas, and interview guidance — all powered by AI.

---

## ✨ Features

- Personalized career recommendations based on skills, interests, experience & goals
- Tailored learning roadmaps with timelines and milestones
- Beginner-friendly project ideas to build a strong portfolio
- Interview preparation guidance with common questions and tips
- Curated free learning resources
- Modern, responsive, SaaS-style user interface
- Fast and intelligent responses using Gemini 1.5 Flash

---

## 🛠 Tech Stack

| Technology              | Purpose                          |
|-------------------------|----------------------------------|
| **Flask**               | Backend Framework                |
| **LangChain**           | AI Workflow Orchestration        |
| **Gemini 2.5 Flash**    | Large Language Model             |
| **HTML + CSS + JS**     | Frontend                         |
| **python-dotenv**       | Environment Variables            |

---

## 🧠 What is LangChain?

**LangChain** is a popular open-source framework that simplifies building applications powered by Large Language Models (LLMs).

It allows developers to easily connect LLMs with external data, tools, memory, and business logic — making it possible to create powerful, reliable, and production-ready AI applications.

### Key Components Used in This Project:
- **Prompt Templates** — For dynamic and reusable prompts
- **LCEL (LangChain Expression Language)** — Modern way to build clean AI pipelines
- **LLM Integration** — Connecting Gemini Flash
- **Output Parsers** — Formatting AI responses cleanly

---

## 🧩 LangChain Concepts Demonstrated

- **Prompt Templates** – Dynamic prompt creation with user inputs
- **LCEL Pipelines** – Clean, readable, and modular workflow using `prompt | llm | parser`
- **LLM Integration** – Using Google Gemini via LangChain
- **Output Parsers** – Converting raw LLM output into user-friendly text
- Modular chain architecture for scalability and maintainability

---

## 📂 Project Structure

```text
AI_CAREER_ASSISTANT/
├── app.py                      # Flask application
├── requirements.txt
├── .env
├── README.md
│
├── chains/
│   └── career_chain.py         # LCEL Chain definition
│
├── utils/
│   └── prompts.py              # Prompt templates
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd AI_CAREER_ASSISTANT
```

### 2. Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Gemini API Key
Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and generate a free API key.

### 5. Create `.env` file
```env
GOOGLE_API_KEY=your_api_key_here
```

### 6. Run the Application
```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## 📖 What You’ll Learn

- Fundamentals of LangChain and LCEL
- Building production-style AI pipelines
- Effective prompt engineering
- Full-stack AI application development
- Clean architecture and modular design

Ideal for portfolios, internships, and showcasing modern AI engineering skills.

---

## 🔮 Future Enhancements

- Multi-turn conversation with memory
- Resume upload and analysis
- RAG (Retrieval-Augmented Generation)
- User authentication & personal dashboard
- Streaming AI responses
- PDF export for roadmaps

---

## 📜 License

This project is open-source and free to use for learning and personal projects.

---

**Made with ❤️ for aspiring developers and AI enthusiasts.**

Feel free to ⭐ star this repo if you found it useful!
```

