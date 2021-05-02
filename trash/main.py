import tkinter as tk
from trash.Word_Gussing_Game_gui import game1
from trash.Fill_in_the_blank_gui import game2
from trash.Reorganized_Word_Game_gui import game3
name_list = []


def page1():
    game1()


def page2():
    game2()


def page3():
    game3()


def click():
    global name_list
    name = text_entry.get()
    if name not in name_list:
        name_list.append(name)
    name_label.configure(text="Name: " + name)


window = tk.Tk()
window.title("Learning English Game")
window.geometry("900x700")
window.configure(background="white")
header = tk.Label(window, text="Welcome", font=("Courier", 50), bg="white")
header.pack()
name_label = tk.Label(window, font=("Courier", 20), bg="white")
name_label.place(relx=1.0, rely=0.0, anchor="ne")
# user enter his name
entry_frame = tk.Frame(window, background="white")
entry_frame.pack(side=tk.TOP)
entry_label = tk.Label(entry_frame, text="Enter your name: ", bg="white")
entry_label.pack(side=tk.LEFT, padx=10, pady=10)
text_entry = tk.Entry(entry_frame)
text_entry.pack(side=tk.LEFT, padx=10, pady=10)
entry_btn = tk.Button(entry_frame, text="Enter",
                      height=1, width=10, command=click)
entry_btn.pack()
# game button
btn_frame = tk.Frame(window, background="white")
btn_frame.pack(side=tk.TOP)
btn_1 = tk.Button(btn_frame, text="Word Gussing",
                  height=2, width=20, command=page1)
btn_1.pack(side=tk.LEFT, padx=20, pady=10)
btn_2 = tk.Button(btn_frame, text="Fill in the blank",
                  height=2, width=20, command=page2)
btn_2.pack(side=tk.LEFT, padx=20, pady=10)
btn_3 = tk.Button(btn_frame, text="Reorganized Word",
                  height=2, width=20, command=page3)
btn_3.pack(side=tk.LEFT, padx=20, pady=10)

window.mainloop()
