TOKEN = 'token'
URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = id

UPDATE_ID_FILE_PATH = 'update_id'


with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = 'token'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'
