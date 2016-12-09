# the commodities for shopping mode
from tkinter import *

from Button import Button

import string, math, random


# the commodities for shopping mode
class Item(object):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        #image[0]--->regular
        #image[1]--->highlight
        self.image = [None]*2
        self.value = 0 # need to updated in each instance

    def drawItem(self, canvas, data):
        imageX = (self.x0+self.x1)/2
        imageY = (self.y0+self.y1)/2
        #determine if should be highlighted

        if self.isInItem(data.motionPosn):
            image = self.image[1]
            self.drawTextBoutPower(canvas)
        else:
            image = self.image[0]
        #print("item", imageX,imageY)

        canvas.create_image(imageX, imageY, image=image)

    def drawTextBoutPower(self, canvas):
        text1 = "Strength drink! The miner will reel up object faster on the"
        text2 = "next level. The Drink only lasts for one level"
        textX1, textY1 = 400, 500
        textX2, textY2 = 400, 535

        canvas.create_text(textX1, textY1, text= text1, fill="yellow",
                            font= "Corbel 27")
        canvas.create_text(textX2, textY2, text= text2, fill="yellow",
                            font= "Corbel 27")        


    def isInItem(self, motionPosn):
        (currX, currY)=motionPosn
        if ((currX>self.x0) and (currX<self.x1) and 
            (currY>self.y0) and (currY<self.y1)):
            return True
        return False

    ## need to work on!!
    def buyItem(self, event, data):
        click = (event.x, event.y)
        if isInItem(self, click):
            data.score -= self.value


class PowerDrink(Item):
    def __init__(self, x0, y0, x1, y1):
        super().__init__(x0, y0, x1, y1)
        self.value = 200
        self.loadImage()

    def loadImage(self):
        if (self.x1-self.x0>100):
            self.image[0]=PhotoImage(file=
                            "image/item/powerDrink120.gif")
            self.image[1]=PhotoImage(file=
                            "image/item/powerDrinkHighlight120.gif")        
        else:
            self.image[0]=PhotoImage(file=
                            "image/item/powerDrink40.gif")
            self.image[1]=PhotoImage(file=
                            "image/item/powerDrinkHighlight40.gif")        

















