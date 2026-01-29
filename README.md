# ✍️ AI Content Generation Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)](https://www.crewai.com/)
[![DeepSeek](https://img.shields.io/badge/LLM-DeepSeek--V3-green)](https://www.deepseek.com/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io/)

A production-ready, multi-agent autonomous system designed to research, draft, edit, and optimize high-quality long-form content. Powered by **CrewAI** and **DeepSeek-V3**, this pipeline orchestrates a team of specialized AI agents that collaborate to transform a simple topic into a comprehensive, SEO-optimized masterpiece.

## 🚀 Overview

The **AI Content Generation Pipeline** is built for content marketers, researchers, and developers who need high-quality editorial content without the manual overhead. Unlike simple LLM wrappers, this system employs a **sequential agentic workflow**. It breaks down the content creation process into professional stages: rigorous research, logical outlining, creative writing, meticulous fact-checking, and technical SEO optimization.

## ✨ Key Features

- **Autonomous Multi-Agent Orchestration**: Powered by CrewAI to manage state and handoffs between specialized agents.
- **Deep Research Integration**: Real-world web searching via DuckDuckGo to provide up-to-date facts and statistics.
- **Quality Assurance Layer**: Dedicated Editor and Fact-Checker agents to ensure accuracy and punchy prose.
- **SEO Optimization**: Integrated SEO Guru agent to optimize headers, keywords, and meta-structures.
- **Premium Streamlit UI**: A sleek, dark-mode dashboard for monitoring agent progress in real-time.
- **Version Control & Quality Scoring**: Automatic saving of content versions and heuristic-based quality metrics.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (Premium custom CSS UI)
- **Backend / Agent Framework**: [CrewAI](https://www.crewai.com/)
- **Orchestration**: Python 3.12
- **LLM**: [DeepSeek-V3](https://www.deepseek.com/) (via LangChain OpenAIChat interface)
- **Tools**: DuckDuckGo Search API, Markdown, Python-dotenv

## 🏗️ Architecture & Workflow

The system follows a sequential process where each agent's output serves as the context for the next:

1.  **🔍 Senior Research Analyst**: Gathers data, expert quotes, and latest trends from the web.
2.  **✍️ Expert Content Writer**: Drafts the narrative based on the research report.
3.  **📝 Senior Content Editor**: Refines flow, clarifies structure, and improves readability.
4.  **✅ Professional Fact Checker**: Verifies all scientific claims and statistics.
5.  **📈 SEO Optimization Expert**: Finalizes the metadata and keyword density for search ranking.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.12+
- A valid DeepSeek API Key ([Get one here](https://platform.deepseek.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/Ismail-2001/Content-Generation-Pipeline-Agent.git
cd Content-Generation-Pipeline-Agent
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
Create a `.env` file in the root directory:
```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

---

## 🚀 Usage

### Running Locally
To launch the Streamlit dashboard:
```bash
streamlit run app.py
```

1.  Enter your **Topic** (e.g., "The Impact of AGI on Software Engineering").
2.  Select the **Content Type** (Blog Post, Technical Article, etc.).
3.  Click **Generate High-Quality Content**.
4.  Monitor the agent logs in the dashboard and download the final Markdown file.

---

## 🌐 Deployment

### Option 1: Streamlit Community Cloud (Recommended)
1.  Push the code to your GitHub repository.
2.  Go to [share.streamlit.io](https://share.streamlit.io) and sign in.
3.  Click **New app** and select your repository.
4.  Add `DEEPSEEK_API_KEY` to the **Secrets** section:
    ```toml
    DEEPSEEK_API_KEY = "your_api_key_here"
    ```
5.  Click **Deploy**!

### Option 2: Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t ai-content-pipeline .
docker run -p 8501:8501 --env-file .env ai-content-pipeline
```

### Option 3: Railway / Render
1.  Connect your GitHub repository to [Railway](https://railway.app/) or [Render](https://render.com/).
2.  Add the `DEEPSEEK_API_KEY` environment variable in the dashboard.
3.  Deploy with one click!

---

## 🖼️ Screenshots / Demo

*(Upload your screenshots to the `assets/` folder and link them here)*

![Dashboard Preview](https://via.placeholder.com/800x450.png?text=AI+Content+Pipeline+Dashboard)

**Live Demo**: Coming Soon

---

## 📅 Roadmap

- [ ] **Multi-Model Support**: Integration with GPT-4o and Claude 3.5 Sonnet.
- [ ] **Image Generation**: Auto-generating cover images using DALL-E 3 or Midjourney.
- [ ] **Direct Publishing**: One-click export to WordPress, Medium, or Ghost.
- [ ] **Custom Style Voice**: Allow users to upload "Brand Style Guides" for the writer agent.
- [ ] **Analytics Dashboard**: Track content performance and SEO metrics over time.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate tests.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [CrewAI](https://www.crewai.com/) for the multi-agent orchestration framework
- [DeepSeek](https://www.deepseek.com/) for the powerful LLM
- [Streamlit](https://streamlit.io/) for the beautiful UI framework

---

**Built with ❤️ by [Ismail](https://github.com/Ismail-2001)**

⭐ **Star this repo if you find it useful!**
