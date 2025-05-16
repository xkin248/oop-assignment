#!/bin/bash

echo "📦 Creating Python virtual environment..."
python3 -m venv venv

echo "✅ Virtual environment created."
echo "⚙️ Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing required Python packages..."
pip install flask mysql-connector-python flask-bcrypt sqlalchemy pyodbc

echo "📝 Freezing dependencies to requirements.txt..."
pip freeze > requirements.txt

echo "✅ All Python packages installed and saved to requirements.txt."
echo "🚀 To activate your virtual environment in the future, run:"
echo "source venv/bin/activate"
