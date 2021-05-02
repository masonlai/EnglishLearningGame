# Word gussing game
# done
import random as rd
import tkinter as tk
import sys
import time
# properties

wordsList = ["cream", "water", "yogurt", "milk"]
count = 5
score = 0
repl_word = "_"
index_list = []
ansWord = guessedWord = repl_word_Count = userEnterWords = None
msg1 = "You should guess a word one by one"
msg2 = "Please enter a letter!"
msg3 = "Congratulations!"
msg4 = "Game over"

# start game content


def game1():
    def start_game():
        global wordsList, ansWord, guessedWord, count
        result = (
            "Welcome to our word guessing game!\nYou will have 5 times to guess a word")
        count = 5
        start_text.configure(text=result)
        ansWord = rd.choice(wordsList)
        guessedWord = list(ansWord)

# replace few word to "_" randomly

    def word_to_underscore():
        global guessedWord, repl_word_Count
        for _ in range(len(guessedWord)-2):
          # generate the random int within the range
            random_index = rd.randint(0, len(guessedWord)-1)
            if random_index not in index_list:
                index_list.append(random_index)  # assign to list
            repl_word_Count = index_list.count(
                repl_word)  # count the No. of  "_"
        for i in index_list:  # get the random int to be index
            guessedWord[i] = repl_word
        # display = str(" ".join(guessedWord))  # list become string
        display_init.configure(text=(" ".join(guessedWord)))

##################

    def main_game_else_part():
        global userEnterWords, ansWord, guessedWord, score
        if userEnterWords in ansWord:
            for n in range(len(ansWord)):
                if ansWord[n] == userEnterWords and userEnterWords not in guessedWord:
                    guessedWord[n] = userEnterWords
                    score = int(score) + 1
                    score_label.configure(text="Score: " + str(score))
                    result = " ".join(guessedWord)
                    output_label.configure(text=result)


# after display a word with missing few letter

    def main_game():
        global userEnterWords, count, score, msg1, msg2, msg3, msg4
        userEnterWords = text_entry.get()
        count = int(count) - 1
        # when times = 0:
        if count == 0:
            interact_label.configure(text=msg4)
            btn["state"] = "disabled"
        times = count
        display_times.configure(text=str(times))  # diplay time
        if len(userEnterWords) > 1:
            interact_label.configure(text=msg1)
        if len(userEnterWords) == 0 or userEnterWords.isalpha() != True:
            interact_label.configure(text=msg2)
        result = " ".join(guessedWord)
        if (result == ansWord):
            interact_label.configure(text=msg3)
            btn["state"] = "disabled"
            return game1()
        else:
            main_game_else_part()  # change to def function due to complexity


############
    window = tk.Tk()
    window.title("Word Gussing Game")
    window.geometry("800x600")
    window.configure(background="white")
    header = tk.Label(window, text="Welcome", font=("Courier", 15), bg="white")
    header.pack()
    score_label = tk.Label(window, font=("Courier", 20), bg="white")
    score_label.place(relx=1.0, rely=0.0, anchor="ne")
##############
    text_frame = tk.Frame(window, background="white")
    text_frame.pack()
    # start game
    start_text = tk.Label(text_frame, font=("Courier", 15), bg="white")
    start_text.pack()
    display_times = tk.Label(text_frame, text="Times: 5",
                             font=("Courier", 15), bg="white")
    display_times.pack(pady=20)
# display word initial
    display_init = tk.Label(text_frame, font=("Courier", 15), bg="white")
    display_init.pack()
# asking input label
    input_label = tk.Label(text_frame, text="Please guess a word for the \"_\" element", font=(
        "Courier", 15), bg="white")  # Enter text label
    input_label.pack()
# asking input label
    text_label = tk.Label(text_frame, text="Input: ",
                          font=("Courier", 15), bg="white")
    text_label.pack()
# user input some word
    text_entry = tk.Entry(text_frame)
    text_entry.pack()

# calculate button
    btn = tk.Button(window, text="Answer",  command=main_game)
    btn.pack()
# show ans place
    output_label = tk.Label(window, font=("Courier", 15), bg="white")
    output_label.pack()

    interact_label = tk.Label(window, font=("Courier", 15), bg="white")
    interact_label.pack()

    start_game() 
    word_to_underscore()
    window.mainloop
