import socket

############################
# Inet Connection checker
# Version 1.0
# Copyright Malte Koch
############################

class InetConnection(object):
	REMOTE_SERVER = "www.google.de"
	def __init__(self):
		pass
	def test(self):
		try:
			host = socket.gethostbyname(self.REMOTE_SERVER)
			s = socket.create_connection((host, 80), 2)
			return True
		except:
			pass
		print "No inet connection"
		return False

#print "InetConnection active: ", InetConnection().test()