#import tkinter
from tkinter import *
import time

import Vector2
import game

oldTime = time.time()
currentTime = time.time()
'''the time the last frame took'''
deltaTime = 0
'''the total time the game is running'''
timePlaying = 0
'''the amound of loop cycles that have been done'''
loopCount = 1

def start(screenSize) :
    ''' starts the whole program'''
    root = Tk()
    canvas = Canvas(root, width = 1200, height = 800)

    #creat inputs here!
    root.bind('<Motion>', mouseMovement)
    root.bind('<KeyPress>', keyDown)
    root.bind('<KeyRelease>', keyUp)

    canvas.pack()

    while True:
        '''Starting the main loop'''
        global currentTime
        global oldTime
        global deltaTime
        global timePlaying
        
        '''Calculating the frame time'''
        currentTime = time.time()
        deltaTime = currentTime-oldTime
        timePlaying += deltaTime
        
        oldTime = currentTime

        global loopCount
        '''updating if the desired fps is reached'''
        if (timePlaying/loopCount > .03):
            #couting the loops
            loopCount += 1
            #updating everything
            mainLoop(canvas, root)
            #updating the window
            root.update()

mousePosition = Vector2.new()
def mouseMovement (e) :
    mousePosition.x = e.x
    mousePosition.y = e.y

keysDown = [False] * 222
def keyDown (e) :
    keysDown[e.keycode] = True  

def keyUp (e) :
    keysDown[e.keycode] = False

def mainLoop(canvas, root) :
    clear(canvas)

    global mousePosition
    global keysDown
    update( {'mousePos': mousePosition, 'keysDown': keysDown} )

    draw(canvas)

def clear(c):
    '''Clear the screen'''
    c.delete('all')

def update(input):
    '''updating the objects'''
    for key in game.GameObjects:
        game.GameObjects[key].update(input)

def draw(c):
    '''Drawing the objects'''
    for key in game.GameObjects:
        game.GameObjects[key].draw(c)


if __name__ == '__main__':
    start(Vector2.new(800, 600))