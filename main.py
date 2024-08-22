import tkinter as tk
import random
import math
from tkinter import messagebox
from tkinter import Message

root = tk.Tk()
root.geometry("600x600")
root.title("Hangman game")

root.resizable(False, False)

# Welcome label
welcomeL = tk.Label(root, text="Welcome to hangman", font=("Arial", 25))
welcomeL.pack()

clearL = False
restartClicked = False
mistakeCounter = 0


def destroy1(warn1):
    warn1.destroy()


def destroy2(warn2):
    warn2.destroy()


def submit():
    global mistakes
    global mistakeCounter
    global clearL

    global getEntry1
    global getEntry2

    global getEntry4
    getEntry1 = entry1.get()
    getEntry2 = entry2.get()

    getEntry4 = entry4.get()
    if not restartClicked:
        if getEntry1 and getEntry2 and getEntry4:
            if getEntry1.isalpha() and getEntry2.isalpha() and getEntry4.isalpha():
                if getEntry1 == randomW1[0] and getEntry2 == randomW1[1] and getEntry4 == randomW1[3]:
                    messagebox.showinfo("Prompt", "Correct word!")
                    update_wins()
                else:
                    messagebox.showinfo("Prompt", "Incorrect word!")
                    update_mistakes()
                    entryvar1.set("")
                    entryvar2.set("")
                    entryvar4.set("")
                    entry1.config(state="normal")
                    entry2.config(state="normal")
                    entry4.config(state="normal")
            else:
                messagebox.showinfo("Warning", "Enter letters only.")
        else:
            messagebox.showinfo("Warning", "Enter letters, don't leave blanks empty.")
    else:
        if getEntry1 and getEntry2 and getEntry4:
            if getEntry1.isalpha() and getEntry2.isalpha() and getEntry4.isalpha():
                if getEntry1 == randomW2[0] and getEntry2 == randomW2[1] and getEntry4 == randomW2[3]:
                    messagebox.showinfo("Prompt", "Correct word!")
                    update_wins()
                else:
                    messagebox.showinfo("Prompt", "Incorrect word!")
                    update_mistakes()
                    entryvar1.set("")
                    entryvar2.set("")
                    entryvar4.set("")
                    entry1.config(state="normal")
                    entry2.config(state="normal")
                    entry4.config(state="normal")
            else:
                messagebox.showinfo("Warning", "Enter letters only.")
        else:
            messagebox.showinfo("Warning", "Enter letters, don't leave blanks empty.")


def on_entry_changed1(*args):
    global value1
    value1 = entryvar1.get()
    if len(value1) == 1:
        entry1.config(state="disabled")


def on_entry_changed2(*args):
    global value2
    value2 = entryvar2.get()
    if len(value2) == 1:
        entry2.config(state="disabled")


def on_entry_changed4(*args):
    global value4
    value4 = entryvar4.get()
    if len(value4) == 1:
        entry4.config(state="disabled")


def ruleFun():
    messageBox = messagebox.showinfo("Rules",
                                     "-Don't leave the blanks empty. \n-Don't enter any character other than letters. \n-One letter per blank. \n-Don't forget to click submit. \n-First letter MUST be capital. \n-You are allowed to make 5 mistakes only or you lose. \n-Restart changes the word but keeps the values.")


def update_mistakes():
    global mistakeCounter
    mistakeCounter += 1
    mistakes.config(text=f"Mistakes: {mistakeCounter}")
    if mistakeCounter == 6:
        lost = messagebox.showinfo("Lost", "You lost the game :(")
        update_loses()
        mistakeCounter = 0
        mistakes.config(text=f"Mistakes: {mistakeCounter}")

def update_loses():
    global loseCounter
    loseCounter += 1
    loses.config(text=f"Loses: {loseCounter}")

def update_wins():
    global winCounter
    winCounter += 1
    wins.config(text=f"Wins: {winCounter}")


def restart():
    global restartClicked
    global randomW2
    entryvar1.set("")
    entryvar2.set("")

    entryvar4.set("")
    entry1.config(state="normal")
    entry2.config(state="normal")

    entry4.config(state="normal")

    restartClicked = True
    randomW2 = random.choice(word_list)
    print(randomW2)
    notEntry3.config(text=randomW2[2])


# Play function
def play():
    root.destroy()
    newRoot = tk.Tk()
    newRoot.title("Hangman game")
    newRoot.geometry("600x600")
    newRoot.resizable(False, False)
    global mistakes
    global mistakeCounter

    global word_list
    word_list = ["Baby", "Ball", "Bell", "Bird", "Came", "Cold", "Cool", "Dark", "Face", "Fire", "Four", "Gold", "Hair",
                 "Hide", "Into", "Keep", "Lace", "List", "Mars", "Move", "Nine", "Open", "Race", "Sale", "Tide", "Back",
                 "Bank", "Bend", "Busy", "Card", "Come", "Crow", "Evil", "Fair", "Fish", "Game", "Gone", "Hear", "Hope",
                 "Iron", "Kick", "Life", "Love", "Meet", "Near", "Nose", "Pull", "Rice", "Sell", "Tree", "Bake", "Base",
                 "Best", "Calm", "Cash", "Cook"]
    global randomW1
    randomW1 = random.choice(word_list)
    print(randomW1)


    # Blank spaces
    global blank1, blank2, blank3, blank4
    blank1 = tk.Label(newRoot, text="_", font=("Arial", 30))
    blank1.place(relx=0.3, rely=0.15)

    blank2 = tk.Label(newRoot, text="_", font=("Arial", 30))
    blank2.place(relx=0.4, rely=0.15)

    blank3 = tk.Label(newRoot, text="_", font=("Arial", 30))
    blank3.place(relx=0.5, rely=0.15)

    blank4 = tk.Label(newRoot, text="_", font=("Arial", 30))
    blank4.place(relx=0.6, rely=0.15)

    # Entries
    global entry1
    global entry2
    global notEntry3
    global entry4

    # Entry vars
    global entryvar1
    global entryvar2

    global entryvar4

    entryvar1 = tk.StringVar()
    entryvar2 = tk.StringVar()

    entryvar4 = tk.StringVar()

    entry1 = tk.Entry(newRoot, font=("Arial", 15), width=2, textvariable=entryvar1)
    entry1.place(relx=0.3, rely=0.14)

    entry2 = tk.Entry(newRoot, font=("Arial", 15), width=2, textvariable=entryvar2)
    entry2.place(relx=0.4, rely=0.14)

    notEntry3 = tk.Label(newRoot, text=randomW1[2], font=("Arial", 15), width=2)
    notEntry3.place(relx=0.5, rely=0.14)

    entry4 = tk.Entry(newRoot, font=("Arial", 15), width=2, textvariable=entryvar4)
    entry4.place(relx=0.6, rely=0.14)

    # Tracing entries
    entryvar1.trace('w', on_entry_changed1)
    entryvar2.trace('w', on_entry_changed2)

    entryvar4.trace('w', on_entry_changed4)

    # Submit button
    global submitB
    submitB = tk.Button(newRoot, text="Submit", font=("Arial", 15), command=submit)
    submitB.place(relx=0.4, rely=0.3)

    # Rules button
    rules2 = tk.Button(newRoot, text="Rules", font=("Arial", 15), command=ruleFun)
    rules2.place(relx=0.397, rely=0.46)

    # Restart button
    global restart
    restart = tk.Button(newRoot, text="Restart", font=("Arial", 14), command=restart)
    restart.place(relx=0.4, rely=0.38)

    # Mistakes label

    mistakeCounter = 0
    mistakes = tk.Label(newRoot, text=f"Mistakes: {mistakeCounter}", font=("Arial", 15))
    mistakes.place(relx=0.8)

    # Wins label
    global wins, winCounter
    winCounter = 0
    wins = tk.Label(newRoot, text=f"Wins: {winCounter}", font=("Arial", 15))
    wins.place(relx=0.8, rely=0.06)

    # Loses label
    global loses, loseCounter
    loseCounter = 0
    loses = tk.Label(newRoot, text=f"Loses: {loseCounter}", font=("Arial", 15))
    loses.place(relx=0.8, rely=0.12)


# Play button
playB = tk.Button(root, text="Play", font=("Arial", 20), command=play)
playB.place(rely=0.3, relx=0.44)

# Rules button
rules = tk.Button(root, text="Rules", font=("Arial", 17), command=ruleFun)
rules.place(relx=0.44, rely=0.4)

root.mainloop()