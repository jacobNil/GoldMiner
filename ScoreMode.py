# contain all necessary data and method for 
# score mode of the game
from tkinter import *
from Precious import Gold, Rock, Diamond, Rat, RatWithDiamond
from ScoreModeTrans import ScoreModeTrans
from Item import Item, PowerDrink
from Claw import Claw
from Miner import Miner

import string, math, random

class ScoreMode(object):
    ##########################################
    # constructor and its helper method
    ##########################################
    def __init__(self, level=1, score=0, 
                 width=800, height=600, changeUnit=4):
        self.level,self.score = level, score
        self.isAccomplished = False
        self.goal = [500, 1000, 2500, 4500]
        self.width, self.height = width, height
        # for time control
        self.timeRemaining,self.msTime = 60, 10 # 60 senconds for each level
        # draw miner
        self.miner = Miner()
        # basic kinds of things underground
        self.groundLineY = 100
        self.ground = [None]*4
        self.loadGroundImage()
        self.golds, self.rocks, self.diamonds, self.rats = [],[],[],[]
        self.allPrecious = [self.golds, self.rocks,self.diamonds,self.rats]
        self.directory = dict()
        self.updataDirectiory()
        self.generateUnderground()
        # the miner is on the top center of the screen
        self.minerX, self.minerY = self.width/2, self.height/8
        self.minerR, self.clawChangeUnit = 40, changeUnit
        # draw the claw and other related feature
        # the claw can rotate from 210 digree to 330 digree        
        self.claw = Claw(self.minerX, self.minerY+10, self.width, self.height, 
                         changeUnit=changeUnit)
        self.powerIcon = PowerDrink(self.minerX+100,self.minerY-20,
                                    self.minerX+160,self.minerY+20)

        
    def loadGroundImage(self):
        self.ground[0] = PhotoImage(file=
                        "image/ScoreMode/background1.gif")
        self.ground[1] = PhotoImage(file=
                        "image/ScoreMode/background2n.gif")
        self.ground[2] = PhotoImage(file=
                        "image/ScoreMode/background3n.gif")
        self.ground[3] = PhotoImage(file=
                        "image/ScoreMode/background3n.gif")
        
    # use list to define the underground precious types and #
    # by using dictionary
    def updataDirectiory(self):
        # 1st level of the game: only rocks and golds
        # gold: 400*2, 200*2, 100*3, 50 *4
        # rock: 40 *1, 30*2,   20 * 2
                        #   XS  S  M  L
        self.directory[1] =[(1, 2, 2, 1), # gold#
                            (1, 1, 1, 1), # rock#
                            0,            # diamond#
                            1,            # rat# 
                            0]            # rat with diamond
        # second level
        self.directory[2] =[(2, 2, 2, 1),
                            (1, 2, 2, 0),
                            1,
                            0,
                            0
                            ] 
        # third level
        self.directory[3] =[(2, 2, 1, 1),
                            (3, 2, 2, 0),
                            3,
                            2,
                            2
                            ] 
        # fourth level
        self.directory[4] =[(3, 2, 0, 1),
                            (3, 2, 2, 0),
                            3,
                            4,
                            4] 
    # generate underground things for different level
    # according to the directory
    def generateUnderground(self):
        goldDir = self.directory[self.level][0]
        rockDir = self.directory[self.level][1]
        diamondNum = self.directory[self.level][2]
        ratNum = self.directory[self.level][3]
        RatWithDiamondNum = self.directory[self.level][4]
        # generate gold according to directory
        for i in range(len(goldDir)):
            for j in range(goldDir[i]):
                gold = Gold(index=i)
                while gold.isOverlapped(self.allPrecious):
                    gold = Gold(index=i)
                self.golds.append(gold)
        # generate rock according to directory
        for i in range(len(rockDir)):
            for j in range(rockDir[i]):
                rock = Rock(index=i)
                while rock.isOverlapped(self.allPrecious):
                    rock = Rock(index=i)
                self.rocks.append(rock)
        # generate diamond
        for i in range(diamondNum):
            diamond = Diamond()
            while diamond.isOverlapped(self.allPrecious):
                diamond = Diamond()
            self.diamonds.append(Diamond())
        # generate rat
        for i in range(ratNum):
            self.rats.append(Rat())
        # generate rat with diamond
        for i in range(RatWithDiamondNum):
            self.rats.append(RatWithDiamond())

    ##########################################
    # control method
    ##########################################
    def helpTimerFired(self, data):
        # basic: time running feature
        if (self.timeRemaining <= 0): 
            if self.score >= self.goal[self.level-1]:
                self.isAccomplished = True
                #print("isAccomplished=", self.isAccomplished)
                #print("currscore=", self.score)
                #print("score required",self.goal[self.level-1])

            data.mode = data.scoreModeTrans
            data.game = ScoreModeTrans(self.isAccomplished, 
                                self.score, self.level)
        for rat in self.rats:
            rat.movingAround()
            #print(rat)

        # time control and display
        self.msTime -= 1
        if (self.msTime) ==0 :
            self.timeRemaining -= 1
            self.msTime = 10
        # will get the clawed item.
        itemValue = self.claw.helpTimerFired(self.allPrecious)
        # when the claw is not stick out
        if itemValue != None:
            self.score += itemValue
            self.miner.congratsPeriod = 5
            self.miner.itemValue = itemValue

        #print("before",self.allPrecious)

        # when item is clawed, this item should be removed from
        # game mode, so the original item will disappear, and a 
        # new one will be created and draw as attached to the claw
        if (self.claw.clawedItem!=None):
            for precious in self.allPrecious:
                for item in precious:
                    if self.claw.clawedItem == item:
                        precious.remove(self.claw.clawedItem)
                        #print("after", self.allPrecious)
        
    def helpKeyPressed(self, event, data):
        if event.keysym == "r": 
            data.mode = data.splashScreen
        elif event.keysym == "Down":
            self.claw.isClawStickOut = True


    ##########################################
    # draw method
    ##########################################
    # draw the background for different level
    # backgound will change from level to level
    def drawScoreMode(self, canvas, data):
        self.drawBackground(canvas)
        self.drawPrecious(canvas)
        self.drawTimer(canvas)
        self.miner.drawMiner(canvas, self)
        self.claw.drawClaw(canvas)
        self.drawScore(canvas)
        if (self.clawChangeUnit==0):
            self.powerIcon.drawItem(canvas,data)


    def drawBackground(self, canvas):
        canvas.create_line(0, self.groundLineY, 
                    self.width, self.groundLineY)
        
        canvas.create_image(self.width/2, self.height/2, 
                            image=self.ground[self.level-1])
        pass

    # draw undergound precious
    def drawPrecious(self, canvas):
        for gold in self.golds:
            gold.drawGold(canvas)
        for rock in self.rocks:
            rock.drawRock(canvas)
        for diamond in self.diamonds:
            diamond.drawDiamond(canvas)
        for rat in self.rats:
            rat.drawRat(canvas)

    def drawTimer(self, canvas):
        timeX, timeY = 750, 55
        levelX, levelY = 750, 30
        alterBoxX0, alterBoxY0 = timeX+22, timeY-5
        alterBoxX1, alterBoxY1 = timeX+38, timeY+8
        timeText = "Time = " + str(self.timeRemaining) 
        levelText = "Level = " + str(self.level)
        if self.timeRemaining < 10:
            if self.timeRemaining%2==0:
                fill = "light blue"
            else: fill = "white"
            # the blingbling box on time
            canvas.create_rectangle(alterBoxX0, alterBoxY0, 
                                    alterBoxX1, alterBoxY1, 
                                    fill = fill, width = 0)
        canvas.create_text(levelX,levelY, text = levelText, 
                            font = "Corbel 20 bold")
        canvas.create_text(timeX, timeY, text = timeText, 
                            font = "Corbel 20 bold")

        
    #draw score and goal of leve on the left top corner
    def drawScore(self, canvas):
        scoreX, scoreY = 70, 30
        goalX, goalY = 70, 55
        moneyText = "Money = $" + str(self.score)
        canvas.create_text(scoreX, scoreY, text=moneyText, 
                            font = "Corbel 20 bold")
        goalText = "Goal = $" + str(self.goal[self.level-1])
        canvas.create_text(goalX, goalY, text = goalText, 
                            font = "Corbel 20 bold")




