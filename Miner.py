
#The class of Miner

from tkinter import *
from Precious import Gold, Rock, Diamond, Rat, RatWithDiamond
from ScoreModeTrans import ScoreModeTrans

import string, math, random


class Miner(object):
    def __init__(self):
        self.x = 405
        self.y = 60  # need to figure out
        # miner state and behaviro control
        self.regularImage = PhotoImage(
                        file="image/miner/regular150a.gif")
        self.workStateNum = 4
        self.workImage = [None]*self.workStateNum
        # four different working poses: down-up-downsweats-up
        #                               0    1  2          3
        self.workImage[0] = PhotoImage(
                        file="image/miner/workingDownSweat150a.gif")
        self.workImage[1] = PhotoImage(
                        file="image/miner/workingUp150.gif")
        self.workImage[2] = PhotoImage(
                        file="image/miner/workingDownSweat150a.gif")
        self.workImage[3] = PhotoImage(
                        file="image/miner/workingUp150.gif")

        self.congratsImage = PhotoImage(
                        file="image/miner/congrats150.gif")

        #miner state
        self.workCount = 0
        self.workCountHelper = 0
        self.congratsPeriod = 0
        self.itemValue = 0


    def drawMiner(self, canvas, other):
        # need to figure our the state of Claw
        # regular state of claw--> regular miner
        if (self.congratsPeriod==0):
            if ((other.claw.isClawStickOut==False)or
                (other.claw.clawStickSpeed>0)):
                self.drawRegularMiner(canvas)
            # claw coming our
            elif (other.claw.clawStickSpeed<0):
                self.drawWorkingMiner(canvas)
            # claw getting back with valuable precious
        else:
            self.drawCongratsMiner(canvas)

    def drawRegularMiner(self, canvas):
        
        canvas.create_image(self.x, self.y, image = self.regularImage)

    def drawWorkingMiner(self, canvas):
        index = self.workCount%self.workStateNum
        image = self.workImage[index]
        canvas.create_image(self.x, self.y, image = image)
        self.workCountHelper +=1
        self.workCount = self.workCountHelper//4

    def drawCongratsMiner(self, canvas):
        if self.itemValue > 50:
            canvas.create_image(self.x, self.y, image = self.congratsImage)
        else:
            self.drawRegularMiner(canvas)
        # draw the shining score
        self.drawShinningScore(canvas)

        self.congratsPeriod -= 1
        self.workCount = 0 # initialize work count
        self.workCountHelper = 0

    # draw the shinning score when get something
    def drawShinningScore(self, canvas):
        # position of score
        textX = 305
        textY = 45
        maxSize = 45
        scale = 8
        # font
        size = maxSize - scale*self.congratsPeriod
        textFont = "Helvetica " + str(size) + " italic"
        fill1="darkGreen"
        fill2="Red"
        scoreText = str(self.itemValue) + "!!"
        if (self.congratsPeriod%2 == 1):
            currFill = fill1
        else: currFill = fill2
        if (self.itemValue > 0):
            canvas.create_text(textX, textY, text=scoreText, 
                            font=textFont, fill = currFill)
        













