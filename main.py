import requests
import json
import time

import const

def answer_user_bot(data):
    data = {
        'chat_id': const.MY_ID,
        'text': data
    }
    url = const.URL.format(token=const.TOKEN,
                           method=const.SEND_METH)
    responce = requests.post(url, data=data)

def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    city = data['name']
    msg = f'The weather in {city}: Temp is {temp}, State is {weather_state}'
    return msg

def get_weather(location):
    url = const.WEATHER_URL.format(city = location,
                                   weather_token = const.WEATHER_TOKEN)
    responce = requests.get(url)

    if responce.status_code != 200:
        return 'City not found'

    data = json.loads(responce.content)
    return parse_weather_data(data)



def get_message(data):
    return data['message']['text']


def save_update_id(update):
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True

def main():
    while True:
        url = const.URL.format(token = const.TOKEN,
                               method = const.UPDATE_METH)
        content = requests.get(url).text

        data = json.loads(content)
        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        time.sleep(1)

if __name__ == '__main__':
    main()



