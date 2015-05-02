###############################################
#             Map Creator                     #
###############################################

"""

This is a map creator program. It will create a map
and save it as a string in a text file that you can
use in your games. side scroller or adventure
aslong as its a grid style game.

Creator - kent 'Turtle' nex
last update - March 1st 2015
finished - march 1st 2015

"""

# Imports
import pygame, sys, boxClass, courserClass, fglobals, keyboardClass
from pygame import *

###########################
#         Globals         #
###########################

# set the size of the screen and the FPS of the game
intSize = intWidth, intHeight = (1280,720)
FPS = 180

########################
#      Functions       #
########################

#This function initiates the game, collecting info for later
def programInit():
    #prints the opening of the program

    print '''
    ##############################
    #       LEVEL CREATOR        #
    #          -Turtle           #
    ##############################

    Welcome to the level creator!
    This is a program where you can
    create your own levels!
    Im going to need some basic
    information first:
    '''
    # This asks if you are starting a new level or not
    newlevel = ''
    # if the answer isnt yes or no then you have to try again
    while newlevel != 'y' and newlevel != 'n':
        newlevel = raw_input('Are you making a new level?:')
        newlevel = (newlevel).lower()

        # if the answer isnt yes or no then you have to try again
    layout = ''
    while layout != 'y' and layout != 'n':
        layout = raw_input('Is the map a side scroller?:')
        layout = (layout).lower()

    x = 0
    y = 0

    if newlevel == 'y':

        # if the answer isnt a number then you have to try again
        while True:
            try:
                x = input('X of the level?[int]:')
                break
            except NameError:
                print 'That was not a number. Try again!:'

        # if the answer isn't a number then you have to try again
        while True:
            try:
                y = input('Y of the level?[int]:')
                break
            except NameError:
                print 'That was not a number. Try again!:'

    # last couple lines wishing you good luck!
    print '''
    Now that we got that over with
    we can start to create our level!
    You use 1-0 to cycle through colors
    and hold left shit and press any key
    to set the mapKey to that letter!
    '''
    # returns the values you collected
    return newlevel, x, y, layout

# This function creates the map for you
def mapCreation(newlevel, x, y, layout):

    # Creates the sprite list
    boxSpriteList = sprite.Group()

    # changes the way the map is generated depending on what kind of map you want
    if (layout).lower() == 'y':
        # For side scrollers
        width = height = intHeight / y
    else:
        # for others
        height = width = intHeight / 20

    # this keeps track of what box it is
    boxnum = 0

    # if is a new map then create it!
    if newlevel == 'y':
        # Go through for every column
        for column in range(y):
            # go through for everything in the row
            for row in range(x):
                # x location
                locx = row * width
                # y location
                locy = column * height
                #creates the box
                box = boxClass.box(width, height, locx, locy, boxnum)
                # adds it to the sprite list
                boxSpriteList.add(box)
                # adds one to the box num
                boxnum += 1

    # Returns the sprites
    return boxSpriteList , width

# This will send back a list of all the sprites that collided with the courser
def boxcolFunc(boxGroup, curser):

    # returns the list
    return pygame.sprite.spritecollide(curser, boxGroup, False)

# this changes the letter of the block
def letterSelect(keys, Dict):
    # Checks this alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # checks all the key presses
    for i in keys:
        # if the key is true and its in the alphabet
        if keys[i] == True and i in alphabet:
            # then its sets it to this letter
            Dict['letter'] = i
    # returns the letter
    return Dict

# this is a dictionary of the colors you can change the block into
# recives all the colors and the update dict
def colorChange(keys, Dict, Colors):

    # checks key presses 1-0 and switches the color to match
    if keys['1']:
        Dict['color'] = Colors['black']
    elif keys['2']:
        Dict['color'] = Colors['red']
    elif keys['3']:
        Dict['color'] = Colors['green']
    elif keys['4']:
        Dict['color'] = Colors['blue']
    elif keys['5']:
        Dict['color'] = Colors['pink']
    elif keys['6']:
        Dict['color'] = Colors['white']
    elif keys['7']:
        Dict['color'] = Colors['teal']
    elif keys['8']:
        Dict['color'] = Colors['purple']
    elif keys['9']:
        Dict['color'] = Colors['gray']
    elif keys['0']:
        Dict['color'] = Colors['yellow']

    # returns the updated update dict
    return Dict

# this function saves the map as a .txt under the name you wanted it to be. gets the sprite list and length of the map
def save(spriteList, length):

    # getting what the user wants to save it as
    saveName = raw_input('What would you like to call your map?:')

    # Creates these empty lists to use later
    mapString = []
    lineString = []

    # sets the variables
    # turn to true when done
    finish = False
    # last number to find
    finalnum = len(spriteList)
    # current number
    i = 0
    # current number on row
    x = 0

    # loop - finishes when finish = True
    while not finish:
        # checks over every sprite
        for sprite in spriteList:
            # if it finds the number its looking for
            if (sprite.number) + 1 == i:
                # it appends that letter to the string
                lineString.append(sprite.letter)
                # if the length of the string = number of rows
                if x == length:
                    # appends that line to the map
                    mapString.append(','.join(lineString))
                    # and resets number count and line string
                    lineString = []
                    x = 0
                # if its the final number - it ends
                if i == finalnum:
                    finish = True
        # adds to the num and character counter
        i += 1
        x += 1
    # joins the string with a newline
    mapString = '\n'.join(mapString)

    # creates a new file and if it cant it will ask for another name
    try:
        # try's to create a new file with that name
        txtfile = open(saveName + '.txt', 'w')
    except:
        # if it cant then it asks for another name
        print"Couldn't make file. Try another name!"
        saveName = raw_input('Name of the file:')

    # writes the map into the file
    txtfile.write(mapString)
    # closes the file
    txtfile.close()
    # checks if the user wants to keep working
    # creates and empty string
    cont = ''
    # while you dont have y or n in it, this will loop until you do
    while cont != 'y' and cont != 'n':
        cont = raw_input('Would you like to keep working on the level?[Y/N]:')
        cont = (cont).lower()

    # if you put n then you close the program
    if cont == 'n':
        # closes the program
        raise SystemExit, 'FINISHED'
    # and if this shows then you dun goofed somewhere
    elif not cont == 'y': 'Something went wrong with the save function...'

# this function loads a map that's already been saved
def load(sideScroller):


    # gets the map name - must include.txt
    mapName = raw_input('Please enter the name of the map that you would like to load!:')
    # adds .txt to the name
    mapName = mapName + '.txt'
    # Try's to open the map, if it can it'll ask for a new map or if you don't want to load any then it will close
    while True:
        try:
            map = open(mapName, 'r+')
            break
        except:
            mapName = raw_input('No map named %s please try again!:' % mapName)
            mapName = mapName + '.txt'

    # reads the map
    mapString = map.read()
    # closes the file
    map.close()
    # removes ,'s
    mapString = mapString.replace(',', '')
    # splits it at the new line
    mapList = mapString.split('\n')

    # create the box sprite group
    boxSpriteList = pygame.sprite.Group()

    # if its a side scroller it sets the width of the map accordingly
    if sideScroller == 'y':
        width = height = intHeight / len(mapList)
    # if its just a free map then its sets it accordingly
    elif sideScroller == 'n':
        width = height = intHeight / 20

    # this is the num for the box to save again
    boxnum = 0

    # this loop will make the map
    for column in range(len(mapList)):
        for row in range(len(mapList[0])):
                # x location
                locx = row * width
                # y location
                locy = column * height
                #creates the box
                box = boxClass.box(width, height, locx, locy, boxnum)
                # sets the letter of the box
                box.letter = mapList[column][row]
                # this sets the color to black unless you its a ' ' the updates the color
                if box.letter != ' ':
                    box.color = fglobals.colors['black']
                    box.loadUpdate()
                # adds it to the sprite list
                boxSpriteList.add(box)
                # adds one to the box num
                boxnum += 1

    # returns the box sprite list and width
    return boxSpriteList, width


###########################
#     Main Function       #
###########################
def main():

    ##########################
    #       Starting         #
    ##########################

    # gets the starting info!
    newlevel, length, height, levellayout = programInit()

     # if its a new map then it loads a saved file
    if newlevel == 'n':
         boxSpriteList, boxWidth = load(levellayout)


    # inits
    pygame.init()
    # sets the framerate clock
    FPSclock = time.Clock()
    # sets the display
    winScreenObj = display.set_mode(intSize)
    # sets the caption for the display
    display.set_caption('Level Creator')

    ########################
    #      Variables       #
    ########################

    # colors
    colors = fglobals.colors

    # Used to set the blocks to new values
    updateDict = {
        'color' : (0,0,0),
        'letter' : 'A'}

    # set blocks to base values
    resetDict = {
        'color' : (colors['default']),
        'letter' : ' '}

    # Box sprite group
    userCurserGroup = pygame.sprite.Group()

    ########################
    #    Starting Calls    #
    ########################

    # This creates the map
    if newlevel == 'y':
        boxSpriteList, boxWidth = mapCreation(newlevel, length, height, levellayout)
    # This makes the cursor then adds it to its own sprite group
    userCurser = courserClass.CursorClass(10,10)
    userCurserGroup.add(userCurser)
    # This makes the keyboard input class
    userKeyboard = keyboardClass.keyboard()

    # Font
    deffont = pygame.font.SysFont(None, 72)
    letterfont = pygame.font.SysFont(None, boxWidth)

    ###########################
    #       Game Loop         #
    ###########################
    while 1:

        # Updates
        # gets the keys from the keyboard class
        keys = userKeyboard.update()
        # updates the cursors position
        userCurserGroup.update(pygame.mouse.get_pos())
        # sets the text of the letter indicator at the top left
        outputText = deffont.render(updateDict['letter'], 0, colors['black'])

        # This is for debug purposes
        if keys['D']:
            for i in boxSpriteList:
                print i.letter

        # this changes the selected letter to a new one
        if keys['LSHIFT']:
            updateDict = letterSelect(keys, updateDict)

        # This will change whether to display the letters or not
        if keys['SPACE']:
            # shows the letters on the sprites
            for i in boxSpriteList:
                i.lDisplay()
            # sets space to false so it doesnt flick between on and off
            keys['SPACE'] = False

        # enlarges the cursor or shrinks
        # Enlarges the cursor by 10
        if keys['mouseScrollup']:
            userCurser.sizeChange(10)
            # sets the mouseScrollup to false so it only happens once
            userKeyboard.keys['mouseScrollup'] = False
        # Shrinks the cursor by 10
        elif keys['mouseScrolldown']:
            userCurser.sizeChange(-10)
            # sets the mouseScrolldown to false so it only happens once
            userKeyboard.keys['mouseScrolldown'] = False

        # updates the left mouse click
        if keys['mouseLeft']:
            # gets the sprites that make contact with the box
            boxcollist = boxcolFunc(boxSpriteList, userCurser)
            # updates all the boxs that make contact with the cursor
            for sprites in boxcollist:
                sprites.change(updateDict)

        # updates the right mouse click
        if keys['mouseRight']:
            # gets the sprites that make contact with the box
            boxcollist = boxcolFunc(boxSpriteList, userCurser)
            for sprites in boxcollist:
                # updates all the boxs that make contact with the cursor
                sprites.change(resetDict)

        # moves the map left and right
        # left
        if keys['LEFT']:
            # sends mod so it moves on the positive
            boxSpriteList.update(1,0)
        # right
        if keys['RIGHT']:
            # sends mod so it moves in the negative
            boxSpriteList.update(-1,0)
        # up - only works in non side scroller levels
        if keys['UP'] and levellayout == 'n':
            # sends mod so it moves up
            boxSpriteList.update(0,1)
        # down - only works in non side scroller levels
        if keys['DOWN'] and levellayout == 'n':
            # sends mod so it moves down
            boxSpriteList.update(0,-1)

        # Calls the function that saves the map as a .txt
        if keys['F1']:
            save(boxSpriteList, length)
            keys['F1'] = False

        # Updates the update Dictionary
        updateDict = colorChange(keys, updateDict, colors)
        # Changes the cursors color to match the color its placing
        userCurser.colorUpdate(updateDict)

        # Draws
        # sets the screen color to white
        winScreenObj.fill(colors['white'])
        # Draws the box's
        boxSpriteList.draw(winScreenObj)
        # this draws the letters on the boxs if their display it true
        for i in boxSpriteList:
            if i.display:
                # returns the surface, x and y
                letterBlit ,x ,y =  i.surfaceReturn(letterfont)
                # Blits all of the letters
                winScreenObj.blit(letterBlit, (x, y))
        # Blits the text to show the letter you're using
        winScreenObj.blit(outputText, (0,0))
        # Blits the cursor
        userCurserGroup.draw(winScreenObj)

        # Final Updates - Don't change
        FPSclock.tick(FPS)
        display.update()

#########################
#     Calls main        #
#########################
if __name__ == '__main__':
    main()