# Class for buttons
class Button():
	# Parameters are image of rectangle,position of it,text of the button,font,and the color shown when mouse is above it
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):

		# Each parameter is put in a self variable
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.change = base_color

		# If rectangle image is not given the function checks if mouse is above the text
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	# function to update
	def update(self, screen):
		# If there's image it is placed in such a way that text can be in the middle
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	# The fuction to check for input(Mouse button)
	def checkForInput(self, position):
		# Checks position of mouse and text and if the mouse has been clicked
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	# function for hovering color
	def changeColor(self, position):

		# Checks mouse position and text position if they are same, the color of text changes
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
			self.change = self.hovering_color
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
			self.change = self.base_color