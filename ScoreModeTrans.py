
# the object draw the score mode transition screen
# the screen will shown when one level of score mode 
# is finished. The screen will shown different content
# based on the level is accomplished or not

from tkinter import *
from Precious import Gold, Rock
from Button import Button
from Shopping import ShopMode, Owner
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
        self.background=PhotoImage(file=
                        "image/ScoreModeTrans/background.gif")
        self.textX1, self.textY1 = self.width/2, self.height/2 -90
        self.textX2, self.textY2 = self.textX1, self.textY1 + 40
        self.textX3, self.textY3 = self.textX1, self.textY2 + 40
        self.playerName = ""
        self.defaultName = "42"
        self.breakRecord = False
        buttonX0, buttonY0 = 280, 416
        buttonX1, buttonY1 = 520, 484
        self.shopButton = Button(buttonX0, buttonY0, 
                        buttonX1, buttonY1,None, "Go Shopping")
        self.showShoppingButton = False

    def helpTimerFired(self, data):
        pass
    """
    def helpKeyPressed(self, event, data):
        if self.isPreAccomplished:
            if event.keysym == "p":
        if event.keysym == "h":
            data.mode = data.helpMode
        if event.keysym == "r":
            init(data)
    """

    def helpMousePressed(self, event, data):
        if self.showShoppingButton:
            clickX, clickY =event.x, event.y
            if self.shopButton.clickInButton(clickX, clickY):
                data.mode = data.shopMode
                data.game=ShopMode(self.currScore,self.currLevel)

    def drawScoreModeTrans(self, canvas, data):
        self.redrawAll(canvas, data)
        
    # draw the transitory screen
    def redrawAll(self, canvas, data):
        self.drawBackground(canvas)
        if self.breakRecord==False:
            if ((self.isPreAccomplished) and 
                (self.currLevel<4)):
                self.drawEnterNextLevelAndShop(canvas, data)
            elif (self.currLevel<4):
                self.drawFailRestart(canvas)
            elif ((self.currLevel == 4) and 
                  (self.isPreAccomplished)):
                if data.record.isInRecord(self.currScore):
                    self.breakRecord = True
        else:
            self.drawEnterRecord(canvas)


    def drawEnterRecord(self, canvas):
        text1 = "You are one of top players!" 
        text2 = "Please Leave Your Name"
        text3 = "Name: __________"
        self.drawText(canvas, text1, text2, text3)
        text4 = self.playerName
        textX4 = self.textX3 + 20
        textY4 = self.textY3
        canvas.create_text(textX4, textY4, text=text4,
                           font = "Corbel 30 bold", fill = "Green" )


    def drawBackground(self, canvas):
        canvas.create_image(self.width/2, self.height/2, 
                            image=self.background)

    def drawEnterNextLevelAndShop(self, canvas,data):
        text1 = "Congrats! You enter next level!"
        text2 = "Press  P to play next level!"
        text3 = "Press  R to restart!"
        # create a button here to enter shop
        self.shopButton.drawButton(canvas, data.motionPosn)
        self.showShoppingButton=True
        self.drawText(canvas, text1, text2, text3)

    def drawFailRestart(self, canvas):
        text1 = "You didn't reach the goal!"
        text2 = "Press  R to restart!"
        text3 = "Press  H for help!"
        self.drawText(canvas, text1, text2, text3)

 
    def drawText(self, canvas, text1, text2, text3):

        canvas.create_text(self.textX1, self.textY1, text = text1, 
                            font="Corbel 30", fill = "yellow")
        canvas.create_text(self.textX2, self.textY2, text = text2, 
                            font="Corbel 30", fill = "yellow")
        canvas.create_text(self.textX3, self.textY3, text = text3, 
                            font="Corbel 30", fill = "yellow")





