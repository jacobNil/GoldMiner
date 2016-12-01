
from tkinter import *

import random, string

# super class for rock and gold
class Precious(object):
    def __init__(self, index=0, width=700, height0=300, height1=500):
        
        # height0 -- height1 define the undergound part, 
        # where the precious randomly distributed
        self.x = random.randint(100, width)
        self.y = random.randint(height0, height1)
        self.index = index
        self.image = [None] * 4 # types of gold and rock are 4
        self.highestSpeed = 50


    # detect if it is clawed by the miner
    def beenClawed(self, other):
        return False

    def __repr__(self):
        
        return "the precious is on (%d, %d)" %(self.x, self.y)

    # this function will be called in draw method. This will 
    # change the self.image and load it with the necessary image

    def loadImage(self):
        self.image[0] = PhotoImage(file="image/gold/gold0.gif")
        self.image[1] = PhotoImage(file="image/gold/gold1.gif")
        self.image[2] = PhotoImage(file="image/gold/gold2.gif")
        self.image[3] = PhotoImage(file="image/gold/gold3.gif")

    def __eq__(self, other):
        if ((isinstance(other, Gold)) and 
            (self.x == other.x) and 
            (self.y == other.y)):
            return True
        return False
    def drawPrecious(self, canvas):
        self.loadImage()
        for i in range(len(self.image)):
            if self.image[i] == None: pass

            canvas.create_image(100*(i+1), 100*(i+1), image=self.image[i])


####################################################################
### the Golds underground
####################################################################
"""
Gold:
* 4 different kinds gold:
                value         size         speed
    * gold0:    50*2^0=50     40*36        50
    * gold1:    50*2^1=100    70*63        40
    * gold2:    50*2^2=200    100*89       30
    * gold3:    50*2^3=400    130*116      20
* the value and the moving speed when get clawed
  can be calculate from the index of the gold
* the position of the gold is randomly distributed underground
"""

class Gold(Precious):
    def __init__(self, index):
        super().__init__(index)

        # the larger the index, the higher the value, 
        # the lower the speed in dragging
        
        self.radius = (40+self.index*30)/2
        self.value = 50*2**self.index
        self.speed = (50 - self.index*10)
        self.loadImage()

    def loadImage(self):
        self.image[0] = PhotoImage(file="image/gold/gold0.gif")
        self.image[1] = PhotoImage(file="image/gold/gold1.gif")
        self.image[2] = PhotoImage(file="image/gold/gold2.gif")
        self.image[3] = PhotoImage(file="image/gold/gold3.gif")

    # draw the object
    def drawGold(self, canvas):
        index = self.index
        canvas.create_image(self.x, self.y, image=self.image[index])
        # draw the circle around the gold,
        # should be removed in the final version
        #canvas.create_oval(self.x-self.radius, self.y-self.radius, 
        #                   self.x+self.radius, self.y+self.radius)

    def __repr__(self):
        
        return "the gold is on (%d, %d)" %(self.x, self.y)

####################################################################
### the rocks underground
####################################################################
        
"""
Rock:
* 4 different kinds gold:
                value         size         speed
    * rock0:    5*2^0=5     40*34        50
    * rock1:    5*2^1=10    50*51        40
    * rock2:    5*2^2=20    60*64        30
    * rock3:    5*2^3=40    70*85        20
* the value and the moving speed when get clawed
  can be calculate from the index of the gold
* the position of the gold is randomly distributed underground
"""

class Rock(Precious):
    def __init__(self, index):
        super().__init__(index)

        # the larger the index, the higher the value, 
        # the lower the speed in dragging
        self.value = 5*2*self.index
        self.speed = (50 - self.index*10)
        self.radius = 20+self.index*5
        self.loadImage()


    def loadImage(self):
        self.image[0] = PhotoImage(file="image/rock/rock40b.gif")
        self.image[1] = PhotoImage(file="image/rock/rock50.gif")
        self.image[2] = PhotoImage(file="image/rock/rock60b.gif")
        self.image[3] = PhotoImage(file="image/rock/rock70a.gif")

    def drawRock(self, canvas):
        index = self.index
        canvas.create_image(self.x, self.y, image=self.image[index])
        # draw the circle around the gold,
        # should be removed in the final version
        #canvas.create_oval(self.x-self.radius, self.y-self.radius, 
        #                   self.x+self.radius, self.y+self.radius)
        pass

    def __repr__(self):
    
        return "the Rock is on (%d, %d)" %(self.x, self.y)

####################################################################
### the diamond underground
####################################################################

class Diamond(object):
    def __init__(self, index=0, width = 800, height0 = 300, height1 = 600):
        # the coordinates should be random
        self.x = random.randint(0, width)
        self.y = random.randint(height0, height1)
        self.value = 500 # the value of dianmond
        self.radius = 10 # need to be modified

    def drawDiamond(self, canvas):
        # load picture and display here
        pass

####################################################################
### moving rats 
####################################################################

class Rat(object):
    def __init__(self, startX, startY, endX):
        self.startX, self.startY = startX, startY
        self.endX, self.endY = endX, startY
        self.speed = random.randint(5, 10)
        self.currX, self.currY = self.startX, self.startY
        self.value = 2
        self.radius = 10

    # the moving method of the rat
    def movingAround(self):
        self.startX += self.speed
        if ((self.currX>self.endX) or (self.currX < self.endX)):
            self.speed -= self.speed

    def drawRat(self, canvas):
        # draw rats here
        pass


























