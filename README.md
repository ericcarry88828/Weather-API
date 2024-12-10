# Weather API

This is an application for viewing weather forecasts through third-party API [OpenWeather](https://openweathermap.org/).
It uses Redis for caching responses to optimize performance and minimize API requests.

## Demo
<p align="center">
  <img src="https://raw.githubusercontent.com/ericcarry88828/Weather-API/refs/heads/main/weatherapp/demo/Demo1.png" width="33%">
  <img src="https://raw.githubusercontent.com/ericcarry88828/Weather-API/refs/heads/main/weatherapp/demo/Demo2.png" width="33%">
  <img src="https://raw.githubusercontent.com/ericcarry88828/Weather-API/refs/heads/main/weatherapp/demo/Demo3.png" width="33%">
</p>

## Features
- Weather Data Fetching: Retrieve real-time weather data for any location.
- Caching with Redis: Cache responses in Redis to reduce redundant API calls.
- Error Handling: Gracefully handle errors such as invalid city codes or third-party API downtime.
- Environment Variables: Store sensitive information like API keys and Redis credentials securely.

## Usage

```
git clone https://github.com/ericcarry88828/Weather-API.git
cd Weather-API
flask run or python run.py
```

## Install

### Pip
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Poetry
```
poetry install
.\.venv\Scripts\activate
```

## Dependencies
- Python version >= 3.10.9
- Python Packages
    - [Flask](https://flask.palletsprojects.com/en/stable/)
    - [Redis](https://redis.readthedocs.io/en/latest/)

## Environment Variables
- `.env`  for flask and redis and third-party API
    - **Note :** you can use local or cloud database
    - `REDIS_HOST`
    - `REDIS_PORT`
    - `REDIS_USERNAME`
    - `REDIS_PASSWORD`
    - `API_KEY`
    - `API_URL`
    - `GEO_URL`
    - `SECRET_KEY`
