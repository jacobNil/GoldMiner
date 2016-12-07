# The top record of all players


from tkinter import *
from Precious import Gold, Rock, Diamond, Rat, RatWithDiamond
from ScoreModeTrans import ScoreModeTrans
from Claw import Claw
from Miner import Miner


class TopRecordMode(object):
    def __init__(self, path="record.txt"):
        self.path = path
        fileContent = readFile(path)

    @staticmethod
    def readFile(path):
        with open(path, "rt") as f:
            return f.read()
            
    @staticmethod
    def writeFile(path, contents):
        with open(path, "wt") as f:
            f.write(contents)