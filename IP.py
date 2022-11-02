import socket



def grabber():
	x = input('What Is The URL: ')
#	y = x + '/24'
	IP_address = socket.gethostbyname(x)
	IP_address2 = socket.gethostbyname(x)
	try:
		print(IP_address2)
	except:
		print(IP_address)

grabber()
