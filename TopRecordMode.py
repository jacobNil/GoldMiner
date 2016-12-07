# The top record of all players


from tkinter import *
from Precious import Gold, Rock, Diamond, Rat, RatWithDiamond
from ScoreModeTrans import ScoreModeTrans
from Button import Button
from Miner import Miner


class RecordMode(object):
    def __init__(self, path="record.txt"):
        self.width = 800
        self.height = 600
        self.path = path
        # the records is a 2d-list of string with 
        # score record and users
        self.records = self.buildRecordsFromFile()
        # only keeo 6 best records
        self.maxRecordNum = 5
        self.buttons = []
        self.background = PhotoImage(
                    file="image/record/recordbackground800.gif")


    """
    The readFile() and writeFile() functions below are from course 
    page of 15112
    http://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    """
    # use formatted txt file to build record
    def buildRecordsFromFile(self):

        def readFile(path):
            with open(path, "rt") as f:
                return f.read()
        fileContet = readFile(self.path)
        records = []
        for line in fileContet.splitlines():
            if (line == ""): continue

            record = []
            for word in line.split():
                record.append(word)
            records.append(record)
        return records

    # if record is updated, save to file with format
    def saveRecordsToFile(self):

        def writeFile(path, contents):
            with open(path, "wt") as f:
                f.write(contents)

        contentsToWrite = ""
        for record in records:
            line = ""
            for item in record:
                if (len(line) == 0):
                    line += item 
                else:
                    line += " "+item
            contentsToWrite += line + "\n"
        writeFile(self.path, contentsToWrite)

    # check if a new score is good enough to be included
    def isInRecord(self, record):
        pass



    def createRecordButtons(self):
        height, width = self.height, self.width
        # the size of button is decided by the icon
        buttonHeight = 67
        buttonWidth = 240 
        numOfRecord = len(self.records)
        margin = (self.height-numOfRecord*buttonHeight-150)/(numOfRecord+1)

        for i in range(numOfRecord):
            x0 = width/2-buttonWidth/2
            y0 = i*buttonHeight + (i+1)*margin
            x1 = width/2+buttonWidth/2
            y1 = (i+1)*buttonHeight + (i+1)*margin
            rank = i +1
            text = str(rank)+" "+self.records[i][0]+": "+self.records[i][1]
            button = Button(x0, y0, x1, y1, None, text)
            self.buttons.append(button)

    # draw method
    def drawRecord(self, canvas, motioPosn):
        backgroundImage = self.background
        canvas.create_image(self.width/2, self.height/2, 
                            image= backgroundImage)
        self.createRecordButtons()
        for button in self.buttons:
            button.drawButton(canvas, motioPosn)

    # control method: help key pressed
    def recordModeHelpKeyPressed(self, event, data):
        if event.keysym == "r":
            data.mode = data.splashScreen


        

