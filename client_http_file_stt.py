import requests

base_url = 'http://0.0.0.0:8000'

headers = {'Content-Type': 'application/json'}
tokenUrl = f'{base_url}/token'
data = '{ "username": "forrestgump", "password": "yourpassword" }'
token_response = requests.post(tokenUrl, data = data, headers=headers)
jwt_token = token_response.json()['access_token']

headers = {'Authorization': 'Bearer ' + jwt_token}
sttUrl = f'{base_url}/api/v1/stt/http'
#sttUrl = f'{base_url}/api/v1/stt/http?model=chinese'
hot_words = {'paris': -1000, 'power': 1000, 'parents': -1000}
audio_filename = 'audio/4507-16021-0012.wav'
#audio_filename = 'audio/I-am-very-busy-today_chinese.wav'
audio = [('audio', open(audio_filename, 'rb'))]
response = requests.post(sttUrl, data=hot_words, files=audio, headers=headers)
print(response.json())
