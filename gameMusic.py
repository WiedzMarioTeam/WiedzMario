import pygame

class GameMusic(object):
	def __init__(self, default_level, sound_map):
		self.is_sound = True
		self.sound_level = default_level
		# initialize pygame mixer
		pygame.mixer.init(44100, 16, 2, 4096)
		self.sound_map = sound_map
		self.sounds = {}
		# bind all sounds
		for key in self.sound_map:
			self.sounds[key] = pygame.mixer.Sound(self.sound_map[key])

	def isSound(self):
		return self.is_sound
		

	def setSound(self, is_sound):
		self.is_sound = is_sound
		
	# play a sound only if sound is enabled
	def playSound(self, key):
		if self.isSound():
			self.sounds[key].set_volume((self.sound_level / 10.0) + 0.1)
			self.sounds[key].play(0)

	def turnOffSound(self,key):
		self.sounds[key].stop()

	def isSoundPlay(self,key):
		if pygame.mixer.get_busy():
			return 0
		else:
			return 1