"""
================================================================================
AI Resume Tailoring System – Production Edition
================================================================================
ML/DL-powered Resume Analysis, Semantic Matching, ATS Optimization,
Skill Gap Analysis, Multi-Template PDF & DOCX Generation, and Interview Guide.
"""

import os
import sys
import tempfile
import re
from pathlib import Path
from datetime import datetime
import streamlit as st

# ============================================================
# PROJECT CONFIGURATION & PATH SETUP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume Tailoring System – Elite Edition",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# MODULE IMPORTS WITH ROBUST ERROR HANDLING
# ============================================================

try:
    from modules.resume_parser import ResumeParser
except Exception as e:
    st.error(f"❌ ResumeParser import failed: {e}")
    st.stop()

try:
    from modules.jd_analyzer import JDAnalyzer
except Exception as e:
    st.error(f"❌ JDAnalyzer import failed: {e}")
    st.stop()

try:
    from modules.skill_extractor import extract_skills, compare_skills
except Exception as e:
    st.error(f"❌ Skill extractor import failed: {e}")
    st.stop()

try:
    from modules.matcher import ResumeJobMatcher
except Exception as e:
    st.error(f"❌ Matcher import failed: {e}")
    st.stop()

try:
    from modules.resume_tailor import ResumeTailor
except Exception as e:
    st.error(f"❌ ResumeTailor import failed: {e}")
    st.stop()

try:
    from modules.pdf_generator import PDFResumeGenerator, TEMPLATE_PALETTES
except Exception as e:
    PDFResumeGenerator = None
    TEMPLATE_PALETTES = {}

try:
    from modules.resume_generator import ResumeGenerator
except Exception as e:
    ResumeGenerator = None

try:
    from modules.template_engine import AVAILABLE_TEMPLATES, render_html_preview
except Exception as e:
    AVAILABLE_TEMPLATES = {}
    render_html_preview = None

# ============================================================
# SAMPLE MASTER PROFILES FOR ZERO-FRICTION TESTING
# ============================================================

SAMPLE_PROFILES = {
    "AI/ML Engineer": {
        "name": "Summaiya Bibi",
        "phone": "+92 346 6577540",
        "email": "summaiya.ai@gmail.com",
        "location": "Islamabad, Pakistan",
        "linkedin": "https://linkedin.com/in/summaiya-ai",
        "github": "https://github.com/summaiya-ai",
        "kaggle": "https://kaggle.com/summaiya-ai",
        "education": "BS Computer Science — Virtual University of Pakistan (2021 – 2025)",
        "certifications": "• Deep Learning Specialization (DeepLearning.AI)\n• AWS Certified Machine Learning Specialty\n• Generative AI & LLMs in Production",
        "summary": "AI/ML Engineer with 3+ years of experience developing predictive machine learning models, natural language processing (NLP) pipelines, and generative AI systems using Python, PyTorch, and HuggingFace. Proven track record of improving inference speeds by 40% and deploying scalable models with Docker and FastAPI.",
        "skills": [
            "Python", "PyTorch", "TensorFlow", "Scikit-Learn", "NLP", "Large Language Models",
            "LangChain", "RAG", "HuggingFace", "FastAPI", "Docker", "AWS", "SQL", "Pandas",
            "NumPy", "MLOps", "Git", "Streamlit"
        ],
        "experience": [
            {
                "title": "AI/ML Engineer",
                "company": "Cognitive AI Solutions",
                "location": "Islamabad, Pakistan",
                "dates": "2024 – Present",
                "bullets": [
                    "Architected and deployed an end-to-end Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and Llama 3, boosting internal knowledge retrieval accuracy by 42%.",
                    "Fine-tuned Transformer models (BERT, RoBERTa) for multi-class intent classification, achieving an F1-score of 0.94 across 50,000+ customer records.",
                    "Engineered low-latency RESTful APIs using FastAPI and Docker, orchestrating model deployments with 99.8% uptime on AWS EC2.",
                    "Collaborated with cross-functional engineering teams to automate CI/CD pipeline for automated model evaluation and data drift monitoring."
                ]
            },
            {
                "title": "AI Developer",
                "company": "DataTech Analytics",
                "location": "Rawalpindi, Pakistan",
                "dates": "2022 – 2024",
                "bullets": [
                    "Developed and evaluated predictive machine learning models using Scikit-Learn and XGBoost for customer churn prediction, reducing churn by 18%.",
                    "Performed exploratory data analysis (EDA) and automated feature engineering pipelines across tabular datasets of over 2M records using Pandas and NumPy.",
                    "Built interactive real-time data visualization dashboards in Streamlit to present model inference insights to executive stakeholders."
                ]
            }
        ],
        "projects": [
            {
                "name": "Enterprise Document QA System (RAG Pipeline)",
                "description": "Engineered an AI-powered conversational document intelligence platform indexing thousands of technical PDFs with semantic search and citation verification.",
                "technologies": ["Python", "LangChain", "PyTorch", "ChromaDB", "FastAPI", "Docker"]
            },
            {
                "name": "Automated Medical Text Entity Extraction",
                "description": "Trained custom Named Entity Recognition (NER) models using SpaCy and Transformers to extract critical diagnostic entities from clinical notes with 91% precision.",
                "technologies": ["Python", "HuggingFace", "SpaCy", "Scikit-Learn", "Streamlit"]
            }
        ]
    },
    "Data Analyst": {
        "name": "Ayesha Malik",
        "phone": "+92 300 7654321",
        "email": "ayesha.malik.ds@gmail.com",
        "location": "Lahore, Pakistan",
        "linkedin": "https://linkedin.com/in/ayesha-malik-ds",
        "github": "https://github.com/ayeshamalik-ds",
        "kaggle": "https://kaggle.com/ayeshamalik-ds",
        "education": "BS Data Science — FAST NUCES (2020 – 2024)",
        "certifications": "• Microsoft Certified: Power BI Data Analyst Associate\n• Google Advanced Data Analytics Professional Certificate",
        "summary": "Data Analyst and Business Intelligence Specialist with expertise in predictive analytics, SQL querying, statistical hypothesis testing, and interactive dashboard engineering in Power BI and Tableau. Experienced in transforming raw transactional data into actionable growth strategies.",
        "skills": [
            "Python", "SQL", "Power BI", "Tableau", "Pandas", "NumPy", "Scikit-Learn",
            "Statistical Analysis", "A/B Testing", "Data Modeling", "DAX", "ETL Pipelines",
            "Excel", "PostgreSQL", "Machine Learning"
        ],
        "experience": [
            {
                "title": "Data Analyst",
                "company": "Apex Financial Analytics",
                "location": "Lahore, Pakistan",
                "dates": "2023 – Present",
                "bullets": [
                    "Formulated statistical predictive models and risk scoring algorithms using Python, Pandas, and Scikit-Learn, cutting default risk by 15%.",
                    "Constructed scalable automated ETL workflows in PostgreSQL and Python, reducing report generation latency from 4 hours to 15 minutes.",
                    "Designed executive-level Power BI reporting suites and DAX measures tracking $20M+ in quarterly revenues."
                ]
            }
        ],
        "projects": [
            {
                "name": "E-Commerce Customer Lifetime Value (CLV) Engine",
                "description": "Implemented segmentation algorithms (RFM Analysis & K-Means clustering) to forecast CLV and optimize targeted promotional campaigns.",
                "technologies": ["Python", "Scikit-Learn", "SQL", "Power BI", "Pandas"]
            }
        ]
    }
}

SAMPLE_JOB_DESCRIPTION = """Machine Learning Engineer
Company: Global AI Technologies Inc.
Location: Remote / Hybrid

Job Summary:
We are seeking an exceptional Machine Learning Engineer to join our high-velocity AI product division. In this role, you will architect, train, and deploy state-of-the-art predictive models, NLP systems, and LLM-driven applications. You will work closely with data scientists and software engineers to scale machine learning pipelines from experimentation to production.

Responsibilities:
• Design, implement, and maintain production-grade machine learning and deep learning pipelines.
• Build Retrieval-Augmented Generation (RAG) workflows and fine-tune large language models (LLMs) for domain-specific automation.
• Develop high-performance, asynchronous REST APIs (FastAPI) for model serving and real-time inference.
• Optimize inference latency, throughput, and GPU utilization in containerized microservices (Docker, Kubernetes).
• Implement robust MLOps practices including model monitoring, CI/CD automation, and data versioning on AWS or GCP.
• Collaborate with cross-functional product teams to translate business problems into high-impact AI solutions.

Required Qualifications & Skills:
• 2+ years of professional software engineering and machine learning experience.
• Strong programming mastery in Python and deep learning frameworks (PyTorch or TensorFlow).
• Proven hands-on experience with Natural Language Processing (NLP), Transformers, HuggingFace, and LangChain.
• Strong foundation in traditional machine learning algorithms (Scikit-Learn, XGBoost, Regression, Clustering).
• Demonstrated experience building and deploying containerized applications with Docker and FastAPI.
• Solid background in SQL, relational databases (PostgreSQL), and cloud infrastructure (AWS or GCP).
• Excellent communication skills and a passion for engineering high-quality, measurable AI systems.

Preferred Qualifications:
• Experience with Vector Databases (ChromaDB, Pinecone, FAISS).
• Familiarity with MLOps tracking tools (MLflow, Weights & Biases) and CI/CD pipelines.
• Bachelor’s or Master’s degree in Computer Science, Data Science, or related engineering discipline.
"""

# ============================================================
# STREAMLIT CACHING
# ============================================================

@st.cache_resource
def get_matcher():
    return ResumeJobMatcher()

@st.cache_resource
def get_tailor():
    return ResumeTailor()

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clean_text(value):
    if value is None:
        return ""
    return str(value).strip()

def safe_list(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return [clean_text(x) for x in value if clean_text(x)]
    if isinstance(value, str):
        return [clean_text(x) for x in value.splitlines() if clean_text(x)]
    return [clean_text(value)] if clean_text(value) else []

def normalize_score(value):
    try:
        v = float(value)
        if 0 <= v <= 1:
            v *= 100
        return max(0.0, min(100.0, v))
    except:
        return 0.0

def get_match_level_label(score):
    s = normalize_score(score)
    if s >= 85:
        return "🌟 Top-Tier Match (Exceptional Fit)"
    if s >= 70:
        return "✅ Strong Match (High Interview Probability)"
    if s >= 55:
        return "👍 Good Match (Competitive Candidate)"
    if s >= 40:
        return "⚠️ Moderate Match (Needs Minor Tailoring)"
    return "❌ Low Match (Significant Skill Gap)"

# ============================================================
# CUSTOM UI CSS (Clean, Modern, Aesthetic)
# ============================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F3356 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
    }
    .hero-badge-wrap {
        display: flex;
        gap: 10px;
        margin-bottom: 12px;
    }
    .hero-badge {
        background: rgba(59, 130, 246, 0.2);
        color: #93C5FD;
        border: 1px solid rgba(59, 130, 246, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .hero-title {
        color: #FFFFFF;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0 0 6px 0;
    }
    .hero-subtitle {
        color: #94A3B8;
        font-size: 1rem;
        margin: 0;
        line-height: 1.5;
    }

    /* Cards */
    .stat-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
    }
    .stat-label {
        color: #64748B;
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 6px;
    }
    .stat-val {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0F172A;
    }
    .stat-val.high { color: #16A34A; }
    .stat-val.med { color: #2563EB; }
    .stat-val.low { color: #D97706; }

    /* Policy Box */
    .policy-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-left: 4px solid #3B82F6;
        border-radius: 10px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
    }
    .policy-title {
        color: #1E3A8A;
        font-weight: 700;
        font-size: 0.92rem;
        margin-bottom: 4px;
    }
    .policy-text {
        color: #475569;
        font-size: 0.85rem;
        line-height: 1.45;
    }

    /* Template Cards in Sidebar */
    .template-card {
        padding: 10px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
        border: 1px solid #E2E8F0;
        background: #FFFFFF;
    }
    .template-card.active {
        border-color: #2563EB;
        background: #EFF6FF;
    }

    /* Skills Badge Container */
    .chips-wrap {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 6px;
    }
    .chip-matched {
        background: #DCFCE7;
        color: #15803D;
        border: 1px solid #86EFAC;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }
    .chip-missing {
        background: #FEF3C7;
        color: #B45309;
        border: 1px solid #FCD34D;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
    }

    /* Section Subheaders */
    .custom-sec-header {
        font-size: 1.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Button Primary Styling */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
        transition: all 0.2s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
        transform: translateY(-1px);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero-container">
    <div class="hero-badge-wrap">
        <span class="hero-badge">⚡ PRODUCTION RESUME AI</span>
        <span class="hero-badge">🎯 ATS OPTIMIZED</span>
        <span class="hero-badge">🎨 4 CURATED TEMPLATES</span>
    </div>
    <h1 class="hero-title">AI Resume Tailoring & Generation System</h1>
    <p class="hero-subtitle">
        Automatically tailor, structure, and format your resume for any Job Description with high ATS match scores,
        action-oriented impact metrics, multi-template PDF exports, and customized interview preparation.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR – TEMPLATE SELECTOR & PROTECTED INFORMATION
# ============================================================

with st.sidebar:
    st.markdown("### 🎨 Select Resume Template")
    st.caption("Choose your visual presentation theme. Both the live preview and the downloaded PDF will reflect this styling.")

    template_options = {
        "modern_executive": "👔 Modern Executive (Navy / Royal)",
        "harvard_ats": "🏛️ Harvard ATS Classic (Monochrome)",
        "silicon_valley": "⚡ Silicon Valley Tech (Teal / Cyan)",
        "creative_indigo": "🎨 Creative Indigo (Deep Indigo)"
    }

    selected_template = st.radio(
        "Choose Design Template",
        options=list(template_options.keys()),
        format_func=lambda x: template_options[x],
        index=0,
        label_visibility="collapsed"
    )

    tmpl_info = AVAILABLE_TEMPLATES.get(selected_template, {})
    if tmpl_info:
        st.markdown(f"""
        <div style="background:{tmpl_info['accent_bg']};border:1px solid {tmpl_info['border_color']};border-radius:10px;padding:8px 12px;margin:8px 0 16px 0;">
            <div style="color:{tmpl_info['primary_color']};font-weight:700;font-size:0.85rem;">{tmpl_info['badge']}</div>
            <div style="color:#475569;font-size:0.78rem;">{tmpl_info['description']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### 🔒 Protected Candidate Info")
    st.caption("Personal details & verified credentials. AI will NEVER fabricate or alter these fields.")

    # Check session state for preloaded profile
    if "p_name" not in st.session_state:
        st.session_state["p_name"] = "Summaiya Bibi"
        st.session_state["p_phone"] = "+92 346 6577540"
        st.session_state["p_email"] = "summaiya.ai@gmail.com"
        st.session_state["p_loc"] = "Islamabad, Pakistan"
        st.session_state["p_linkedin"] = "https://linkedin.com/in/summaiya-ai"
        st.session_state["p_github"] = "https://github.com/summaiya-ai"
        st.session_state["p_kaggle"] = "https://kaggle.com/summaiya-ai"
        st.session_state["p_edu"] = "BS Computer Science — Virtual University of Pakistan (2021 – 2025)"
        st.session_state["p_certs"] = "• Deep Learning Specialization (DeepLearning.AI)\n• AWS Certified Machine Learning Specialty"

    side_name = st.text_input("Full Name", value=st.session_state["p_name"], key="sb_name")
    side_phone = st.text_input("Phone Number", value=st.session_state["p_phone"], key="sb_phone")
    side_email = st.text_input("Email Address", value=st.session_state["p_email"], key="sb_email")
    side_loc = st.text_input("Location", value=st.session_state["p_loc"], key="sb_loc")
    side_linkedin = st.text_input("LinkedIn Profile URL", value=st.session_state["p_linkedin"], key="sb_li")
    side_github = st.text_input("GitHub URL", value=st.session_state["p_github"], key="sb_gh")
    side_kaggle = st.text_input("Kaggle / Portfolio URL", value=st.session_state["p_kaggle"], key="sb_kg")
    side_edu = st.text_area("Education Details", value=st.session_state["p_edu"], height=80, key="sb_edu")
    side_certs = st.text_area("Certifications & Honors", value=st.session_state["p_certs"], height=80, key="sb_certs")

# ============================================================
# MAIN INPUT SECTION
# ============================================================

st.markdown('<div class="custom-sec-header">1️⃣ Master Resume / Candidate Profile</div>', unsafe_allow_html=True)

input_tab1, input_tab2 = st.tabs(["📤 Upload Existing Resume (PDF / DOCX)", "⚡ One-Click Master Profiles (Instant Test)"])

uploaded_resume_file = None
selected_master_profile = None

with input_tab1:
    uploaded_resume_file = st.file_uploader(
        "Upload your master resume (PDF, DOCX, or TXT)",
        type=["pdf", "docx", "txt"],
        help="The system will extract your text, match keywords, and optimize it."
    )
    if uploaded_resume_file:
        st.success(f"📄 Loaded file: **{uploaded_resume_file.name}**")

with input_tab2:
    st.caption("Don't have a PDF ready? Select a realistic, fully-formed candidate profile to test immediately:")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        if st.button("🧠 Load AI/ML Engineer Profile", use_container_width=True):
            prof = SAMPLE_PROFILES["AI/ML Engineer"]
            st.session_state["active_profile"] = prof
            st.session_state["p_name"] = prof["name"]
            st.session_state["p_phone"] = prof["phone"]
            st.session_state["p_email"] = prof["email"]
            st.session_state["p_loc"] = prof["location"]
            st.session_state["p_linkedin"] = prof["linkedin"]
            st.session_state["p_github"] = prof["github"]
            st.session_state["p_kaggle"] = prof["kaggle"]
            st.session_state["p_edu"] = prof["education"]
            st.session_state["p_certs"] = prof["certifications"]
            st.rerun()

    with col_p2:
        if st.button("📊 Load Data Analyst Profile", use_container_width=True):
            prof = SAMPLE_PROFILES["Data Analyst"]
            st.session_state["active_profile"] = prof
            st.session_state["p_name"] = prof["name"]
            st.session_state["p_phone"] = prof["phone"]
            st.session_state["p_email"] = prof["email"]
            st.session_state["p_loc"] = prof["location"]
            st.session_state["p_linkedin"] = prof["linkedin"]
            st.session_state["p_github"] = prof["github"]
            st.session_state["p_kaggle"] = prof["kaggle"]
            st.session_state["p_edu"] = prof["education"]
            st.session_state["p_certs"] = prof["certifications"]
            st.rerun()

    if "active_profile" in st.session_state:
        st.info(f"✅ Active Test Profile: **{st.session_state['active_profile']['name']}** ({len(st.session_state['active_profile']['skills'])} verified skills, {len(st.session_state['active_profile']['experience'])} roles)")

st.markdown('<div class="custom-sec-header">2️⃣ Target Job Description (JD)</div>', unsafe_allow_html=True)

col_jd_top1, col_jd_top2 = st.columns([3, 1])
with col_jd_top2:
    if st.button("⚡ Load Sample AI/ML JD", use_container_width=True, help="Load a real-world AI/ML Engineer job posting"):
        st.session_state["jd_input_text"] = SAMPLE_JOB_DESCRIPTION
        st.rerun()

default_jd = st.session_state.get("jd_input_text", SAMPLE_JOB_DESCRIPTION)
job_description = st.text_area(
    "Paste the target Job Description (JD) here:",
    value=default_jd,
    height=200,
    placeholder="Paste the complete job description from LinkedIn, Indeed, Glassdoor, etc."
)

st.markdown("""
<div class="policy-box">
    <div class="policy-title">🔒 Candidate Protection & Truth-in-Resume Guarantee</div>
    <div class="policy-text">
        Our tailoring engine guarantees that your verified personal information, contact handles, education, and dates are preserved 100% intact. Missing JD skills are reported separately as gap analysis recommendations — never hallucinated on your resume.
    </div>
</div>
""", unsafe_allow_html=True)

# Main Action Button
start_tailoring = st.button("🚀 Analyze & Generate Tailored Resume", type="primary", use_container_width=True)

# ============================================================
# TAILORING PIPELINE
# ============================================================

if start_tailoring:
    if uploaded_resume_file is None and "active_profile" not in st.session_state:
        st.error("⚠️ Please either upload a resume file (PDF/DOCX) or load a sample master profile above.")
        st.stop()
    if not job_description.strip():
        st.error("⚠️ Please provide a Job Description.")
        st.stop()

    temp_path = None
    try:
        parsed_resume = {}
        resume_text = ""

        # Step 1: Parse candidate resume
        with st.status("🔍 Processing Resume & Job Description...", expanded=True) as status:
            if uploaded_resume_file is not None:
                st.write("📄 Parsing uploaded document...")
                suffix = Path(uploaded_resume_file.name).suffix.lower()
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as f:
                    f.write(uploaded_resume_file.getbuffer())
                    temp_path = f.name

                parser = ResumeParser()
                if hasattr(parser, "parse_resume"):
                    parsed_resume = parser.parse_resume(temp_path)
                else:
                    raw_extracted_text = parser.parse(temp_path)
                    parsed_resume = {"text": raw_extracted_text}

                resume_text = parsed_resume.get("text", "")
            else:
                st.write("👤 Using active candidate profile...")
                active = st.session_state["active_profile"]
                parsed_resume = {
                    "name": active["name"],
                    "phone": active["phone"],
                    "email": active["email"],
                    "location": active["location"],
                    "linkedin": active["linkedin"],
                    "github": active["github"],
                    "kaggle": active["kaggle"],
                    "education": active["education"],
                    "certifications": active["certifications"],
                    "summary": active["summary"],
                    "skills": active["skills"],
                    "experience": active["experience"],
                    "projects": active["projects"]
                }
                resume_text = f"{active['summary']}\n{' '.join(active['skills'])}\n"
                for exp in active["experience"]:
                    resume_text += f"{exp['title']} {exp['company']} {' '.join(exp['bullets'])}\n"
                for proj in active["projects"]:
                    resume_text += f"{proj['name']} {proj['description']} {' '.join(proj['technologies'])}\n"

            # Step 2: JD Analysis
            st.write("🧠 Analyzing Job Description requirements & keywords...")
            jd_analyzer = JDAnalyzer()
            jd_result = jd_analyzer.analyze(job_description) if hasattr(jd_analyzer, "analyze") else {}
            target_job_title = jd_result.get("job_title") or "AI/ML Engineer"

            # Step 3: Skill Comparison
            st.write("🎯 Extracting technical competencies & comparing skill overlap...")
            resume_skills = safe_list(extract_skills(resume_text))
            if not resume_skills and "skills" in parsed_resume:
                resume_skills = safe_list(parsed_resume["skills"])

            skill_comp = compare_skills(resume_text, job_description) or {}
            matched_skills = safe_list(skill_comp.get("matched_skills", []))
            missing_skills = safe_list(skill_comp.get("missing_skills", []))
            keyword_score = normalize_score(skill_comp.get("match_percentage", 0))

            # Step 4: Semantic Matching
            st.write("🔗 Calculating semantic alignment score...")
            matcher = get_matcher()
            match_result = matcher.match(resume_text, job_description) if hasattr(matcher, "match") else {}
            semantic_score = normalize_score(match_result.get("semantic_score", 0))
            ats_final_score = normalize_score(match_result.get("final_score", keyword_score))
            if ats_final_score == 0 and keyword_score > 0:
                ats_final_score = keyword_score

            match_level = get_match_level_label(ats_final_score)

            # Step 5: Resume Tailoring
            st.write("✨ Tailoring professional summary & aligning experience...")
            tailor = get_tailor()
            tailored = tailor.tailor(parsed_resume, jd_result, job_description)
            if not isinstance(tailored, dict):
                tailored = {}

            # Inject protected sidebar overrides
            tailored["name"] = side_name.strip() or tailored.get("name", "Candidate")
            tailored["phone"] = side_phone.strip() or tailored.get("phone", "")
            tailored["email"] = side_email.strip() or tailored.get("email", "")
            tailored["location"] = side_loc.strip() or tailored.get("location", "")
            tailored["linkedin"] = side_linkedin.strip() or tailored.get("linkedin", "")
            tailored["github"] = side_github.strip() or tailored.get("github", "")
            tailored["kaggle"] = side_kaggle.strip() or tailored.get("kaggle", "")
            tailored["education"] = side_edu.strip() or tailored.get("education", "")
            tailored["certifications"] = side_certs.strip() or tailored.get("certifications", "")
            tailored["job_title"] = target_job_title

            # Categorize skills for clean presentation
            candidate_raw_skills = tailored.get("skills", resume_skills)
            if isinstance(candidate_raw_skills, list):
                skills_categorized = tailor.categorize_skills(candidate_raw_skills)
                # Use categorized skills dict for PDF/DOCX/HTML rendering
                # (PDF generator and template engine both support dict format)
                if any(v for v in skills_categorized.values()):
                    tailored["skills"] = skills_categorized
            tailored["matched_skills"] = matched_skills
            tailored["missing_skills"] = missing_skills

            # Store in session state for persistence
            st.session_state["tailored_resume"] = tailored
            st.session_state["jd_result"] = jd_result
            st.session_state["ats_final_score"] = ats_final_score
            st.session_state["semantic_score"] = semantic_score
            st.session_state["keyword_score"] = keyword_score
            st.session_state["match_level"] = match_level
            st.session_state["matched_skills"] = matched_skills
            st.session_state["missing_skills"] = missing_skills

            status.update(label="🎉 Resume Tailoring & Optimization Complete!", state="complete", expanded=False)

    except Exception as e:
        st.error(f"❌ Error during resume processing: {e}")
        import traceback
        st.code(traceback.format_exc())
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except Exception:
                pass

# ============================================================
# RESULTS PRESENTATION SECTION
# ============================================================

if "tailored_resume" in st.session_state:
    tailored = st.session_state["tailored_resume"]
    jd_result = st.session_state["jd_result"]
    ats_score = st.session_state["ats_final_score"]
    semantic_score = st.session_state["semantic_score"]
    keyword_score = st.session_state["keyword_score"]
    match_level = st.session_state["match_level"]
    matched_skills = st.session_state["matched_skills"]
    missing_skills = st.session_state["missing_skills"]

    st.markdown("---")

    # Score Cards
    st.markdown('<div class="custom-sec-header">📊 Resume Performance & ATS Scorecard</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)

    score_cls = "high" if ats_score >= 70 else ("med" if ats_score >= 50 else "low")
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">🎯 Overall ATS Match</div>
            <div class="stat-val {score_cls}">{ats_score:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">🧠 Semantic AI Score</div>
            <div class="stat-val med">{semantic_score:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">🔍 Hard Skills Overlap</div>
            <div class="stat-val {'high' if keyword_score >= 60 else 'med'}">{keyword_score:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">📈 Interview Likelihood</div>
            <div style="font-size:1.15rem;font-weight:800;color:#0F172A;margin-top:6px;">{match_level}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 4 Dynamic Tabs for Output
    tab_resume, tab_gap, tab_cover, tab_prep = st.tabs([
        "📄 Tailored Resume & Downloads",
        "🎯 Skill Match & Gap Analysis",
        "✉️ Tailored Cover Letter",
        "💡 Interview Preparation Guide"
    ])

    # ----------------------------------------------------
    # TAB 1: TAILORED RESUME PREVIEW & DOWNLOADS
    # ----------------------------------------------------
    with tab_resume:
        st.markdown("### 📥 Download Your Tailored Resume")
        st.caption(f"Generating documents formatted with the **{template_options.get(selected_template, selected_template)}** template.")

        # Prepare Downloads
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        cand_name_slug = clean_text(tailored.get("name", "Candidate")).replace(" ", "_")

        # 1. PDF Generation
        pdf_bytes = None
        if PDFResumeGenerator is not None:
            try:
                pdf_gen = PDFResumeGenerator(output_folder=str(out_dir))
                pdf_path = out_dir / f"Tailored_Resume_{cand_name_slug}.pdf"
                pdf_gen.generate_pdf(tailored, filename=str(pdf_path.name), template=selected_template)
                if pdf_path.exists():
                    with open(pdf_path, "rb") as f:
                        pdf_bytes = f.read()
            except Exception as e:
                st.warning(f"⚠️ PDF generation note: {e}")

        # 2. DOCX Generation
        docx_bytes = None
        if ResumeGenerator is not None:
            try:
                docx_gen = ResumeGenerator()
                docx_path = out_dir / f"Tailored_Resume_{cand_name_slug}.docx"
                docx_gen.generate_docx(tailored, output_path=str(docx_path))
                if docx_path.exists():
                    with open(docx_path, "rb") as f:
                        docx_bytes = f.read()
            except Exception as e:
                pass

        # 3. TXT Generation
        txt_content = f"""================================================================================
                               TAILORED RESUME
================================================================================
Name        : {tailored.get('name', '')}
Title       : {tailored.get('job_title', '')}
Email       : {tailored.get('email', '')} | Phone: {tailored.get('phone', '')}
Location    : {tailored.get('location', '')}
LinkedIn    : {tailored.get('linkedin', '')}
GitHub      : {tailored.get('github', '')}
Kaggle      : {tailored.get('kaggle', '')}

PROFESSIONAL SUMMARY
--------------------------------------------------------------------------------
{tailored.get('professional_summary', '')}

SKILLS
--------------------------------------------------------------------------------
"""
        # Handle both dict (categorized) and list (flat) skills
        skills_data = tailored.get('skills', [])
        if isinstance(skills_data, dict):
            for cat, slist in skills_data.items():
                if slist:
                    txt_content += f"{cat}: {', '.join(slist)}\n"
        elif isinstance(skills_data, list):
            txt_content += ', '.join(str(s) for s in skills_data)
        txt_content += """

EXPERIENCE
--------------------------------------------------------------------------------
"""
        for exp in tailored.get("experience", []):
            if isinstance(exp, dict):
                txt_content += f"\n• {exp.get('title', '')} | {exp.get('company', '')} ({exp.get('dates', '')})\n"
                for b in exp.get("bullets", []):
                    txt_content += f"   - {b}\n"
            else:
                txt_content += f"• {exp}\n"

        txt_content += f"""
PROJECTS
--------------------------------------------------------------------------------
"""
        for proj in tailored.get("projects", []):
            if isinstance(proj, dict):
                txt_content += f"\n• {proj.get('name', '')}\n  {proj.get('description', '')}\n  Technologies: {', '.join(proj.get('technologies', []))}\n"
            else:
                txt_content += f"• {proj}\n"

        txt_content += f"""
EDUCATION
--------------------------------------------------------------------------------
{tailored.get('education', '')}

CERTIFICATIONS
--------------------------------------------------------------------------------
{tailored.get('certifications', '')}
"""

        # Action Buttons
        d_col1, d_col2, d_col3 = st.columns(3)
        with d_col1:
            if pdf_bytes:
                st.download_button(
                    label=f"📄 Download PDF ({template_options.get(selected_template, '').split('(')[0].strip()})",
                    data=pdf_bytes,
                    file_name=f"Tailored_Resume_{cand_name_slug}.pdf",
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
            else:
                st.button("📄 PDF Generator Loading...", disabled=True, use_container_width=True)

        with d_col2:
            if docx_bytes:
                st.download_button(
                    label="📝 Download Word Document (DOCX)",
                    data=docx_bytes,
                    file_name=f"Tailored_Resume_{cand_name_slug}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
            else:
                st.button("📝 DOCX Generator Initializing...", disabled=True, use_container_width=True)

        with d_col3:
            st.download_button(
                label="📋 Download Plain Text (TXT)",
                data=txt_content,
                file_name=f"Tailored_Resume_{cand_name_slug}.txt",
                mime="text/plain",
                use_container_width=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 👁️ Live Interactive Resume Preview")
        st.caption("Rendered live matching your chosen template colors, typography, and layout.")

        # Render HTML preview
        if render_html_preview:
            html_code = render_html_preview(tailored, template_id=selected_template)
            st.components.v1.html(html_code, height=950, scrolling=True)

    # ----------------------------------------------------
    # TAB 2: SKILL MATCH & GAP ANALYSIS
    # ----------------------------------------------------
    with tab_gap:
        st.markdown("### 🎯 Skill Match & Gap Analysis Breakdown")
        st.caption("Direct comparison between candidate technical competencies and target JD requirements.")

        g_col1, g_col2 = st.columns(2)
        with g_col1:
            st.markdown(f"#### ✅ Matched Skills ({len(matched_skills)})")
            st.caption("Skills you already have that directly match the target Job Description:")
            if matched_skills:
                chips_html = "".join([f'<span class="chip-matched">✓ {s}</span>' for s in matched_skills])
                st.markdown(f'<div class="chips-wrap">{chips_html}</div>', unsafe_allow_html=True)
            else:
                st.info("No direct skill matches detected.")

        with g_col2:
            st.markdown(f"#### ⚠️ Missing Skills Gaps ({len(missing_skills)})")
            st.caption("Keywords requested in the JD that were not found in your resume:")
            if missing_skills:
                chips_html = "".join([f'<span class="chip-missing">✗ {s}</span>' for s in missing_skills])
                st.markdown(f'<div class="chips-wrap">{chips_html}</div>', unsafe_allow_html=True)
            else:
                st.success("🎉 Outstanding! Zero skill gaps detected between your resume and this JD.")

        st.markdown("---")
        st.markdown("#### 💡 Tactical Advice to Reach 95%+ ATS Score")
        st.markdown(f"""
        1. **Incorporate Missing Keywords into Your Work**: If you have familiar experience with `{', '.join(missing_skills[:3]) if missing_skills else 'any secondary tools'}`, consider adding them to your projects or skills list to immediately elevate your score.
        2. **Quantify Your Accomplishments**: Recruiters and ATS screening engines favor resumes with numeric metrics (e.g. *reduced inference latency by 35%*, *indexed 50k+ records*).
        3. **Target Job Title Alignment**: Your resume title has been aligned to **"{tailored.get('job_title')}"** to match recruiter search filters.
        """)

    # ----------------------------------------------------
    # TAB 3: TAILORED COVER LETTER
    # ----------------------------------------------------
    with tab_cover:
        st.markdown("### ✉️ Auto-Generated Tailored Cover Letter")
        st.caption("A tailored 3-paragraph executive cover letter customized to the JD and your matched strengths.")

        tailor_eng = get_tailor()
        cover_letter = tailor_eng.generate_cover_letter(tailored, jd_result)

        st.text_area("Cover Letter Text", value=cover_letter, height=350)

        st.download_button(
            label="⬇️ Download Cover Letter (TXT)",
            data=cover_letter,
            file_name=f"Cover_Letter_{cand_name_slug}.txt",
            mime="text/plain"
        )

    # ----------------------------------------------------
    # TAB 4: INTERVIEW PREPARATION GUIDE
    # ----------------------------------------------------
    with tab_prep:
        st.markdown("### 💡 Interview Preparation & Strategy Guide")
        st.caption("Strategic interview talking points designed to help you turn your tailored resume into an actual job offer.")

        tailor_eng = get_tailor()
        tips = tailor_eng.generate_interview_tips(matched_skills, missing_skills, jd_result)

        for tip in tips:
            icon = "🌟" if tip["type"] == "strength" else ("🌉" if tip["type"] == "gap" else "📐")
            with st.expander(f"{icon} {tip['title']}", expanded=True):
                st.write(tip["description"])

        st.markdown("""
        #### 🎯 Top 3 Questions to Prepare For This Role:
        1. *"Walk me through a challenging problem where you implemented scalable systems utilizing your core stack."*
        2. *"How do you monitor and optimize model performance or system throughput after deployment in production?"*
        3. *"Can you give an example of how you quickly learned and applied a new technology or framework under tight deadlines?"*
        """)

# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div style="text-align:center;color:#94A3B8;font-size:0.82rem;padding-top:3rem;padding-bottom:1.5rem;">
    AI Resume Tailoring System &bull; Production Engine &bull; Sentence Transformers &bull; Multi-Template PDF & DOCX Export
</div>
""", unsafe_allow_html=True)