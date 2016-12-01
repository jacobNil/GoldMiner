
# the object draw the score mode transition screen
# the screen will shown when one level of score mode 
# is finished. The screen will shown different content
# based on the level is accomplished or not

from tkinter import *
from Precious import Gold, Rock
#from ScoreMode import ScoreMode

import string, math, random

class ScoreModeTrans(object):
    def __init__(self, isAccomplished, currScore, currLevel):
        self.width = 800
        self.height = 600
        self.isPreAccomplished = isAccomplished
        # record the current game progress
        self.currScore = currScore
        self.currLevel = currLevel
        self.background=PhotoImage(file="image/ScoreModeTrans/background.gif")
        self.textX1, self.textY1 = self.width/2, self.height/2 -90
        self.textX2, self.textY2 = self.textX1, self.textY1 + 40
        self.textX3, self.textY3 = self.textX1, self.textY2 + 40



    def helpTimerFired(self, data):
        pass

    def helpKeyPressed(self, event, data):
        if self.isPreAccomplished:
            if event.keysym == "p":
                pass
                
        if event.keysym == "h":
            data.mode = data.helpMode
        if event.keysym == "r":
            init(data)

    def drawScoreModeTrans(self, canvas):
        self.redrawAll(canvas)
        
    # draw the transitory screen
    def redrawAll(self, canvas):
        self.drawBackground(canvas)
        self.createText(canvas)

    def drawBackground(self, canvas):
        canvas.create_image(self.width/2, self.height/2, image=self.background)

    def createText(self, canvas):
        # display different information based on 
        # the previous level
        if self.isPreAccomplished:
            text1 = "Congrats! You enter next level!"
            text2 = "Press  P to play next level!"
            text3 = "Press  R to restart!"
        else:
            text1 = "You didn't reach the goal!"
            text2 = "Press  R to restart!"
            text3 = "Press  H for help!"

        canvas.create_text(self.textX1, self.textY1, text = text1, 
                            font="Corbel 30", fill = "yellow")
        canvas.create_text(self.textX2, self.textY2, text = text2, 
                            font="Corbel 30", fill = "yellow")
        canvas.create_text(self.textX3, self.textY3, text = text3, 
                            font="Corbel 30", fill = "yellow")
















