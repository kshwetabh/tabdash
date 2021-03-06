import forecastio

def getForecastData():
    api_key = "8f79661fe2a618c388fcf2942839c428"
    lat = 12.8695687
    lng = 77.5318274
    forecast_obj = {}

    forecast = forecastio.load_forecast(api_key, lat, lng)
    currently = forecast.currently()
    #sometimes temperature is in fractions, remote the digits after decimal
    forecast_obj["temperature"] = format(currently.temperature, '.0f')
    forecast_obj["icon"] = currently.icon
    forecast_obj["summary"] = currently.summary

    print forecast_obj
    return forecast_obj

getForecastData()