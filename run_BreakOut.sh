#!/bin/bash

VENV_DIR="venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python -m venv $VENV_DIR
else
    echo "Virtual environment already exists."
fi

if [ -f "$VENV_DIR/Scripts/activate" ]; then
    source $VENV_DIR/Scripts/activate
else
    source $VENV_DIR/bin/activate
fi

if [ -f "requirements.txt" ]; then
    echo "Installing packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependency installation."
fi

echo "Running game..."
python main.py

deactivate