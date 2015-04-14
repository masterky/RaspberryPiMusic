###########################
# Needed Modules:
# sudo apt-get install python-dev
# sudo apt-get install python-rpi.gpio
# 
#############################


from time import sleep

try:
	import RPi.GPIO as GPIO
except Exception, e:
	print "No Raspberry Pi lib installed"

class Oberserver(object):

	# Actions
	BUTTON_PUSHED = 0

	def __init__(self):
		pass
	def nofity(self, action, port):
		if action == self.BUTTON_PUSHED:
			# do stuff
			pass


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
				print "Button bushed"
				observer.notify(observer.BUTTON_PUSHED, self.port)
			else:
				print "idleling...."

			sleep(self.THRESHOLD)
