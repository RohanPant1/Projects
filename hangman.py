import tkinter as tk
import random

with open("hangman.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = (random.choice(words))
word = list(word)
print(word)
correct = []

window = tk.Tk()
string_variable = tk.StringVar()
guess_label = tk.Entry(window, width=10,textvariable=string_variable)
guess_label.grid(row=1, column=10, pady=10)

for i in range(len(word)):
    tk.Label(window, height=2, width=4, borderwidth=1, relief= 'raised', padx= 2).grid(column=i, row=3)

guesses = 7
guesses_label = tk.Label(window, text=guesses, height=2, width=2)
guesses_label.grid(row=5, column=10, pady=10)

def check_word():
    global guesses
    global correct
    guess = guess_label.get()
    
    occurence = [a for a, x in enumerate(word) if x == guess]
    print(occurence)
    if guess in word:
        tk.Label(window, text="It is in the word").grid(row=6, column=10)
        for j in range(len(occurence)):
            tk.Label(window, text=guess, height=2, width=4, borderwidth=1, relief='raised', padx=2,background='green').grid(column=occurence[j], row=3)
            correct.append(guess)
    else:
        tk.Label(window, text="It is not in the word").grid(row=6, column=10)
        guesses=guesses-1
        guesses_label['text']=guesses
    if guesses<1:
        tk.Label(window, text="Game over").grid(row=7, column=10)
        for l in range(len(word)):
            tk.Label(window, text=str(word[l]), height=2, width=4, borderwidth=1, relief='raised', padx=2,background='red').grid(column=l, row=3)
    elif len(correct)==len(word):      
        tk.Label(window, text="You won!").grid(row=7, column=10)
              


        

check = tk.Button(window, text="check",  height=2, width=10,command=check_word).grid(row=4, column=10, pady=10)

window.mainloop()