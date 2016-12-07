
from tkinter import *

import random, string

# super class for rock and gold
class Precious(object):

    def __init__(self,index=0,width=800,height=600):
        # height0 -- height1 define the undergound part, 
        # where the precious randomly distributed
        self.margin = 50 # the margin of precious range
        self.width, self.height = width, height
        self.lBound = self.margin
        self.rBound = self.width-self.margin
        self.upBound = self.margin*6
        self.loBound = self.height-self.margin
        self.x=random.randint(self.lBound, self.rBound)
        self.y=random.randint(self.upBound, self.loBound)
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
        elif ((isinstance(other, Rock)) and 
            (self.x == other.x) and 
            (self.y == other.y)):
            return True
        return False

    # avoid the overlapping with other precious underground
    def isOverlapped(self, other):
        for precious in other:
            for item in precious:
                if ((self.x-item.x)**2 + (self.y-item.y)**2 
                    < (self.radius+item.radius)**2):
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
        self.speed = (50-self.index*10)
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
    def __init__(self, index=0, width = 800, height = 600):
        # the coordinates should be random
        self.margin = 50
        self.width, self.height = width, height
        self.lBound = self.margin
        self.rBound = self.width-self.margin
        self.upBound = self.margin*6
        self.loBound = self.height-self.margin
        self.x=random.randint(self.lBound, self.rBound)
        self.y=random.randint(self.upBound, self.loBound)
        self.value = 500 # the value of dianmond
        self.radius = 10 # need to be modified
        self.image = [None]*2
        self.loadImage()

    def loadImage(self):
        self.image[0] = PhotoImage(file="image/diamond/diamond1.gif")


    def drawDiamond(self, canvas):
        # load picture and display here
        radius = self.radius
        canvas.create_image(self.x, self.y, image=self.image[0])
        
    # detect if the precious is overlapped with other precious
    def isOverlapped(self, other):
        for precious in other:
            for item in precious:
                if ((self.x-item.x)**2 + (self.y-item.y)**2 
                    < (self.radius+item.radius)**2):
                    return True
        return False

####################################################################
### moving rats 
####################################################################

class Rat(object):
    def __init__(self, startX=50, startY=300, endX=550, endY=450):
        # define the possible range of start position
        self.travelDistance = random.randint(250, 450)
        self.startX, self.startY = startX, startY
        self.endX, self.endY = endX, endY
        direction = random.choice([-1, 1])
        self.speed = direction*random.randint(5, 10)
        self.x = random.randint(startX, endX) 
        self.y = random.randint(startY, endY)
        # the moving range of the rat
        self.leftRange = self.x-self.travelDistance/2
        self.rightRange = self.x+self.travelDistance/2

        # this properties cannot be directly inherited by 
        # other different kinds of rats
        self.value = 2
        self.radius = 18
        self.image = [None]*2
        self.loadImage()

    def loadImage(self):

        self.image[0] = PhotoImage(file="image/rat/rat40r.gif")
        self.image[1] = PhotoImage(file="image/rat/rat40l.gif")

    # the moving method of the rat
    def movingAround(self):
        self.x += self.speed
        if ((self.x>=self.rightRange) or (self.x <= self.leftRange)):
            self.x -= self.speed
            self.speed = -self.speed
            print("position of rat", self.x)
            print("speed", self.speed)

    def drawRat(self, canvas):
        # load picture and display here
        radius = self.radius
        # get the moving direction of the rats and load image 
        # accordingly
        if (self.speed > 0):
            image = self.image[0]
        else:
            image = self.image[1]

        canvas.create_image(self.x, self.y, image=image)
        #canvas.create_oval(self.x-radius, self.y-radius, 
                            #self.x+radius, self.y+radius)

    def __repr__(self):
        return ("the mouse is in %d, %d" %(self.x, self.y))



####################################################################
### moving rats with diamonds
####################################################################
# a subclass, inherit from class Rat.
# The difference is the image and value
class RatWithDiamond(Rat):
    def __init__(self):
        super().__init__(startX=200, startY=300, endX=600)

        self.value = 602 # the value is the sum of rat and diamond
        self.radius = 18
        self.image = [None]*2
        self.loadImage()

    def loadImage(self):
        self.image[0] = PhotoImage(file="image/rat/ratDiamond40r.gif")
        self.image[1] = PhotoImage(file="image/rat/ratDiamond40l.gif")






