@echo off
SET VENV_DIR=venv

IF NOT EXIST "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
) ELSE (
    echo Virtual environment already exists.
)

CALL "%VENV_DIR%\Scripts\activate"

IF EXIST "requirements.txt" (
    echo Installing packages...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt not found. Skipping dependency installation.
)

echo Running game...
python main.py

CALL "%VENV_DIR%\Scripts\deactivate"

pause