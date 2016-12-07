from tkinter import *
from Precious import Gold, Rock, Diamond, Rat, RatWithDiamond
from ScoreModeTrans import ScoreModeTrans

import string, math, random


##################################################################
##the class of Claw, with basic feature of stick out
##################################################################

class Claw(object):
    def __init__(self, startX, startY, width, height):
        self.handStartX, self.handStartY = startX, startY
        self.width, self.height = width, height
        self.currAngle = math.pi*3/2
        self.minAngle, self.maxAngle = math.pi*13/12, math.pi*23/12
        self.angleSpeed = math.pi/48
        self.initHandLength = 30
        self.handLength = self.initHandLength
        self.handEndX = self.handStartX-math.cos(self.currAngle)*self.handLength
        self.handEndY = self.handStartY-math.sin(self.currAngle)*self.handLength

        self.clawLaneLength = 15
        self.lenDifference = 5 # the difference between 2 states
        self.fingerLength = 10
        self.isClawStickOut = False
        self.clawStickSpeed = 18

        # about the dectect point of the claw
        self.finger1StartX = None
        self.finger1StartY = None
        self.finger1EndX = None
        self.finger1EndY = None
        self.finger2StartX = None
        self.finger2StartY = None
        self.finger2EndX = None
        self.finger2EndY = None
        # about claw behavior
        self.isClawed = False
        self.clawedItem = None


    ##############################################################
    # draw method
    ##############################################################

    # draw claw and hand of claw
    def drawClaw(self, canvas):
        # the claw hand can rotate from 210 digree to 330 digree
        handStartX, handStartY = self.handStartX, self.handStartY
        currAngle = self.currAngle
        handLength = self.handLength
        angleSpeed = self.angleSpeed
        handEndX = (self.handStartX-
                        math.cos(self.currAngle)*self.handLength)
        handEndY = (self.handStartY-
                        math.sin(self.currAngle)*self.handLength)
        self.handEndX, self.handEndY = handEndX, handEndY
        # the claw lane is vertical to the claw hand
        if self.clawedItem == None:
            clawLaneLength = self.clawLaneLength
        else:
            clawLaneLength = self.clawLaneLength - self.lenDifference
        clawLaneTheta1 = currAngle+math.pi/2
        clawLaneTheta2 = currAngle-math.pi/2
        clawLaneStartX = handEndX-math.cos(clawLaneTheta1)*clawLaneLength
        clawLaneStartY = handEndY-math.sin(clawLaneTheta1)*clawLaneLength
        clawLaneEndX = handEndX-math.cos(clawLaneTheta2)*clawLaneLength
        clawLaneEndY = handEndY-math.sin(clawLaneTheta2)*clawLaneLength
        # the claw fingers
        # finger1 start from the clawLaneStartX, Y
        fingerLength = self.fingerLength
        finger1StartX, finger1StartY = clawLaneStartX, clawLaneStartY
        finger1Theta = currAngle+math.pi/6
        finger1EndX = finger1StartX-math.cos(finger1Theta)*fingerLength
        finger1EndY = finger1StartY-math.sin(finger1Theta)*fingerLength
        # finger1 start from the clawLaneStartX, Y        
        finger2StartX, finger2StartY = clawLaneEndX, clawLaneEndY
        finger2Theta = currAngle - math.pi/6
        finger2EndX = finger2StartX-math.cos(finger2Theta)*fingerLength
        finger2EndY = finger2StartY-math.sin(finger2Theta)*fingerLength
        self.finger1StartX = finger1StartX
        self.finger1StartY = finger1StartY
        self.finger1EndX = finger1EndX
        self.finger1EndY = finger1EndY

        self.finger2StartX = finger2StartX
        self.finger2StartY = finger2StartY
        self.finger2EndX = finger2EndX
        self.finger2EndY = finger2EndY
        # draw claow hand
        canvas.create_line(handStartX, handStartY, handEndX, handEndY, 
                            fill = "black", width = 2)
        # draw clawlane
        canvas.create_line(clawLaneStartX, clawLaneStartY, 
                            clawLaneEndX, clawLaneEndY, width=2)
        # draw 2 claw fingers
        # finger 1
        canvas.create_line(finger1StartX, finger1StartY, 
                            finger1EndX, finger1EndY, width=2)
        # draw the clawed item, when it was clawed
        self.drawClawedItem(canvas)
        #draw finger 2
        canvas.create_line(finger2StartX, finger2StartY, 
                            finger2EndX, finger2EndY, width=2)   

    # draw the clawed item, when it was clawed
    def drawClawedItem(self, canvas):
        # only deal with the conditon that sth is clawed
        if self.clawedItem == None:
            return None
        elif (self.clawedItem != None):
            #print("drawing clawed item")
            itemR = self.clawedItem.radius
            itemDistance = self.handLength+itemR
            self.clawedItem.x = (self.handStartX-
                        math.cos(self.currAngle)*itemDistance)
            self.clawedItem.y = (self.handStartY-
                        math.sin(self.currAngle)*itemDistance)

            if isinstance(self.clawedItem, Gold):
                self.clawedItem.drawGold(canvas)
            elif isinstance(self.clawedItem, Rock):
                self.clawedItem.drawRock(canvas)
            elif isinstance(self.clawedItem, Diamond):
                self.clawedItem.drawDiamond(canvas)
            # be careful about the order of two rat class
            # need to check RatWithDiamond First
            elif isinstance(self.clawedItem, RatWithDiamond):
                self.clawedItem.drawRat(canvas)
            elif isinstance(self.clawedItem, Rat):
                self.clawedItem.drawRat(canvas)
            

    ##############################################################
    # claw behavior
    ##############################################################
    def clawRotate(self):
        if ((self.currAngle <= self.minAngle) or 
            (self.currAngle >= self.maxAngle)):
            self.angleSpeed = - self.angleSpeed
        elif (self.currAngle >= self.maxAngle):
            self.currAngle -= self.angleSpeed
        self.currAngle += self.angleSpeed



    def clawStickOut(self):
        # check if the claw got something, 
        # if it does, retract immediately
        if ((self.clawedItem!=None) and (self.clawStickSpeed>0)):
            self.clawStickSpeed = -self.clawStickSpeed

        #print("self.clawedItem", self.clawedItem)
        #print("self.clawStickSpeed", self.clawStickSpeed)
        self.handLength += self.clawStickSpeed
        # the regular claw stick out behavior
        # stick out until the bound of the interface and
        # then retract
        if (self.clawStickSpeed > 0):
            speed = self.clawStickSpeed
            if ((self.handEndX<0) or (self.handEndX>self.width-speed) or
                (self.handEndY<0+speed) or (self.handEndY>self.height-speed)):
                self.clawStickSpeed = -self.clawStickSpeed   
        else: 
            if self.handLength < self.initHandLength:
                    self.handLength = self.initHandLength
                    self.isClawStickOut = False
                    # get the
                    value = 0
                    if (self.clawedItem!=None):
                        value = self.clawedItem.value
                    self.clawedItem = None
                    print("the current clawed=", self.clawedItem)
                    self.clawStickSpeed = -self.clawStickSpeed
                    return value

    ##############################################
    # claw behavior
    ##############################################
    def helpTimerFired(self, currPrecious):
        if (not self.isClawStickOut):
            self.clawRotate()

        else: # when the claw is out
            value = self.clawStickOut()
            if (self.clawedItem!=None):
                # do something
                self.clawStickSpeed=-math.fabs(self.clawStickSpeed)

            elif ((self.clawedItem==None) and 
                (self.clawStickSpeed>0)):
                self.clawedItem = self.whichItemClawed(currPrecious)
                return value

    # check and return the item that clawed
    # if None iterm is clawed, return none
    def whichItemClawed(self, currPrecious):
        for precious in currPrecious:
            for item in precious:
                if self.isclawContacted(item):
                    print("the current clawed",item)
                    return item
        return None

    def isclawContacted(self, item):
        # calculate and find the detect points, 
        # which are on the end of claw finger and 
        # the center of 2 claw fingers and the hand end
        detect1X = self.finger1EndX
        detect1Y = self.finger1EndY
        detect2X = self.finger2EndX
        detect2Y = self.finger2EndY
        detect3X = self.handEndX
        detect3Y = self.handEndY

        clawDetectPoint = [ (detect1X, detect1Y), 
                            (detect2X, detect2Y),
                            (detect3X, detect3Y)]
        #print("detectpoint=", clawDetectPoint)
        for point in clawDetectPoint:
            if self.pointInCircle(point, item):
                return True
        return False
    # a helper function
    # generally return true if the point=(x, y) are in the circcle
    # define as (item.x, item.y, item.radiu)
    @staticmethod
    def pointInCircle(point, item):
        dist = (point[0]-item.x)**2 + (point[1]-item.y)**2
        dist = math.sqrt(dist)
        return (dist<item.radius)


         
            