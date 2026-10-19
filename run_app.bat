@echo off
title SURAKSHA AI - Women Safety Intelligence Platform
echo ===================================================
echo   Starting SURAKSHA AI Platform...
echo ===================================================

cd /d "%~dp0"

REM Find python executable (.venv or system)
if exist ".venv\Scripts\python.exe" (
    set "PY_EXE=.venv\Scripts\python.exe"
) else if exist "..\.venv\Scripts\python.exe" (
    set "PY_EXE=..\.venv\Scripts\python.exe"
) else (
    set "PY_EXE=python"
)

REM Ensure folium & dependencies are present
"%PY_EXE%" -c "import folium, streamlit_folium" 2>nul
if %errorlevel% neq 0 (
    echo Installing required map packages...
    "%PY_EXE%" -m pip install folium streamlit-folium
)

echo.
echo Launching SURAKSHA AI at http://localhost:8501 ...
"%PY_EXE%" -m streamlit run app.py
pause
