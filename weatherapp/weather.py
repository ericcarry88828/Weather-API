from functools import wraps
from flask import Blueprint, jsonify, render_template, request, current_app
import redis.exceptions
import requests
import redis
bp = Blueprint('weather', __name__)


@bp.route('/')
def index():
    return render_template("index.html")


@bp.route('/weather')
def get_wather():
    city = request.args.get('city', None)

    check_data = check_weather(city)
    if check_data:
        return jsonify(check_data)

    lat, lon = get_lat_lon(city)
    if not lat:
        return jsonify({'error': "The city you entered cannot be found", "cod": "404"}), 404
    url = current_app.config['API_URL']
    para = {
        "lat": lat,
        "lon": lon,
        'units': "metric",
        'lang': "en",
        "appid": current_app.config['API_KEY']
    }
    r = requests.get(url, params=para)
    if r.status_code == 200:
        resp = r.json()
        temp = resp['main']['temp']
        hum = resp['main']['humidity']
        wind = resp['wind']['speed']
        desc = resp['weather'][0]['description']
        main = resp['weather'][0]['main']
        weather_data = {
            'temp': temp,
            'hum': hum,
            "wind": wind,
            "desc": desc,
            "main": main
        }

        store_data = [item for kv in weather_data.items() for item in kv]
        resp = set_weather(city, store_data)
        return jsonify(weather_data), 200
    return jsonify({"error": "Check 3rd party API Service status"}), 500


def get_lat_lon(city_name):
    url = current_app.config['GEO_URL']
    para = {
        "q": city_name,
        "appid": current_app.config['API_KEY']
    }
    r = requests.get(url, params=para)
    if r.status_code == 200 and r.json():
        resp = r.json()
        lat = resp[0]['lat']
        lon = resp[0]['lon']
        return lat, lon
    return False, False


def connect_redis(f):
    @wraps(f)
    def decoration_function(*args, **kwargs):
        r = redis.Redis(
            host=current_app.config['REDIS_HOST'], port=current_app.config['REDIS_PORT'], username=current_app.config['REDIS_USERNAME'], password=current_app.config['REDIS_PASSWORD'], decode_responses=True)
        try:
            r.ping()
        except redis.exceptions.ConnectionError as e:
            print(e)
        except redis.exceptions as all:
            print(all)
        return f(r, *args, **kwargs)
    return decoration_function


@connect_redis
def set_weather(r, name, store_data: list = None):
    r.hset(name, items=store_data)
    if r.hlen(name):
        r.expire(name, current_app.config['DATA_EXPIRE'])
    else:
        print('execution fail')


@connect_redis
def check_weather(r, name):
    data = r.hgetall(name)
    if data:
        return data
    return False
