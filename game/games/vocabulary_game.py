import random
from game import indexFrame
from game.util import tkObjLib as lib, dbUtil
from random_words import RandomWords
from datetime import datetime
from PyDictionary import PyDictionary
import tkinter as tk

dictionary = PyDictionary()

chance4fail = 5

ScorePositionCfg = {"side": "bottom", "pady": 20}
ScoreFont = ("Terminal", 20, "bold")

headerPositionCfg = {"pady": 40}
headerFont = ("Terminal", 25, "bold")

questionPositionCfg = {"pady": 20}
questFont = ("Terminal", 20, "bold")

inputFont = ("Terminal", 20)

ansBtnFont = ("Terminal", 20)
ansBtnFontPositionCfg = {"padx": 20, "pady": 20, "side": "left", "expand": False}

# hintFont = ("Terminal", 15)
hintPositionCfg = {"pady": 20}


class FailCount:
    def __init__(self, chance4fail):
        self.chance4fail = chance4fail

    def getMsg(self):
        return (
            "Welcome to vaocabulary game!\nYou have {chance4fail} chances to fail! \nChoice one which matches \nthe meaning of the dictionary").format(
            chance4fail=self.chance4fail)

    def fail(self):
        self.chance4fail = self.chance4fail - 1


class ScoreCount:
    def __init__(self):
        self.score = 0

    def getMsg(self):
        return ("Score: {score}").format(
            score=self.score)

    def nextStage(self):
        self.score = self.score + 1


def setVBGFrame(mainFram, player):
    failCount = FailCount(chance4fail)
    scoreCount = ScoreCount()

    displayScore = lib.setTextLabel(mainFram, scoreCount.getMsg(), font=ScoreFont, positionCfg=ScorePositionCfg)

    header = lib.setHeader(mainFram, failCount.getMsg(), font=headerFont, positionCfg=headerPositionCfg)

    possibleAns, ans, definition = getQuestion()

    definitionDisplay = lib.setScrolledText(mainFram, definition, width=70,
                                            height=10, positionCfg=hintPositionCfg)

    definitionDisplay.configure(state='disabled')

    ansFrame = lib.getFrame(mainFram)

    genBtn4Ans(ansFrame, possibleAns, ans, header,
               failCount,
               scoreCount,
               displayScore, player,
               mainFram,
               definitionDisplay)


def genBtn4Ans(ansFrame, questions, ans, header,
               failCount,
               scoreCount,
               displayScore, player,
               mainFram,
               definitionDisplay):
    for i in questions:
        lib.setBtn(ansFrame, i, font=ansBtnFont, positionCfg=ansBtnFontPositionCfg,
                   command=lambda btnValue=i: btnEvent(btnValue))

    def btnEvent(btnValue):
        validateAns(ans, btnValue, header,
                    failCount,
                    scoreCount,
                    displayScore, player,
                    mainFram,
                    definitionDisplay,
                    ansFrame)


def getQuestion():
    rw = RandomWords()
    ans = rw.random_word()
    fakeAns = 2
    definition = dictionary.meaning(ans)
    print(definition)
    print(ans)

    possibleAns = []
    possibleAns.append(ans)

    for i in range(fakeAns):
        fake = rw.random_word()
        possibleAns.append(fake)

    random.shuffle(possibleAns)

    question = reorganize(ans)
    return possibleAns, ans, definition


def reorganize(word4game):
    word4game = list(word4game)
    random.shuffle(word4game)
    question = "".join(word4game)
    return question


def validateAns(ans, bntValue, header,
                failCount,
                scoreCount,
                displayScore, player,
                mainFram,
                definitionDisplay,
                ansFrame):
    usersAns = bntValue

    if ans.lower() == usersAns.lower():
        nextStage(ansFrame, header, failCount, scoreCount, displayScore,
                  player, mainFram, definitionDisplay)
    else:
        fail(header, failCount, scoreCount, player, mainFram)


def nextStage(ansFrame, header,
              failCount,
              scoreCount,
              displayScore, player,
              mainFram,
              definitionDisplay):
    possibleAns, ans, definition = getQuestion()

    definitionDisplay.configure(state='normal')
    definitionDisplay.delete('1.0', tk.END)
    definitionDisplay.insert(tk.INSERT, definition)
    definitionDisplay.configure(state='disabled')

    scoreCount.nextStage()
    displayScore.configure(text=scoreCount.getMsg())

    lib.clearFrame(ansFrame)

    genBtn4Ans(ansFrame, possibleAns, ans, header,
               failCount,
               scoreCount,
               displayScore, player,
               mainFram,
               definitionDisplay)


def fail(header, failCount, scoreCount, player, mainFram):
    failCount.fail()
    if failCount.chance4fail <= 0:
        dbUtil.updateVBG(player.name, scoreCount.score, datetime.now().strftime("%m/%d/%Y"))
        rows = dbUtil.top10VBG()
        lib.clearFrame(mainFram)
        indexFrame.genIndexBtn(player, mainFram)
        lib.createRanking(rows)
    else:
        header.configure(text=failCount.getMsg())
