@echo off
cd /d "%~dp0"
echo Starting AI Resume Tailoring System...
start /b python -m streamlit run app.py --server.headless=true
ping 127.0.0.1 -n 4 >nul
start http://localhost:8501

