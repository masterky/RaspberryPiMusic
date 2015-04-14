#!/bin/python2.7
#############################
# Remote Music Player class
# Version 1.0
# Copyright: Malte Koch
# Libraries needed: pygame
##############################

import pygame
from os import listdir
from os.path import isfile, join
import random
from time import sleep
from thread import start_new_thread
from sys import exit



			

class MyMusic(object):

	stopFlag = False

	def __init__(self, path):
		pygame.mixer.init()
		pygame.mixer.fadeout(500)
		self.files = [join(path,f) for f in listdir(path) if isfile(join(path,f)) ]

	def __play__(self, audio):
		pygame.mixer.music.load(audio)
		pygame.mixer.music.play()
	
	def play(self):
		pygame.mixer.unpause()

	def loadNPlay(self, audio):
		self.__play__(audio)
		while pygame.mixer.music.get_busy() == True:
			continue
	def stop(self):
		pygame.mixer.music.stop()
		self.stopFlag = True

	def playAll(self):
		size = len(self.files)
		for i in range(0, size):
			if self.stopFlag is True:
				break
			print "Now playing ", self.files[i]
			self.loadNPlay(self.files[i])
	def pause(self):
		if pygame.mixer.get_busy() == True:
			pygame.mixer.pause()

	def shuffle(self):
		size = len(self.files)
		while not self.stopFlag:
			r = random.randint(0, (size -1))
			print "Now playing ", self.files[r]
			self.loadNPlay(self.files[r])

''''
m = MyMusic("C:\Users\masterky\Music\Claudia Aufnahmen")
start_new_thread(m.playAll,())
print "Sleep"
sleep(2)
print "Now stopping"
m.stop()
sleep(2)
print "Going home"
exit(0)
'''