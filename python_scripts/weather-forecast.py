import forecastio

def getForecastData():
    api_key = "xxxxxxx"
    lat = 12.8695687
    lng = 67.5318274
    forecast_obj = {}

    forecast = forecastio.load_forecast(api_key, lat, lng)
    currently = forecast.currently()
    forecast_obj["temperature"] = currently.temperature
    forecast_obj["icon"] = currently.icon
    forecast_obj["summary"] = currently.summary

    # print forecast_obj["icon"]
    return forecast

# getForecastData()