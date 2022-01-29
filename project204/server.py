import socket
from threading import Thread

SERVER = None
PORT = 6000
IP_ADDRESS = '127.0.0.1'

CLIENTS=[]

def setup():
	print('WELCOME TO TAMBOLA GAME')

	global SERVER 
	global PORT
	global IP_ADDRESS

	SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	SERVER.bind(IP_ADDRESS, PORT)

	SERVER.listen(10)

	print('SERVER WAITING FOR CONNECTIONS')


def acceptConnections():
	global CLIENTS, SERVER

	while True:
		player_socket, addr = SERVER.accept()
		player_name = player_socket.recv(1024).decode().strip()
		print(player_name)

		if (len(CLIENTS.keys()) == 0):
			CLIENTS[player_name] = {'player_type':'player1'}
		else:
			CLIENTS[player_name] = {'player_type':'player2'}

		CLIENTS[player_name]['player_socket'] = player_socket
		CLIENTS[player_name]['address'] = addr	
		CLIENTS[player_name]['player_name'] = player_name
		CLIENTS[player_name]['turn'] = False

		print(f"Connection Established With {player_name}:{addr}")

		
