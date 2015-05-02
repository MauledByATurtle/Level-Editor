import pygame, fglobals

# This creates the box class! - it is a child to the sprite class
class box(pygame.sprite.Sprite):

    # Init function: sent x and y for location
    def __init__(self, width, height,  x,  y, num):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Sets the color
        self.color = fglobals.colors['default']
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
        # this gets the rect from the image
        self.rect = self.image.get_rect()
        # This places the box in the right spot
        self.rect.x = x
        self.rect.y = y
        # The speed that the box moves
        self.speed = 10
        # the letter of the block
        self.letter = ' '
        # This will tell to display the letter or not
        self.display = False
        # this will keep what block it is
        self.number = num

    # Shows the letters on the rect
    def surfaceReturn(self, font):
        # Sets the color to the inverse of the boxs color
        fontColor = ((255 - self.color[0]), (255 - self.color[1]),(255 - self.color[2]))
        # Makes the surface of the letter
        letterdisplay = font.render(self.letter, 0, fontColor)
        # Returns the letters surface and pos of the square
        return letterdisplay, self.rect.x, self.rect.y

    # Moves the rects
    def update(self, xmod, ymod):
        # Moves the rect left or right depending on the mod = 1 or -1
        self.rect.x += self.speed * xmod
        # Moves the rect up or down depending on the mod = 1 or -1
        self.rect.y += self.speed * ymod

    # changes the color of the blocks you're clicking on
    def change(self, update):
        # Changes the color to the new color
        self.color = update['color']
        # Changes the letter to the new letter
        self.letter = update['letter']
        # Fills in the image
        self.image.fill(self.color)

        # Switches whether to display the letters or not
    def lDisplay(self):
        # If display is false then it is true and if its true then its false
        if not self.display: self.display = True
        elif self.display: self.display = False

    # this shows the color on the block. It fixs a problem I was having with loading maps and nothing shows up
    def loadUpdate(self):
        self.image.fill(self.color)

