import tkinter as tk
import tkinter.scrolledtext as st

defaultPosition = {"padx": 0, "pady": 0}


def getWindows(title, geometry="800x600", background="white"):
    window = tk.Tk()
    window.title(title)
    window.geometry(geometry)
    window.configure(background=background)
    return window


def setHeader(frame, text, font, background="white", positionCfg={}, **kwargs):
    cnf = {"text": text, "font": font, "background": background}
    cnf.update(kwargs)
    header = tk.Label(master=frame, cnf=cnf)
    header.pack(positionCfg)
    return header


def setTextLabel(frame, text, background="white", positionCfg={}, **kwargs):
    cnf = {"text": text, "background": background}
    cnf.update(kwargs)
    TextLabel = tk.Label(frame, cnf=cnf)
    TextLabel.pack(positionCfg)
    return TextLabel


def setScrolledText(frame, text, width, height, positionCfg={}, ):
    scrolledText = st.ScrolledText(frame, width=width, height=height)
    scrolledText.insert(tk.INSERT, text)
    scrolledText.pack(positionCfg)
    return scrolledText


def setAnsInput(frame, limit=10, background="white", positionCfg={}, **kwargs):
    cnf = {"background": background}
    cnf.update(kwargs)

    def limitSize(*args):
        value = fieldValue.get()
        if len(value) > limit: fieldValue.set(value[:limit])

    fieldValue = tk.StringVar()
    fieldValue.trace('w', limitSize)

    inputField = tk.Entry(frame, cnf=cnf, textvariable=fieldValue)
    inputField.pack(positionCfg)

    return inputField, fieldValue


def getFrame(window, background="white", **kwargs):
    cnf = {"background": background}
    cnf.update(kwargs)
    frame = tk.Frame(window, cnf=cnf)
    frame.pack()
    return frame


def setBtn(frame, text, command=None, background="white", positionCfg={}, **kwargs):
    cnf = {"text": text, "command": command, "background": background}
    cnf.update(kwargs)
    btn = tk.Button(frame, cnf=cnf)
    btn.pack(positionCfg)
    return btn


def createRanking(records):
    root = tk.Tk()
    root.title("Ranking")

    font = ("Terminal", 15, "bold")

    b = tk.Label(root, text="Name", background="gray66", font=font)
    b.grid(row=0, column=0, sticky="nsew")

    b = tk.Label(root, text="Score", background="gray66", font=font)
    b.grid(row=0, column=1, sticky="nsew")

    b = tk.Label(root, text="date", background="gray66", font=font)
    b.grid(row=0, column=2, sticky="nsew")

    for i, data in enumerate(records):
        if i % 2 == 0:
            bg = "white"
        else:
            bg = "gray66"

        for j, DetailsOfData in enumerate(data):
            b = tk.Label(root, text=DetailsOfData, background=bg, font=font)
            b.grid(row=i + 1, column=j, sticky="nsew")

    tk.mainloop()

def clearFrame(displayFrame):
    for widget in displayFrame.winfo_children():
        widget.pack_forget()