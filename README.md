# GitGrade AI 🚀
### AI-Powered GitHub Repository Evaluation System

GitGrade AI is an intelligent system that analyzes a public GitHub repository and converts it into a **Score**, **Written Summary**, and **Personalized Improvement Roadmap** — similar to how a recruiter or senior engineer would evaluate code.

---

## 🎯 Problem Statement
Students build projects on GitHub but often don’t know:
- How good their code looks to recruiters
- What is missing in structure, tests, or documentation
- How to improve in a structured way

GitGrade AI acts as a **Repository Mirror**, reflecting real strengths and weaknesses based purely on repository data.

---

## 🧠 How It Works
1. User submits a GitHub repository URL
2. System fetches public repository data using GitHub APIs
3. Code, commits, structure, and documentation are analyzed
4. AI generates:
   - Score (0–100 + level)
   - Recruiter-style summary
   - Personalized improvement roadmap
5. Optional: PDF report & developer badge

---

## 📊 Evaluation Dimensions
| Dimension | Weight |
|--------|--------|
| Code Quality & Readability | 25 |
| Project Structure | 15 |
| Documentation | 15 |
| Testing & Maintainability | 15 |
| Git Practices | 15 |
| Real-world Relevance | 15 |

---

## 🛠️ Tech Stack
**Frontend**
- Next.js
- Tailwind CSS
- ShadCN UI

**Backend**
- FastAPI (Python)
- GitHub REST API
- Radon (Code complexity)
- OpenAI / LLM API

---

## 🤖 Role of AI
AI is used to:
- Convert raw metrics into human-readable feedback
- Generate mentor-like summaries
- Create actionable, personalized roadmaps

AI does **not** guess scores — scoring is rule-based and transparent.

---

## 📄 Features
- GitHub repo analysis
- Score & skill level (Beginner / Intermediate / Advanced)
- AI-generated evaluation summary
- Personalized roadmap
- PDF report export
- Developer skill badge

---

## 🎥 Demo
📹 Screen recording included in submission  
Shows:
- Repo input
- Analysis
- Score, summary, roadmap
- PDF export

---

## 🚀 Future Scope
- Resume integration
- Recruiter dashboards
- College-level analytics
- Open-source contribution scoring

---

## 🚦 Deployment & Running

### Backend
```bash
cd backend
pip install -r requirements.txt
# Set GITHUB_TOKEN and OPENAI_API_KEY in .env or environment
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
# Open http://localhost:3000
```
