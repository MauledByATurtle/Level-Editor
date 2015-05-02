import pygame, fglobals

# Class CursorClass - Child of Sprite class
class CursorClass(pygame.sprite.Sprite):

    # init function
    def __init__(self, width, height):
        # Inits the sprite class
        pygame.sprite.Sprite.__init__(self)
        # Sets the color
        self.color = fglobals.colors['cursor']
        # sets the image of the sprite and fills it in with the color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        # get the rect from the image
        self.rect = self.image.get_rect()

    # update function - Changes the position to the mouse pos
    def update(self, pos):
        # sets the center of the rect to the mouse loc
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

    # changes the size of the cursor
    def sizeChange(self, percentage):
        # This is used so the cursor cant get below 0 in size
        # If the cursor is above 10 then do stuff normally
        if self.rect.width > 10:
            # this infaltes the rect and creates a new image
            self.rect = self.rect.inflate(percentage, percentage)
            self.image = pygame.Surface(self.rect.size)
        # if the cursor is smaller then 10 then then you can only make it bigger
        elif self.rect.width <= 10 and percentage > 0:
            # this inflates the rect and  creates the new image
            self.rect = self.rect.inflate(percentage, percentage)
            self.image = pygame.Surface(self.rect.size)

    # Changes the color to match the color blocks
    def colorUpdate(self, Dict):
        self.color = Dict['color']
        self.image.fill(self.color)




