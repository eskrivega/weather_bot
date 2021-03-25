TOKEN = '1726245951:AAHajR0q3ZEXPpEcl9IOUpYmZYbDWwlnils'
URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 336590651

UPDATE_ID_FILE_PATH = 'update_id'


with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = '6c4e05f8106b0e9b8c6b30528efdff19'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}'