from flask import Flask, render_template, request, jsonify
import json
from weather_forecast import getForecastData
from airtel_smartbytes import getSmartByteData

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/")
def index():
    # print getForecastData()
    # print getSmartByteData()
    return render_template("index.html")

@app.route("/smartbytes")
def smartbytes():
    smartBytes = getSmartByteData()
    return jsonify(remaining_data=smartBytes["remaining_data"], remaining_days=smartBytes["remaining_days"], remaining_pct=smartBytes["remaining_pct"])


@app.route("/weather")
def weather():
    weatherForecast = getForecastData()
    return jsonify(temperature=weatherForecast["temperature"], icon=weatherForecast["icon"], summary=weatherForecast["summary"])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
