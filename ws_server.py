from websocket_server import WebsocketServer
import logging
from os import getenv
from dotenv import load_dotenv
import json
load_dotenv()

class Websocket_Server():

    def __init__(self, host, port):
        self.server = WebsocketServer(port=port, host=host, loglevel=logging.DEBUG)

    def new_client(self, client, server):
        print('------------------------------------------')
        print("\033[1m新しいクライアントが接続されました。識別IDは{}です。\033[0m".format(client['id']))
    def client_left(self, client, server):
        print('------------------------------------------')
        print("\033[1mID{}のクライアントは切断されました。\033[0m".format(client['id']))
    def message_received(self, client, server, message):
        print('------------------------------------------')
        print("\033[1mID{}のクライアントからメッセージが送信されました。\033[0m\n内容: {}".format(client['id'], message))
        print()
        print('\033[1m送信メッセージ変換\033[0m')
        check = json.loads(message)
        print('名前:{}\n送信先:{}\n内容:{}'.format(check['name'],check['sender'],check['content']))
        self.server.send_message_to_all(message)
    
    # サーバーを起動する
    def run(self):
        self.server.set_fn_new_client(self.new_client)

        self.server.set_fn_client_left(self.client_left)

        self.server.set_fn_message_received(self.message_received) 
        self.server.run_forever()

IP_ADDR = getenv('IP') # IPアドレスを指定

aa=[
    '██╗    ██╗███████╗██████╗ ',
    '██║    ██║██╔════╝██╔══██╗',
    '██║ █╗ ██║█████╗  ██████╔╝',
    '██║███╗██║██╔══╝  ██╔══██╗',
    '╚███╔███╔╝███████╗██████╔╝',
    ' ╚══╝╚══╝ ╚══════╝╚═════╝ ',
    '███████╗ ██████╗  ██████╗██╗  ██╗███████╗████████╗',
    '██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝',
    '███████╗██║   ██║██║     █████╔╝ █████╗     ██║   ',
    '╚════██║██║   ██║██║     ██╔═██╗ ██╔══╝     ██║   ',
    '███████║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║   ',
    '╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ',
    '███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ ',
    '██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗',
    '███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝',
    '╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗',
    '███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║',
    '╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝'
]

for i in aa:
    print(f"\033[36m\033[1m{i}\033[0m\033[0m")

PORT=9001 # ポートを指定
ws_server = Websocket_Server(IP_ADDR, PORT)
ws_server.run()

