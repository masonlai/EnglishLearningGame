from util import tkObjLib as lib
from games import reorganize_word, word_Gussing, vocabulary_game
import tkinter as tk
import art

btnWidth = 25
btnHeight = 4

askNamePositionCfg = {"pady": 40}
askNameEntryFont = ("Terminal", 20, "bold")

confirmNameBtnPositionCfg = {"pady": 40}
confirmNameBtnFont = ("Terminal", 15, "bold")

headerPositionCfg = {"pady": 40}
headerFont = ("Terminal", 60, "bold")

namePositionCfg = {"pady": 40}
nameFont = ("Terminal", 30, "bold")

btnPositionCfg = {"padx": 10, "pady": 10}

iconPositionCfg = {"pady": 0}
iconFont = ("monospace", 10)

warningPositionCfg = {"pady": 0}
warningWordFont = ("Terminal", 5)
warningArtFont = ("monospace", 5)

pudding = """───────────────────────────────────────
───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────
───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────
──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────
▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───
▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────
─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────
──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐──────
──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────
────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────"""

warning = """

             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
  u$$$$       $$$$$u$u$u$$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$uu    *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*                         $$$$*

"""


def setIndexFrame(displayFrame):
    mainFram = lib.getFrame(displayFrame)
    askName(mainFram)


def askName(mainFram):
    lib.setTextLabel(mainFram, "Hi there, what is your name?", font=askNameEntryFont, positionCfg=askNamePositionCfg)
    nameEntryVar = tk.StringVar()
    nameEntry, value = lib.setAnsInput(mainFram, limit=20, font=askNameEntryFont, textvariable=nameEntryVar)
    confirmBtn = lib.setBtn(mainFram, "Confirm", font=confirmNameBtnFont, positionCfg=confirmNameBtnPositionCfg,
                            command=lambda: confirmName())

    def enterEvent(event):
        confirmBtn.invoke()

    def confirmName():
        name = nameEntry.get()
        if name != "":
            player = Player(name)
            lib.clearFrame(mainFram)
            genIndexBtn(player, mainFram)
        else:
            lib.setTextLabel(mainFram, art.text2art("NAME!!!", font="block", chr_ignore=True), font=warningWordFont,
                             positionCfg=warningPositionCfg)
            cat.pack_forget()
            lib.setTextLabel(mainFram, warning, font=warningArtFont, positionCfg=warningPositionCfg)

    nameEntry.bind('<Return>', enterEvent)

    # lib.setTextLabel(mainFram, text2art("Mason", chr_ignore=True), font=iconFont, positionCfg=iconPositionCfg)
    cat = lib.setTextLabel(mainFram, pudding, font=iconFont, positionCfg=iconPositionCfg)


def genIndexBtn(player, mainFram):
    lib.setHeader(mainFram, "HiThere:)", font=headerFont, positionCfg=headerPositionCfg)

    lib.setHeader(mainFram, player.getMsg(), font=nameFont, positionCfg=namePositionCfg)

    lib.setBtn(frame=mainFram, text="SPELLING GAME", positionCfg=btnPositionCfg,
               command=lambda: WGG(mainFram, player),
               height=btnHeight, width=btnWidth)
    lib.setBtn(frame=mainFram, text="REORGANIZE WORD", positionCfg=btnPositionCfg,
               command=lambda: ROG(mainFram, player), height=btnHeight, width=btnWidth)
    lib.setBtn(frame=mainFram, text="VOCABULARY GAME", positionCfg=btnPositionCfg,
               command=lambda: VBG(mainFram, player), height=btnHeight, width=btnWidth)


def WGG(displayFrame, player):
    lib.clearFrame(displayFrame)
    word_Gussing.setWGGFrame(displayFrame, player)


def ROG(displayFrame, player):
    lib.clearFrame(displayFrame)
    reorganize_word.setROGFrame(displayFrame, player)


def VBG(displayFrame, player):
    lib.clearFrame(displayFrame)
    vocabulary_game.setVBGFrame(displayFrame, player)


class Player:
    def __init__(self, name):
        self.name = name

    def getMsg(self):
        return ("Player: {name}").format(
            name=self.name)
