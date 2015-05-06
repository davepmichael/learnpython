import pygame
import sys
from pygame.locals import *
from random import randint

class Player(pygame.sprite.Sprite):
	'''The class that holds the main player, and controls how they jump. nb. The player doens't move left or right, the world moves around them'''
	def __init__(self, start_x, start_y, width, height):
		
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
		self.rect = self.image.get_rect()
		self.rect.x = start_x
		self.rect.y = start_y
		self.speed_y = 0
		self.base = pygame.Rect(start_x, start_y + height, width, 2)
		
	def move_y(self):
		collided_y = world.collided_get_y(self.base)
		if self.speed_y <= 0 or collided_y < 0:
			self.rect.y = self.rect.y + self.speed_y
			self.speed_y = self.speed_y + gravity
		if collided_y > 0 and self.speed_y > 0:
			self.rect.y = collided_y
		self.base.y = self.rect.y+self.rect.height
		 

	def move_y(self):
		'''this calculates the y-axis movement for the player in the 
		current speed'''
		pass

	def jump(self, speed):
		'''This sets the player to jump, but it only can if its feet are on the floor'''
		pass

class World():
	'''This will hold the platforms and the goal. 
	nb. In this game, the world moves left and right rather than the player'''
	def __init__(self, level, block_size, colour_platform, colour_goals):
		self.platforms = []
		self.goals = []
		self.posn_y = 0
		self.colour = colour_platform
		self.colour_goals = colour_goals
		self.block_size = block_size

		for line in level:
			self.posn_x = 0
			for block in line:
				if block == "-":
					self.platforms.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))
				if block == "G":
					self.goals.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))
				self.posn_x = self.posn_x + block_size
			self.posn_y = self.posn_y + block_size

	def move(self, dist):
		'''move the world dist pixels right (a negative dist means left)'''
		pass

	def collided_get_y(self, player_rect):
		'''get the y value of the platform the player is currently on'''
		return_y = -1
		for block in self.platforms:
			if block.colliderect(player_rect):
				return_y = block.y - block.height + 1
		return return_y

	def at_goal(self, player_rect):
		'''return True if the player is currently in contact with the goal. False otherwise'''
		pass

	def update(self, screen):
		'''draw all the rectangles onto the screen'''
		for block in self.platforms:
			pygame.draw.rect(screen, self.colour, block, 0)
		for block in self.goals:
			pygame.draw.rect(screen, self.colour_goals, block, 0)

class Doom():
	'''this class holds all the things that can kill the player'''
	def __init__(self, fireball_num, pit_depth, colour):
		pass

	def move(self, dist):
		'''move everything right dist pixels (negative dist means left)'''
		pass

	def update(self, screen):
		'''move fireballs down, and draw everything on the screen'''
		pass

	def collided(self, player_rect):
		'''check if the player is currently in contact with any of the doom.
		nb. shrink the rectangle for the fireballs to make it fairer'''
		pass

class Fireball(pygame.sprite.Sprite):
	'''this class holds the fireballs that fall from the sky'''
	def __init__(self):
		pass

	def reset(self):
		'''re-generate the fireball a random distance along the screen and give them a random speed'''
		pass

	def move_x(self, dist):
		'''move the fireballs dist pixels to the right 
		(negative dist means left)'''
		pass

	def move_y(self):
		'''move the fireball the appropriate distance down the screen
		nb. fireballs don't accellerate with gravity, but have a random speed. if the fireball has reached the bottom of the screen, 
		regenerate it'''
		pass

	def update(self, screen, colour):
		'''draw the fireball onto the screen'''
		pass
#options
screen_x = 600
screen_y = 400
game_name = "Awesome Raspberry Pi Platformer"
player_spawn_x = 50
player_spawn_y = 200
player_image = "lidia.png"
level=[
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"          ---                G",
	"     -- --    ---       ------",
	" -- -            -------      "]
platform_colour = (100,100,100)
goal_colour = (0,0,255)
gravity = 1

#initialise pygame.mixer

#initialise pygame
pygame.init()
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption(game_name)
screen = pygame.display.get_surface()

#load level

#initialise variables
clock = pygame.time.Clock()
player = Player(player_spawn_x, player_spawn_y, 20, 30)
player_plain = pygame.sprite.RenderPlain(player)
world = World(level, 30, platform_colour, goal_colour)
finished = False

#setup the background

while not finished:
	
	#blank screen
	screen.fill((0, 0, 0))
	
	#check events
	for event in pygame.event.get():
		if event.type == quit:
			finished = True
			
	#check which keys are held      
	#move the player with gravity
	player.move_y()
	
	#render the frame
	player_plain.draw(screen)
	world.update(screen)
	
	#update the display
	pygame.display.update()
	
	#check if the player is dead
	#check if the player has completed the level
	#set the speed
	clock.tick(20)
	
