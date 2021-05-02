# done
import tkinter as tk
import sys

currentQuestion = 0
answerSubIndex = 0  # need to reset on every question switching
score = 0
count = 5
answerList = [
    ["the"],
    ["was", "the"],
    ["is"],
]
questionBank = [
    "Johnny waited for the bus",
    "The mum was happy when she found the girl",
    "Donald is nice"
]
currentAskingQuestion = None
currentAnswer = None


def game2():
    def display_sentence():
        global count, currentQuestion, answerSubIndex, questionSpilt, currentQuestion, currentAskingQuestion, currentAnswer, score
        count = 5
        currentQuestion = 0
        answerSubIndex = 0
        score = 0
        questionSpilt = questionBank[currentQuestion].split()
        for x in range(len(questionSpilt)):
            for y in answerList[currentQuestion]:
                if questionSpilt[x] == y:
                    questionSpilt[x] = '_'
        currentAnswer = answerList[currentQuestion][answerSubIndex]
        currentAskingQuestion = " ".join(questionSpilt)
        display_init.configure(text=currentAskingQuestion)

    def check_input():
        global removed_word, underScore, count, score, ans_to_list, remove_word_list, answerSubIndex, currentQuestion, answerList, currentAskingQuestion, currentAnswer, isNextQ
        if count == 0:
            output_label.configure(text="Game Over")
            btn["state"] = "disabled"

        word = text_entry.get()
        text_entry.delete(0, 'end')
        isNextQ = False
        if word != currentAnswer:
            if count > 1:
                output_label.configure(text="Please try it again")
                count -= 1
        elif word.isalpha() != True:
            if count > 1:
                output_label.configure(text="Please enter a letter")
        else:  # correct
            qspilt = currentAskingQuestion.split()
            for i in range(len(qspilt)):
                if qspilt[i] == '_':
                    qspilt[i] = word
                    score = int(score) + 1
                    score_label.configure(text="Score: " + str(score))
                    answerSubIndex += 1
                    if answerSubIndex >= len(answerList[currentQuestion]):
                        answerSubIndex = 0
                        currentQuestion += 1
                        isNextQ = True
                    break
            try:
                currentAnswer = answerList[currentQuestion][answerSubIndex]
            except:  # handle end game
                btn["state"] = "disabled"
                return
            if isNextQ:
                questionSpilt = questionBank[currentQuestion].split()
                for x in range(len(questionSpilt)):
                    for y in answerList[currentQuestion]:
                        if questionSpilt[x] == y:
                            questionSpilt[x] = '_'
                currentAskingQuestion = " ".join(questionSpilt)
            else:
                currentAskingQuestion = " ".join(qspilt)
            display_init.configure(text=currentAskingQuestion)
            output_label.configure(text="Congratulations!")
            window.mainloop()

    window = tk.Tk()
    window.title("Fill in the blank")
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

# Label
    input_label = tk.Label(text_frame, text="Please enter a word to fill into blank", font=(
        "Courier", 15), bg="white")  # Enter text label
    input_label.pack()
# Label
    text_label = tk.Label(text_frame, text="Input: ",
                          font=("Courier", 15), bg="white")
    text_label.pack()
# Text box
    text_entry = tk.Entry(text_frame)
    text_entry.pack()
    var_text = text_entry.get()

# calculate button
    btn = tk.Button(window, text="Click", command=check_input)
    btn.pack()
# show ans place
    output_label = tk.Label(window, font=("Courier", 15), bg="white")
    output_label.pack()

# main
    display_sentence()
    window.mainloop()
