import turtle as t
import time as ti
import random as r
import math as m

# Will add more functionality here later.
def end():
	t.bye()

class Window():
	def __init__(self, vertical, horizontal, color, exitKey, name):
		self.screen = t.Screen()
		self.screen.setup(height = vertical, width = horizontal)
		self.screen.bgcolor(color)
		self.screen.title(name)
		self.screen.listen()
		self.screen.onkeypress(end, exitKey)
		self.screen.tracer(0)

	def run(self):
		self.screen.update()

	def kill(self):
		t.bye()

# This is your basic, default window.
class DefaultWindow(Window):
	def __init__(self, name, vertical = 600, horizontal = 800, color = '#FFFFFF', exitKey = 'Escape'):
		super().__init__(vertical, horizontal, color, exitKey, name)

class GameObject():
	def __init__(self, color, speed, x, y, width, height, shape):
		self.turtle = t.Turtle()
		self.turtle.color(color)
		self.turtle.shape(shape)
		self.turtle.shapesize(stretch_len = width/20, stretch_wid = height/20)
		self.turtle.penup()
		self.turtle.goto(x, y)
		self.speed = speed
		self.wid = width
		self.high = height
		self.x, self.y = x, y

	# For binding simple movement to keys
	def up(self):
		self.turtle.sety(self.turtle.ycor() + self.speed)
	def down(self):
		self.turtle.sety(self.turtle.ycor() - self.speed)
	def left(self):
		self.turtle.setx(self.turtle.xcor() - self.speed)
	def right(self):
		self.turtle.setx(self.turtle.xcor() + self.speed)

	# Goes up, down, left, right in bindsList
	def simple_binds(self, bindsList, window):
		window.screen.listen() 
		window.screen.onkeypress(self.up, bindsList[0])
		window.screen.onkeypress(self.down, bindsList[1])
		window.screen.onkeypress(self.left, bindsList[2])
		window.screen.onkeypress(self.right, bindsList[3])

	# If two entities have collided
	def collided(self, other):
		if abs(other.turtle.xcor() - self.turtle.xcor()) > other.wid:
			return False
		elif abs(other.turtle.ycor() - self.turtle.ycor()) > other.high:
			return False
		return True

class StaticBox(GameObject):
	def __init__(self, color, x, y, width, height, speed = 0, shape = 'square'):
		# Fixed bug here- needs to be in same order as super()
		super().__init__(color, speed, x, y, width, height, shape)

	# Aligning with other coordinates - tested.
	def align_left(self, coor):
		self.turtle.goto(coor + self.wid/2, self.y)
	def align_right(self, coor):
		self.turtle.goto(coor - self.wid/2, self.y)
	def align_up(self, coor):
		self.turtle.goto(self.x, coor - self.high/2)
	def align_down(self, coor):
		self.turtle.goto(self.x, coor + self.high/2)
