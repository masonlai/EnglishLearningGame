import indexFrame
from util import tkObjLib as lib

if __name__ == '__main__':
    window = lib.getWindows("English Learning Game")
    displayFrame = lib.getFrame(window)
    indexFrame.setIndexFrame(displayFrame)
    displayFrame.pack()
    window.mainloop()
