<div align="center">

<img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Sentence--Transformers-ML-orange?style=for-the-badge&logo=huggingface&logoColor=white"/>
<img src="https://img.shields.io/badge/ReportLab-PDF-0052CC?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>

# 🤖 AI Resume Tailoring System — Elite Edition

### *ML/DL-Powered Resume Analysis • Semantic Matching • ATS Optimization • Multi-Template PDF & DOCX Export*

> **Stop submitting generic resumes. Let AI tailor your resume to every job description — in seconds.**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![GitHub](https://img.shields.io/badge/GitHub-summaiyazafar-181717?style=for-the-badge&logo=github)](https://github.com/summaiyazafar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Summaiya%20Bibi-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/summaiya-bibi/)

</div>

---

## 📌 Table of Contents

- [✨ What This System Does](#-what-this-system-does)
- [🚀 Key Features](#-key-features)
- [🧠 How It Works — AI Pipeline](#-how-it-works--ai-pipeline)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Tech Stack](#️-tech-stack)
- [📦 Installation & Local Setup](#-installation--local-setup)
- [☁️ Deploy on Streamlit Cloud (Free)](#️-deploy-on-streamlit-cloud-free)
- [🎨 Resume Templates](#-resume-templates)
- [📊 ATS Scoring System](#-ats-scoring-system)
- [🔒 Data Privacy & Protection Policy](#-data-privacy--protection-policy)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ What This System Does

The **AI Resume Tailoring System** is a full-stack, production-grade AI web application built by **Summaiya Bibi** (BS Computer Science). It analyzes your existing resume against any Job Description (JD) and automatically generates a perfectly tailored, ATS-optimized version — complete with professional PDF and DOCX exports, a customized cover letter, and a personalized interview preparation guide.

This is **not a simple keyword stuffing tool**. It uses real ML/NLP models:

- 🧠 **Sentence Transformers** for deep semantic similarity scoring
- 🔍 **Custom NLP skill extraction** engine with 300+ recognized technical skills
- 📊 **Hybrid ATS scoring** (40% keyword match + 60% semantic embedding similarity)
- 🔒 **Protected field architecture** — personal data is **never fabricated or modified**

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| 📤 **Resume Upload** | Parse and analyze PDF, DOCX, or TXT resumes with intelligent section extraction |
| 🧠 **Semantic AI Matching** | Uses `sentence-transformers` to compute deep NLP similarity between resume and JD |
| 🎯 **ATS Score Dashboard** | Live ATS match %, semantic score %, hard skill overlap %, and interview likelihood |
| ✂️ **Intelligent Tailoring** | Auto-rewrites your professional summary and re-orders skills to align with the JD |
| 🔍 **Skill Gap Analysis** | Visually highlights which skills you have ✅ and which are missing ⚠️ from the JD |
| 📄 **Multi-Format Export** | Download your tailored resume as **PDF**, **DOCX**, or **plain TXT** |
| 🎨 **4 Premium Templates** | Choose from 4 designer resume themes with live HTML preview |
| ✉️ **Cover Letter Generator** | Auto-generates a customized 3-paragraph cover letter aligned to your strengths and the JD |
| 💡 **Interview Prep Guide** | Generates personalized interview talking points, strength framing, and gap bridge strategies |
| 🔒 **Data Protection** | Personal info (name, email, phone, LinkedIn, education) is ALWAYS preserved exactly |
| ⚡ **One-Click Test Profiles** | Built-in AI/ML Engineer and Data Analyst sample profiles for instant testing |

---

## 🧠 How It Works — AI Pipeline

```
📄 Resume (PDF/DOCX/TXT)          📋 Job Description (JD)
          │                                    │
          ▼                                    ▼
  ┌───────────────────┐              ┌──────────────────────┐
  │   Resume Parser   │              │     JD Analyzer      │
  │  (pypdf / docx)   │              │  (Keyword + NLP)     │
  └────────┬──────────┘              └──────────┬───────────┘
           │                                    │
           ▼                                    ▼
  ┌────────────────────────────────────────────────────┐
  │             Skill Extractor & Comparator           │
  │  • Extracts 300+ technical skills from both docs   │
  │  • Computes keyword overlap score (40% weight)     │
  └────────────────────────┬───────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────┐
  │           Semantic Matcher (AI Embedding)          │
  │  • sentence-transformers/all-MiniLM-L6-v2          │
  │  • Cosine similarity between resume & JD vectors   │
  │  • Semantic score (60% weight)                     │
  └────────────────────────┬───────────────────────────┘
                           │
                           ▼
  ┌────────────────────────────────────────────────────┐
  │              Resume Tailor Engine                  │
  │  • Rewrites professional summary for the JD        │
  │  • Re-ranks and categorizes skills                 │
  │  • Re-orders experience bullets by relevance       │
  │  • Preserves ALL protected personal fields         │
  └────────────────────────┬───────────────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         📄 PDF        📝 DOCX       📋 TXT
     (ReportLab)   (python-docx)  (plain text)
```

**Final Composite ATS Score Formula:**
```
Final ATS Score = (Keyword Match × 0.40) + (Semantic Similarity × 0.60)
```

---

## 🗂️ Project Structure

```
AI-Resume-Tailoring-System/
│
├── app.py                          # 🚀 Main Streamlit application (1024 lines)
├── requirements.txt                # 📦 All Python dependencies
├── .gitignore                      # 🔒 Excludes .env, .venv, output files
│
├── modules/                        # 🧠 Core AI/ML engine modules
│   ├── __init__.py
│   ├── resume_parser.py            # PDF/DOCX/TXT extraction & section detection
│   ├── jd_analyzer.py              # Job description keyword & requirement extraction
│   ├── skill_extractor.py          # 300+ skill recognition & comparison engine
│   ├── semantic_matcher.py         # Sentence Transformer embedding similarity
│   ├── matcher.py                  # Hybrid scoring orchestrator (keyword + semantic)
│   ├── resume_tailor.py            # AI resume rewriting & optimization engine
│   ├── gap_analyzer.py             # Skill gap detection & recommendations
│   ├── pdf_generator.py            # ReportLab multi-template PDF generator
│   ├── resume_generator.py         # python-docx DOCX generator
│   ├── template_engine.py          # 4 HTML/CSS live preview templates
│   ├── ml_trainer.py               # ML feature engineering & model training
│   ├── ml_feature_engineering.py   # Feature extraction utilities
│   ├── ranking_engine.py           # Resume ranking algorithms
│   └── data_preprocessor.py        # Text normalization & preprocessing
│
├── templates/                      # Resume HTML/CSS template assets
├── assets/                         # Static assets (fonts, icons)
├── data/                           # Data & model artifacts
├── models/                         # Trained ML model files
└── output/                         # Generated resume downloads (gitignored)
```

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend / UI** | Streamlit 1.30+ | Interactive web application |
| **PDF Generation** | ReportLab 4.0+ | Professional multi-template PDF output |
| **DOCX Generation** | python-docx 1.0+ | Word document resume export |
| **NLP / Embeddings** | sentence-transformers | Semantic similarity scoring |
| **Resume Parsing** | pypdf + pdfplumber | PDF text extraction |
| **ML / Matching** | scikit-learn, NumPy | Cosine similarity, feature engineering |
| **Data Handling** | pandas, NumPy | Data processing pipelines |
| **Config** | python-dotenv | Environment variable management |
| **UI Enhancement** | Pillow, Rich | Image processing & logging |

---

## 📦 Installation & Local Setup

### Prerequisites

- Python **3.9 or higher**
- pip package manager
- (Optional) Git for cloning

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Tailoring-System.git
cd AI-Resume-Tailoring-System
```

### Step 2 — Create a Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ **Note:** The first run will auto-download the `sentence-transformers` model (~90MB). Ensure you have an internet connection.

### Step 4 — Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Add any API keys here if you integrate external LLM APIs (optional)
# OPENAI_API_KEY=your_key_here
# GEMINI_API_KEY=your_key_here
```

### Step 5 — Run the Application

```bash
streamlit run app.py
```

The app will open automatically at **`http://localhost:8501`**

---

## ☁️ Deploy on Streamlit Cloud (Free)   Complete App:https://ai-resume-tailoring-system-brw4pxqbja3puc9rnnstky.streamlit.app/

Deploy this project publicly in **under 5 minutes** — completely free:

1. **Push your code to GitHub** (see [GitHub Setup Guide](https://docs.github.com/en/get-started))
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub
3. Click **"New App"** and fill in:
   - **Repository:** `YOUR_USERNAME/AI-Resume-Tailoring-System`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **"Advanced Settings"** → **"Secrets"** and add your `.env` variables if needed
5. Click **"Deploy"** — your app goes live in ~2 minutes! 🚀

> 💡 **Streamlit Community Cloud is 100% free** for public repositories and provides a shareable public URL for your app.

---

## 🎨 Resume Templates

The system includes **4 professionally designed resume templates**, each optimized for different industries and purposes:

| Template | Style | Best For |
|---|---|---|
| 👔 **Modern Executive** | Navy / Royal Blue accents, Inter font | Leadership, Management, Business roles |
| 🏛️ **Harvard ATS Classic** | Clean monochrome, Georgia serif font | Maximum ATS compliance (Workday, Taleo) |
| ⚡ **Silicon Valley Tech** | Teal / Cyan accents, Outfit font, skill chips | AI/ML, Software Engineering, Tech startups |
| 🎨 **Creative Indigo** | Deep Indigo / Violet, Plus Jakarta Sans | Data Science, Consulting, Design-adjacent |

Each template renders as:
- **Live HTML preview** inside the app (interactive, scrollable)
- **Downloadable PDF** using the exact same design system
- **DOCX** for further manual editing in Microsoft Word

---

## 📊 ATS Scoring System

The system computes a **multi-dimensional ATS score** to evaluate how well your resume matches a Job Description:

```
┌─────────────────────────────────────────────────────────┐
│  Score Component        │  Weight  │  Method            │
├─────────────────────────┼──────────┼────────────────────┤
│  Hard Skill Overlap     │   40%    │  Keyword matching  │
│  Semantic AI Score      │   60%    │  Embedding cosine  │
└─────────────────────────┴──────────┴────────────────────┘
```

**Score Interpretation:**

| Score Range | Label | Meaning |
|---|---|---|
| ≥ 85% | 🌟 Top-Tier Match | Exceptional fit — very high callback probability |
| ≥ 70% | ✅ Strong Match | High interview probability |
| ≥ 55% | 👍 Good Match | Competitive candidate — minor tailoring suggested |
| ≥ 40% | ⚠️ Moderate Match | Needs tailoring — specific skill gaps identified |
| < 40% | ❌ Low Match | Significant skill gap — focus on gap analysis |

---

## 🔒 Data Privacy & Protection Policy

This system strictly enforces a **Candidate Protection Policy**:

- ✅ **Protected fields are NEVER modified:** Name, email, phone, LinkedIn, GitHub, Kaggle, location, education, certifications
- ✅ **No hallucination:** The AI will never invent skills, jobs, or credentials you don't have
- ✅ **Gap reporting, not fabrication:** Missing JD skills are shown as recommendations, never added to your resume automatically
- ✅ **Local processing:** All data is processed locally on your machine or Streamlit Cloud — no data is sent to third-party AI APIs
- ✅ **No data storage:** Output files are temporary and cleaned up automatically

---

## 📁 Output Files

After generating your tailored resume, the following files are available for download:

| Format | Description |
|---|---|
| `Tailored_Resume_[Name].pdf` | Professional PDF with your chosen template design |
| `Tailored_Resume_[Name].docx` | Editable Microsoft Word document |
| `Tailored_Resume_[Name].txt` | ATS-safe plain text version |
| `Cover_Letter_[Name].txt` | Tailored 3-paragraph cover letter |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repository, then:
git clone https://github.com/YOUR_USERNAME/AI-Resume-Tailoring-System.git
git checkout -b feature/your-feature-name

# Make your changes, then:
git add .
git commit -m "feat: describe your change clearly"
git push origin feature/your-feature-name
# Open a Pull Request on GitHub
```

**Ideas for contributions:**
- 🌐 Add support for more resume languages / locales
- 🤖 Integrate LLM APIs (Gemini, GPT-4) for enhanced summary rewriting
- 📊 Add Radar Chart visualization for skill gap analysis
- 🎨 Design new resume templates
- 🧪 Add unit tests for ML modules

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

**Built with ❤️ by [Summaiya Bibi](https://github.com/summaiyazafar)**

🎓 BS Computer Science | AI/ML Engineer | Pakistan

[![GitHub](https://img.shields.io/badge/GitHub-summaiyazafar-181717?style=flat-square&logo=github)](https://github.com/summaiyazafar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Summaiya%20Bibi-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/summaiya-bibi/)

*If this project helped you land your dream job — give it a ⭐ on GitHub!*

[![GitHub Stars](https://img.shields.io/github/stars/summaiyazafar/AI-Resume-Tailoring-System?style=social)](https://github.com/summaiyazafar/AI-Resume-Tailoring-System)
[![GitHub Forks](https://img.shields.io/github/forks/summaiyazafar/AI-Resume-Tailoring-System?style=social)](https://github.com/summaiyazafar/AI-Resume-Tailoring-System)

</div>
