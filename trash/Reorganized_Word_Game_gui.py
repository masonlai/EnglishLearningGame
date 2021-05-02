# Reorganized Word Game
# Done!
import tkinter as tk
import random as rd
index = 0
ans = shuffledWord = inputWord = None
wordsList = ["apple", "bacon", "banana", "cake", "fish"]
score = 0


def game3():
    def displayWords():
        global ans, shuffledWord, wordsList
        wordsList = ["apple", "bacon", "banana", "cake", "fish"]
        ans = wordsList[index]
        listString = list(ans)
        shuffledWord = "".join(rd.sample(listString, len(listString)))
        result = str(shuffledWord)
        display_init.configure(text=result)

    def checkAns():
        global index, score
        var_text = text_entry.get()
        if var_text == ans:
            result = "Doing well! Let's go to the other words."
            output_label.configure(text=result)
            score = int(score) + 1
            score_label.configure(text="Score: " + str(score))
            if index == (len(wordsList)-1):
                btn["state"] = "disabled"
            else:
                index += 1
                return displayWords()
        else:
            result = "Sorry for that it's not the correct answer. \nPlease try it again!!"
            output_label.configure(text=result)
            return displayWords()

##############################
    window = tk.Tk()
    window.title("Reorganized Word Game")
    window.geometry("800x600")
    window.configure(background="white")
    header = tk.Label(window, text="Welcome", font=("Courier", 15), bg="white")
    header.pack()
    score_label = tk.Label(window, font=("Courier", 20), bg="white")
    score_label.place(relx=1.0, rely=0.0, anchor="ne")
# Entry text part
    text_frame = tk.Frame(window, background="white")
    text_frame.pack()
    display_init = tk.Label(text_frame, font=("Courier", 15), bg="white")
    display_init.pack()
    # Enter text label
    input_label = tk.Label(text_frame, text="Please enter a reorganized word on below text box", font=(
        "Courier", 15), bg="white")
    input_label.pack()
    text_label = tk.Label(text_frame, text="Input: ",
                          font=("Courier", 15), bg="white")
    text_label.pack()
    text_entry = tk.Entry(text_frame)
    text_entry.pack()
# calculate button
    btn = tk.Button(window, text="Answer", font=(
        "Courier", 15), bg="white", command=checkAns)
    btn.pack()
# show ans place
    output_label = tk.Label(window, font=("Courier", 15), bg="white")
    output_label.pack()

    displayWords()
    window.mainloop()
