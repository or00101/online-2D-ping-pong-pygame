from general import Vector

##########################################
#   ~~~~~~~ CHARACHTER CONFIG ~~~~~~~
##########################################

LEFT_SIDE = 0
RIGHT_SIDE = 1
CHARACTER_SIZE = Vector(15, 30)

##########################################
#      ~~~~~~~ PLAYER CLASS ~~~~~~~
##########################################

class Player():
	def __init__(self, x, y, side, color):
		self.pos = Vector(x, y)
		self.side = side
		self.color = color
		self.size = CHARACTER_SIZE

	def update_pos(self, new_vel):
		v_x = new_vel.x
		v_y = new_vel.y

		self.pos.x += v_x
		self.pos.y += v_y

	def draw(self, pg, win):
		rect = (self.pos.x, self.pos.y, self.size.x, self.size.y)
		pg.draw.rect(win, self.color, rect)

	# Boundary Check:
	def past_right_boundary(self, bg):
		if self.side == LEFT_SIDE:
			right_boundary = bg.fieldline.pos.x
		else:
			right_boundary = bg.WIDTH
		return self.pos.x + self.size.x >= right_boundary

	def past_left_boundary(self, bg):
		if self.side == LEFT_SIDE:
			left_boundary = 0
		else:
			left_boundary = bg.fieldline.pos.x + bg.fieldline.thickness
		return self.pos.x <= left_boundary

	def past_upper_boundary(self):
		return self.pos.y <= 0

	def past_bottom_boundary(self, bg):
		return self.pos.y + self.size.y >= bg.HEIGHT