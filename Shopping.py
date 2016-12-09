

from tkinter import *

from Button import Button
from Item import Item, PowerDrink
from Precious import Precious, Gold, Rock, Diamond, Rat, RatWithDiamond
import string, math, random


class ShopMode(object):
    def __init__(self, currScore=0, currLevel=0):
        # keep track of current score and level
        self.currLevel = currLevel
        self.currScore = currScore
        self.speedUnit = 0
        self.height=600
        self.width =800
        # about the basic elements of shopmode
        # shop owner, item, button, backgound
        self.background = PhotoImage(
                            file="image/Shop/shopBackground800n.gif")
        self.owner=Owner()
        self.buttonX0, self.buttonY0 = 640, 40
        self.buttonX1, self.buttonY1 = 760, 75
        buttonText = "Next Level"
        self.button = Button(self.buttonX0, self.buttonY0, 
                            self.buttonX1, self.buttonY1, 
                            "yellow", buttonText)
        self.itemX0, self.itemY0= 240, 300
        self.itemX1, self.itemY1= 360, 432
        self.item = PowerDrink(self.itemX0, self.itemY0, 
                                self.itemX1, self.itemY1)
        self.hasStrength=False
        self.angryTime = 10
        self.shopEnded = False
        x0, y0, x1, y1 = 140, 30, 200, 50
        self.powerIcon = PowerDrink(x0,y0,x1,y1)

    def drawShopMode(self, canvas, data):
        self.drawBackground(canvas, data)
        self.owner.drawOwner(canvas, data)
        self.item.drawItem(canvas, data)
        self.drawScore(canvas)
        if self.hasStrength:
            self.powerIcon.drawItem(canvas, data)


    def drawBackground(self, canvas, data):
        imageX = self.width/2
        imageY = self.height/2
        image = self.background
        distX, distY = -5, 83
        canvas.create_image(imageX, imageY, image=image)
        self.button.drawButton(canvas, data.motionPosn)
        priceX = distX+(self.itemX0+self.itemX1)/2
        
        priceY = distY+(self.itemY0+ self.itemY1)/2
        canvas.create_text(priceX, priceY, text="200$",
                fill="red", font="Helvetica 21")
        pass


    def shopModeKeyPressed(self, event, data):
        if event.keysym == "r":
            data.mode = data.splashScreen
            data.game = None
        pass

        #draw score and goal of leve on the left top corner
    def drawScore(self, canvas):
        scoreX, scoreY = 70, 40
      
        moneyText = "Money = $" + str(self.currScore)
        canvas.create_text(scoreX,scoreY,text=moneyText,fill="yellow", 
                            font = "Corbel 20 bold")
        


# the shop owner, withe different gestures and facial expression
class Owner(object):
    def __init__(self):
        self.angryOwner = PhotoImage(
                            file="image/owner/angryOwner200.gif")
        # 2 different states of owner
        self.regularOwner=[None]*2
        self.regularOwner[0]=PhotoImage(
                            file="image/owner/regularOwner200.gif")
        self.regularOwner[1]=PhotoImage(
                            file="image/owner/eyesClosedOwner200.gif")

    def drawOwner(self, canvas, data):
        #position of owner
        ownerX = 630
        ownerY = 335
        #print(data.motionPosn)
        # the state of onner is randomly chosed
        stateDecider = 0.8
        state = random.random()
        if state>stateDecider:
            image = self.regularOwner[1]
        else:
            image = self.regularOwner[0]

        canvas.create_image(ownerX, ownerY, image=image)







