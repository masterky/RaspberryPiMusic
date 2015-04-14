###########################
# Needed Modules:
# sudo apt-get install python-dev
# sudo apt-get install python-rpi.gpio
# 
#############################

from thread import start_new_thread

# My Imports
from time import sleep
from MyMusic import MyMusic
import Data


try:
	import RPi.GPIO as GPIO
except Exception, e:
	print "No Raspberry Pi lib installed"

class Observer(object):

	# Actions
	BUTTON_PUSHED = 0
	THRESHOLD = 0.01

	def __init__(self):
		self.myMusic = MyMusic(Data.MUSIC_PATH)
		self.pushButton = Button(2, self)

	def nofity(self, action, port):
		if action == self.BUTTON_PUSHED:
			# do stuff
			print "button pushed"
			pass
	def observe(self):

		start_new_thread(self.myMusic.shuffle,())

		while 1:
			sleep(self.THRESHOLD)



class Button(object):

	stopFlag = False
	THRESHOLD = 0.5
	def __init__(self, port, observer):

		self.port = port
		self.observer = observer
		# RPi.GPIO Layout verwenden (wie Pin-Nummern)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(port, GPIO.IN)

	def stop(self):
		self.stopFlag = True
	# Run as Thread please
	def waitForPush(self):
		while not self.stopFlag:
			if GPIO.input(self.port) == GPIO.HIGH:
				observer.notify(observer.BUTTON_PUSHED, self.port)
			else:
				print "idleling...."

			sleep(self.THRESHOLD)
