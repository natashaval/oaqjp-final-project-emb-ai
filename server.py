"""
create Flask for IBM EmotionDetector
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route('/emotionDetector')
def emotion_detector_route():
    """
        emotion detector route
    """
    input_text = request.args.get('textToAnalyze')
    result = emotion_detector(input_text)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
    "'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
    "and 'sadness': {result['sadness']}. "
    "The dominant emotion is <b>{result['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    """
        index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
