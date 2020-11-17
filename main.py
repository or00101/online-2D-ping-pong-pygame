import pygame as pg
import time
from player import Player
from general import Vector
from background import Background

##########################################
#    ~~~~~~~ GAMEPLAY GRAPHICS ~~~~~~~
##########################################

WIDTH = 700
HEIGHT = 500
FPS = 140

# Conveersion of units
def sec_to_msec(sec):
	return sec * 1000

# Determine FPS rate and save CPU power
def throttle(fps):
	T = sec_to_msec(1 / fps)
	T = int(T)

	pg.time.wait(T)

##########################################
#    ~~~~~~~ PLAYER CONFIG ~~~~~~~
##########################################

WALKING_VELOCITY = 0.03 * FPS
LEFT_SIDE = 0
RIGHT_SIDE = 1

# Left player start
LSTART_X = WIDTH / 4
LSTART_Y = HEIGHT / 2
LCOLOR = (255, 0, 0)

# Right player start
RSTART_X = 3 * WIDTH / 4
RSTART_Y = HEIGHT / 2
RCOLOR = (0, 0, 255)

##########################################
#     ~~~~~~~ KEY BINDINGS ~~~~~~~
##########################################

# Left player key bindings format: WASD
LPLAYER_UP = pg.K_w
LPLAYER_LEFT = pg.K_a
LPLAYER_DOWN = pg.K_s
LPLAYER_RIGHT = pg.K_d

# Right player key bindings format: (arrows)
RPLAYER_UP = pg.K_UP
RPLAYER_LEFT = pg.K_LEFT
RPLAYER_DOWN = pg.K_DOWN
RPLAYER_RIGHT = pg.K_RIGHT

##########################################
# ~~~~~~~ WINDOW & BACKGROUND INIT ~~~~~~~
##########################################

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("ping pong game")

bg = Background(WIDTH, HEIGHT)

##########################################
#       ~~~~~~~ PLAYERS INIT ~~~~~~~
##########################################

lplayer = Player(LSTART_X, LSTART_Y, LEFT_SIDE, LCOLOR)
rplayer = Player(RSTART_X, RSTART_Y, RIGHT_SIDE, RCOLOR)

##########################################
#     ~~~~~~~ GAMEPLAY HANDLES ~~~~~~~
##########################################
def handle_quit(pg):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			return True
	return False

def handle_key_presses(player, keys):
	new_vel = Vector(0, 0)


	# handle WASD keys:
	#UP
	if keys[LPLAYER_UP] and not player.past_upper_boundary(): 
		new_vel.y = -1

	#LEFT
	if keys[LPLAYER_LEFT] and not player.past_left_boundary(bg): 
		new_vel.x = -1
	
	#DOWN
	if keys[LPLAYER_DOWN] and not player.past_bottom_boundary(bg): 
		new_vel.y = 1
	
	#RIGHT
	if keys[LPLAYER_RIGHT] and not player.past_right_boundary(bg): 
		new_vel.x = 1
	
	new_vel.normalize()
	new_vel.mult_by_scalar(WALKING_VELOCITY)

	#update player velocity
	player.update_pos(new_vel)
	return player

def handle_opponent(player, keys):
	new_vel = Vector(0, 0)


	# handle WASD keys:
	#UP
	if keys[RPLAYER_UP] and not player.past_upper_boundary(): 
		new_vel.y = -1

	#LEFT
	if keys[RPLAYER_LEFT] and not player.past_left_boundary(bg): 
		new_vel.x = -1
	
	#DOWN
	if keys[RPLAYER_DOWN] and not player.past_bottom_boundary(bg): 
		new_vel.y = 1
	
	#RIGHT
	if keys[RPLAYER_RIGHT] and not player.past_right_boundary(bg): 
		new_vel.x = 1
	
	new_vel.normalize()
	new_vel.mult_by_scalar(WALKING_VELOCITY)

	#update player velocity
	player.update_pos(new_vel)
	return player

##########################################
#       ~~~~~~~  RUN GAME ~~~~~~~
##########################################

done = False
while not done:
	done = handle_quit(pg)

	keys = pg.key.get_pressed()

	lplayer = handle_key_presses(lplayer, keys)
	rplayer = handle_opponent(rplayer, keys)

	#generate background
	bg.draw(pg, win)
	lplayer.draw(pg, win)
	rplayer.draw(pg, win)
	throttle(FPS)
	pg.display.update()

pg.quit()



