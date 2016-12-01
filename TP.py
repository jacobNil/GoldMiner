
from tkinter import *
from objects import Button
#from PIL import Image, ImageTk



def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)




####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    width = data.width
    height = data.height
    data.splashScreen = "splash Screen"
    data.scoreMode = "Score Mode"
    data.timeMode = "Time Mode"
    data.helpMode = "Help"
    data.shopMode = "Shopping"

    data.originalMode = data.splashScreen
    # the initial screen
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
    data.image = None





####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == data.splashScreen):  splashScreenMousePressed(event, data)

    elif (data.mode == data.scoreMode):   scoreModeMousePressed(event, data)
    elif (data.mode == data.timeMode):    timeModeMousePressed(event, data)
    elif (data.mode == data.helpMode):    helpMousePressed(event, data)
    elif (data.mode == data.shopMode):    shopModeMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == data.splashScreen): splashScreenKeyPressed(event, data)
    elif (data.mode == data.scoreMode):  scoreModeKeyPressed(event, data)
    elif (data.mode == data.timeMode):   timeModeKeyPressed(event, data)
    elif (data.mode == data.helpMode):   helpKeyPressed(event, data)
    elif (data.mode == data.shopMode):   shopModeKeyPressed(event, data)

def timerFired(data):
    if (data.mode == data.splashScreen): splashScreenTimerFired(data)
    elif (data.mode == data.scoreMode):  scoreModeTimerFired(data)
    elif (data.mode == data.timeMode):   timeModeTimerFired(data)
    elif (data.mode == data.helpMode):   helpTimerFired(data)
    elif (data.mode == data.shopMode):   shopModeTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == data.splashScreen): splashScreenRedrawAll(canvas, data)
    elif (data.mode == data.scoreMode):  scoreModeRedrawAll(canvas, data)
    elif (data.mode == data.timeMode):   timeModeRedrawAll(canvas, data)
    elif (data.mode == data.helpMode):   helpRedrawAll(canvas, data)
    elif (data.mode == data.shopMode):   shopModeRedrawAll(canvas, data)





####################################
# playGame: "timeMode"
####################################

def timeModeMousePressed(event, data):
    data.score = 0

def timeModeKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.originalMode = data.mode
        data.mode = data.helpMode
    elif (event.keysym == "r"):
        data.mode = data.splashScreen
        init(data)

def timeModeTimerFired(data):
    data.score += 1

def timeModeRedrawAll(canvas, data):

    timeMode.drawAboveGround(canva, data)

    timeMode.drawUndergound(canvas, data)

    timeMode.drawPrecious(canvas, data)

    timeMode.drawMiner(canvas, data)

    timeMode.drawTools(canvas, data)

    timeMode.drawClock(canvas, data)


    
    canvas.create_text(data.width/2, data.height/2-10,
                       text="Score = " + str(data.score), font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+15,
                       text="this is time mode", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press 'h' for help!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+60,
                       text="Press 'r' to reset!", font="Arial 20")



drawAboveGround

####################################
# playGame: "scoreMode"
####################################

def scoreModeMousePressed(event, data):
    data.score = 0

def scoreModeKeyPressed(event, data):
    if (event.keysym == 'h'):
        data.originalMode = data.mode
        data.mode = data.helpMode
    elif (event.keysym == "r"):
        data.mode = data.splashScreen
        init(data)

def scoreModeTimerFired(data):

    data.score += 1

def scoreModeRedrawAll(canvas, data):

    canvas.create_text(data.width/2, data.height/2-10,
                       text="Score = " + str(data.score), font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+15,
                       text="this is score mode", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+40,
                       text="Press 'h' for help!", font="Arial 20")
    canvas.create_text(data.width/2, data.height/2+60,
                       text="Press 'r' to reset!", font="Arial 20")

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
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    x = event.x
    y = event.y
    print(x, y)
    for button in data.splashScreenButton:
        if button.clickInButton(x, y) == True:
            data.mode = button.name
            #print(button)
            break

def splashScreenKeyPressed(event, data):
    data.mode = "playGame"

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):

    
    #print(image)
    canvas.create_image(0, 0, anchor = NW, image=data.image)

    for button in data.splashScreenButton:
        button.drawButton(canvas)

    

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

    init(data)
    # create the root and the canvas
    root = Tk()
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
    data.image = PhotoImage(file="splash.gif")
    #print(image)
    
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)