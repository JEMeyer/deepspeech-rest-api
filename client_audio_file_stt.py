import websocket
from halo import Halo

websocket = websocket.WebSocket()
websocket.connect('ws://0.0.0.0:8000/api/v1/stt/ws')

try:
    with Halo(text='Audio file STT with WebSocket...', text_color='cyan', spinner='spin'):
        with open('audio/8455-210777-0068.wav', mode='rb') as file:
            websocket.send('{"power":1000, "paris":-1000}')
            audio = file.read()
            websocket.send_binary(audio)
            result = websocket.recv()
            print()
            print(result)
            websocket.close()
except KeyboardInterrupt:
    print()
    print('Audio file STT is interrupted')
