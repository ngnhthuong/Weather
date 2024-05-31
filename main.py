from flask import Flask, request, jsonify, render_template, redirect, url_for
import pandas as pd
import numpy as np
from datetime import datetime
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

@app.route('/weather')
def weather():
    df = pd.read_csv('static/model/XGBRegressor/date_weather_predict.csv')
    weather_data = df.to_dict(orient='records')
    print(weather_data)
    current_date = datetime.now()
    current_date = current_date.strftime('%d/%m/%Y')
    return render_template('weather.html', weather_data=weather_data, current_date=current_date)   


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2999)