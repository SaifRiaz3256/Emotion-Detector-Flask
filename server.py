"""
Flask web application for emotion detection using Watson NLP API.

This module provides a web interface for analyzing text emotions
through a REST API endpoint and serves an HTML interface.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Endpoint for emotion detection analysis.

    Processes text input from query parameters and returns formatted
    emotion analysis results or error messages for invalid input.

    Returns:
        str: Formatted emotion analysis results or error message.
    """
    # Get the text from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle empty or None input at server level
    if not text_to_analyze or text_to_analyze.strip() == '':
        return "Invalid text! Please try again!"

    # Call the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check if the analysis was successful (dominant_emotion should not be None)
    # This handles cases where emotion_detector returns None values due to:
    # - Blank input detected by the function
    # - Status code 400 from API
    # - Network errors without offline fallback
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    emotions_list = []
    for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        score = response.get(emotion, 0.0)
        emotions_list.append(f"'{emotion}': {score}")

    emotions_text = ", ".join(emotions_list)
    dominant_emotion = response['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is {emotions_text}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Render the main page.

    Serves the HTML template for the emotion detection web interface.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
