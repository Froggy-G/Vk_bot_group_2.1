import translators as ts
import random
import requests
import settings

# module's data
info_answers = ({'1': 'Нивкоем случае',
               '2': 'Нет',
               '3': 'Скорее всего нет', 
               '4': 'Возможно', 
               '5': 'Скорее всего да', 
               '6': 'Да',
               '7': 'Однозначно да'})

# module "probability"
def probability_number():
    return 'Вероятность: '+ str(random.randint(0, 100)) + '%'

# module "info"
def get_info():
    number = random.randint(1, 7)
    for ans in info_answers:
        if ans == str(number):
            return info_answers[ans]

# module "transalte"
def translate(request_message):
    if request_message == 'перевод' or request_message == 'перевод ':
        return 'Вы не ввели текст'
    return ts.translate_html(request_message[8:], translator=ts.bing, to_language='ru', translator_params={})
def mem_translate(request_message):
    if request_message == 'мперевод' or request_message == 'мперевод ':
        return 'Вы не ввели текст'
    return ts.translate_html(request_message[9:], translator=ts.google, to_language='ru', translator_params={})

# module "weather"
def open_weather_map_service():
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city_id = '479123'
    query = {
        'id': city_id,
        'appID': settings.open_weather_map_token # your weather token
    }
    weather_data = requests.get(base_url, params=query).json()

    # translate weather parse
    def translate_parse_into_russian(text):
        return ts.translate_html(text, translator=ts.google, to_language='ru', translator_params={})

    # weather parse
    now_weather = {
        'main': weather_data['weather'][0]['description'],
        'temp': weather_data['main']['temp'],
        'humidity': weather_data['main']['humidity'],
        'pressure': weather_data['main']['pressure'],
        'visibility': weather_data['visibility'],
        'wind': weather_data['wind']['speed']
    }

    return (f"Погода для города: Ульяновск\n"
            f"\n🌆На улице сейчас: {translate_parse_into_russian(now_weather['main'])}" 
            f"\n🌡Температура: {round(now_weather['temp'] - 273)}℃"
            f"\n💧Влажность: {now_weather['humidity']}%"
            f"\n🌫Давление: {round(now_weather['pressure'] / 1.3)}мм.рт.стлб"
            f"\n🕴Видимость: {(now_weather['visibility']/ 1000)}км" 
            f"\n🌬Скорость ветра: {now_weather['wind']}м/с")