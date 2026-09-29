@echo off
echo Stopping Streamlit AI Resume Tailoring System...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8501') do taskkill /f /pid %%a 2>nul
echo Streamlit server stopped successfully.
pause
