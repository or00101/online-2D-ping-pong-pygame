from general import Vector

##########################################
#     ~~~~~~~ BACKGROUND CONST ~~~~~~~
##########################################
BACKGROUND_COLOR = (10, 150, 10)
FIELDLINE_THICKNESS = 5
FIELDLINE_COLOR = (250, 250, 250)
FIELDLINE_POS_Y = 20

##########################################
#     ~~~~~~~ FIELDLINE CLASS ~~~~~~~
##########################################

class Fieldline:
	def __init__(self, WIDTH, HEIGHT):

		FIELDLINE_POS_X = WIDTH/2 - FIELDLINE_THICKNESS
		FIELDLINE_LENGTH = HEIGHT - 2 * FIELDLINE_POS_Y

		self.thickness = FIELDLINE_THICKNESS
		self.color = FIELDLINE_COLOR
		self.pos = Vector(FIELDLINE_POS_X, FIELDLINE_POS_Y)
		self.length = FIELDLINE_LENGTH

	def draw(self, pg, win):
		rect = (self.pos.x, self.pos.y, self.thickness, self.length)

		pg.draw.rect(win, self.color, rect)

##########################################
#    ~~~~~~~ BACKGROUND CLASS ~~~~~~~
##########################################

class Background:
	def __init__(self, WIDTH, HEIGHT):
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		self.color = BACKGROUND_COLOR
		self.fieldline = Fieldline(WIDTH, HEIGHT)

	def draw(self, pg, win):
		win.fill(self.color)
		self.fieldline.draw(pg, win)