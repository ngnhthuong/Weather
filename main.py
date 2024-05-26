from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/text-generate')
def textGenerate():
    return render_template('text-generate.html')

@app.route('/face-detection')
def faceDetection():
    return render_template('face-detection.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2999)