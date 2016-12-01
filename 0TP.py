
from tkinter import *
from objects import Button
from Precious import Precious, Gold, Rock

from ScoreMode import ScoreMode
import random, string

#from PIL import Image, ImageTk

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    # the interface dimensions
    width = data.width
    height = data.height
    # the mode control
    data.splashScreen = "splash Screen"
    data.scoreMode = "Score Mode"
    data.timeMode = "Time Mode"
    data.helpMode = "Help"
    data.shopMode = "Shopping"
    data.scoreModeTrans = "scoreModeTransition"

    data.originalMode = data.splashScreen # the strat mode

    # the splash screen
    data.mode = data.splashScreen
    data.score = 0
    margin = data.height/9
    scoreButton = Button(width/2, margin, width*4/5, 2*margin, 
                        "yellow", "Score Mode")
    timeButton = Button(width/2, 3*margin, width*4/5, 4*margin, 
                        "yellow", "Time Mode")
    shoppingButton = Button(width/2, 5*margin, width*4/5, 6*margin, 
                        "yellow", "Shopping")
    helpButton = Button (width/2, 7*margin, width*4/5, 8*margin, 
                        "yellow", "Help")

    data.splashScreenButton = [scoreButton, timeButton, 
                               shoppingButton, helpButton]
    data.splashImage = None

    data.game = None

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == data.splashScreen):  splashScreenMousePressed(event, data)

    elif (data.mode == data.scoreMode):   pass
    elif (data.mode == data.timeMode):    cleanModeMousePressed(event, data)
    elif (data.mode == data.helpMode):    helpMousePressed(event, data)
    elif (data.mode == data.shopMode):    shopModeMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == data.splashScreen): splashScreenKeyPressed(event, data)
    elif (data.mode == data.scoreMode):  data.game.helpKeyPressed(event, data)
    elif (data.mode == data.timeMode):   cleanModeKeyPressed(event, data)
    elif (data.mode == data.helpMode):   helpKeyPressed(event, data)
    elif (data.mode == data.shopMode):   shopModeKeyPressed(event, data)
    elif (data.mode == data.scoreModeTrans):
        scoreModeTransHelpKeyPressed(event, data)


def timerFired(data):
    if (data.mode == data.splashScreen): splashScreenTimerFired(data)
    elif (data.mode == data.scoreMode):  data.game.helpTimerFired(data)
    elif (data.mode == data.timeMode):   cleanModeTimerFired(data)
    elif (data.mode == data.helpMode):   helpTimerFired(data)
    elif (data.mode == data.shopMode):   shopModeTimerFired(data)
    elif (data.mode == data.scoreModeTrans): 
        data.game.helpTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == data.splashScreen): splashScreenRedrawAll(canvas, data)
    elif (data.mode == data.scoreMode):  data.game.drawScoreMode(canvas)
    elif (data.mode == data.timeMode):   cleanModeRedrawAll(canvas, data)
    elif (data.mode == data.helpMode):   helpRedrawAll(canvas, data)
    elif (data.mode == data.shopMode):   shopModeRedrawAll(canvas, data)
    elif (data.mode == data.scoreModeTrans): 
        data.game.drawScoreModeTrans(canvas)



####################################
# scoreModeTrans helper function
####################################

# since this helper function should be able to create a new
# object of score Mode game, but the object ScoreMode and the 
# object ScoreModeTrans cannot import each other. So i have to use
# helper function for now
# ????!!!!!but this need to be worked on!!!!!!!!!!!
def scoreModeTransHelpKeyPressed(event, data):
    if data.game.isPreAccomplished:
        if event.keysym == "p":
            level = data.game.currLevel
            score = data.game.currScore
            data.game = ScoreMode(level+1, score)
            data.mode = data.scoreMode
                
    if event.keysym == "h":
        data.mode = data.helpMode
    if event.keysym == "r":
        init(data)



####################################
# playGame: "cleanMode"
####################################

def cleanModeMousePressed(event, data):
    data.score = 0

def cleanModeKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.originalMode = data.mode
        data.mode = data.helpMode
    elif (event.keysym == "r"):
        data.mode = data.splashScreen
        init(data)

def cleanModeTimerFired(data):

    data.score += 1

def cleanModeRedrawAll(canvas, data):

    canvas.create_text(data.width/2, data.height/2-10,
                       text="Score = " + str(data.score), font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+15,
                       text="this is score mode", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press 'h' for help!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+60,
                       text="Press 'r' to reset!", font="Arial 20")

####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    x = event.x
    y = event.y
    
    for button in data.splashScreenButton:
        if button.clickInButton(x, y) == True:
            data.mode = button.name
            data.game = ScoreMode(width=data.width, 
                                  height=data.height)
            #print(button)
            break

def splashScreenKeyPressed(event, data):
    if event.keysym == "t" :
        data.mode = data.timeMode
        
    elif event.keysym == "s":
        data.mode = data.scoreMode
        data.game = ScoreMode()
    elif event.keysym == "h":
        data.mode = data.helpMode

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    data.splashImage = PhotoImage(file="image/splash/splash.gif")
    canvas.create_image(0, 0, anchor = NW, image=data.splashImage)

    
    for button in data.splashScreenButton:
        button.drawButton(canvas)

####################################
# playGame: "shopping"
####################################

def shopModeMousePressed(event, data):
    data.score = 0

def shopModeKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.originalMode = data.mode
        data.mode = data.helpMode
    elif (event.keysym == "r"):
        data.mode = data.splashScreen

def shopModeTimerFired(data):
    data.score += 1

def shopModeRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="This is a fun game!", font="Arial 26 bold")
    
    canvas.create_text(data.width/2, data.height/2+15,
                       text="you can do shopping here", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press 'h' for help!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+60,
                       text="Press 'r' to reset!", font="Arial 20")


####################################
# help mode
####################################

def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    data.mode = data.originalMode

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_text(data.width/2, data.height/2-40,
                       text="This is help mode!", font="Arial 26 bold")
    canvas.create_text(data.width/2, data.height/2-10,
                       text="How to play:", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press any key to keep playing!", font="Arial 20")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    
    # create the root and the canvas
    root = Tk()
    init(data)
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(fill=BOTH, expand=YES)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    
    #print(image)
    
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)





