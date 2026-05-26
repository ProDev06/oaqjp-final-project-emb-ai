'''
Importing necessary modules
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Web app")

@app.route("/emotionDetector")
def em_detector():
    '''
Creating route and execute func
'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    ang = response['anger']
    dis = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sad = response['sadness']
    dom = response['dominant_emotion']

    if dom is None:
        return "Invalid text! Please try again!"

    s = f"'anger': {ang}, 'disgust': {dis}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sad}."
    return f"For the given statement, the system response is {s} The dominant emotion is {dom}."


@app.route("/")
def render_index_page():
    '''
Creating home page
'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
