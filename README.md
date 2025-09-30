# Repository for final project
echo "# Emotion Detection Flask Application

A web application that analyzes text emotions using Watson NLP API with offline fallback.

## Features
- Real-time emotion detection (anger, disgust, fear, joy, sadness)
- Web interface for easy text input
- Offline fallback using lexicon-based analysis
- Error handling for invalid inputs
- REST API endpoint

## Installation
1. Clone the repository
2. Create virtual environment: python -m venv .venv
3. Activate: .\.venv\Scripts\Activate.ps1
4. Install dependencies: pip install -r requirements.txt

## Usage
1. Run: python server.py
2. Open browser: http://localhost:5000
3. Enter text and click 'Run Sentiment Analysis'

## Files
- server.py - Flask web server
- EmotionDetection/ - Emotion detection package
- templates/index.html - Web interface
- static/mywebscript.js - Frontend JavaScript
- requirements.txt - Dependencies
- test_emotion_detection.py - Unit tests

## Testing
Run unit tests: python test_emotion_detection.py
Run static analysis: pylint server.py

## License
MIT License" > README.md