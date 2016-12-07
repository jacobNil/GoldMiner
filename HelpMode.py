# the helpMode object

from tkinter import *
from Button import Button

class HelpMode(object):
    def __init__(self):
        imageNum = 2
        self.width = 800
        self.height = 600
        self.image=[None]*imageNum
        self.image[0]= PhotoImage(file=
                            "image/help/helpRegular800.gif")
        self.image[1]= PhotoImage(file=
                            "image/help/helpHighlight800.gif")
        self.buttonX0, self.buttonY0 = 678, 24
        self.buttonX1, self.buttonY1 = 756, 47

    def helpRedrawAll(self, canvas, data):

        (currX, currY) = data.motionPosn
        #print("currMouse",currX,currY)
        # the if the button is hightlighted
        if self.inButton(currX, currY):
            image = self.image[1]
        else: 
            image = self.image[0]

        canvas.create_image(self.width/2, self.height/2, 
                            image = image)

    def helpMousePressed(self, event, data):
        currX = event.x
        currY = event.y
        if self.inButton(currX, currY):
            data.mode = data.splashScreen
        pass

    def helpKeyPressed(self, event, data):
        if (event.keysym == "r"):
            data.mode = data.splashScreen
        pass


    def inButton(self, currX, currY):
        if ((currX > self.buttonX0) and 
            (currX < self.buttonX1) and
            (currY>self.buttonY0) and 
            (currY< self.buttonY1)):
            return True
        return False













