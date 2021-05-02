import random
from game import indexFrame
from game.util import tkObjLib as lib, dbUtil
from random_words import RandomWords
from datetime import datetime
from PyDictionary import PyDictionary
import tkinter as tk

dictionary = PyDictionary()

hiddenSymbol = "_"
chance4fail = 5

ScorePositionCfg = {"side": "bottom", "pady": 20}
ScoreFont = ("Terminal", 20, "bold")

headerPositionCfg = {"pady": 40}
headerFont = ("Terminal", 25, "bold")

questionPositionCfg = {"pady": 20}
questFont = ("Terminal", 20, "bold")

inputFont = ("Terminal", 20)

ansBtnFont = ("Terminal", 20)
ansBtnFontPositionCfg = {"pady": 20, "side": "bottom", "expand": False}

# hintFont = ("Terminal", 15)
hintPositionCfg = {"pady": 20}


class FailCount:
    def __init__(self, chance4fail):
        self.chance4fail = chance4fail

    def getMsg(self):
        return ("Welcome to spelling game!\nYou have {chance4fail} chances to fail").format(
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


class QuestionGenerator:
    def __init__(self, question):
        self.question = question

    def getMsg(self):
        return ("Question: {question}").format(
            question=self.question)


def setWGGFrame(mainFram, player):
    failCount = FailCount(chance4fail)
    scoreCount = ScoreCount()

    displayScore = lib.setTextLabel(mainFram, scoreCount.getMsg(), font=ScoreFont, positionCfg=ScorePositionCfg)

    header = lib.setHeader(mainFram, failCount.getMsg(), font=headerFont, positionCfg=headerPositionCfg)

    question, ansLetter, hint = getQuestion()
    questionGenerator = QuestionGenerator(question)
    displayQuestion = lib.setTextLabel(mainFram, questionGenerator.getMsg(), font=questFont,
                                       positionCfg=questionPositionCfg)

    inputField, fieldValue = lib.setAnsInput(mainFram, limit=1, font=inputFont, width=2)
    hintDisplay = lib.setScrolledText(mainFram, hint, width=70,
                                      height=10, positionCfg=hintPositionCfg)

    hintDisplay.configure(state='disabled')

    ansBtn = lib.setBtn(mainFram, "Check", font=ansBtnFont, positionCfg=ansBtnFontPositionCfg,
                        command=lambda: validateAns(ansLetter, inputField, header,
                                                    failCount,
                                                    displayQuestion,
                                                    ansBtn, scoreCount,
                                                    questionGenerator,
                                                    displayScore, player,
                                                    mainFram, fieldValue,
                                                    hintDisplay))

    def enterEvent(event):
        ansBtn.invoke()

    inputField.bind('<Return>', enterEvent)


def getQuestion():
    rw = RandomWords()
    word4game = rw.random_word()
    hint = dictionary.meaning(word4game)
    print(hint)
    print(word4game)
    question, ansLetter = word_to_underscore(word4game)
    return question, ansLetter, hint


def word_to_underscore(word4game):
    word4game = list(word4game)
    random_index = random.randint(0, len(word4game) - 1)
    ansLetter = word4game[random_index]
    word4game[random_index] = hiddenSymbol
    word4game = "".join(word4game)
    return word4game, ansLetter


def validateAns(ansLetter, inputField, header, failCount, displayQuestion, ansBtn, scoreCount, questionGenerator,
                displayScore, player, mainFram, fieldValue, hintDisplay):
    usersAns = inputField.get()
    if ansLetter.lower() == usersAns.lower():
        nextStage(displayQuestion, ansBtn, inputField, header, failCount, scoreCount, questionGenerator, displayScore,
                  player, mainFram, fieldValue, hintDisplay)
    else:
        fail(header, failCount, scoreCount, player, mainFram)


def nextStage(displayQuestion, ansBtn, inputField, header, failCount, scoreCount, questionGenerator, displayScore,
              player, mainFram, fieldValue, hintDisplay):
    question, ansLetter, hint = getQuestion()
    questionGenerator.question = question
    displayQuestion.configure(text=questionGenerator.getMsg())

    hintDisplay.configure(state='normal')
    hintDisplay.delete('1.0', tk.END)
    hintDisplay.insert(tk.INSERT, hint)
    hintDisplay.configure(state='disabled')

    scoreCount.nextStage()
    displayScore.configure(text=scoreCount.getMsg())

    fieldValue.set("")

    ansBtn.configure(command=lambda: validateAns(ansLetter, inputField, header,
                                                 failCount,
                                                 displayQuestion,
                                                 ansBtn, scoreCount,
                                                 questionGenerator,
                                                 displayScore, player,
                                                 mainFram, fieldValue,
                                                 hintDisplay))


def fail(header, failCount, scoreCount, player, mainFram):
    failCount.fail()
    if failCount.chance4fail <= 0:
        dbUtil.updateWGG(player.name, scoreCount.score, datetime.now().strftime("%m/%d/%Y"))
        rows = dbUtil.top10WGG()
        lib.clearFrame(mainFram)
        indexFrame.genIndexBtn(player, mainFram)
        lib.createRanking(rows)
    else:
        header.configure(text=failCount.getMsg())
