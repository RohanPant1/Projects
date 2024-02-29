import time
import tkinter as tk 
from tkinter import filedialog, Text
import os 


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

word = input("What would you like to type out:")

print("This is the beginning of the typing test, type the following words out in 3 seconds:")
print (colored(255, 0, 0, word))

for i in [ 3, 2, 1,]:
   print("%s" % i , end='')
   print(" ")
   time.sleep(1)

start = int(time.time())
test = input(str("Type:"))
end = int(time.time())

result = 0

#difference beteen what you typexd and what you were meant to type

#accuracy

accuracy = list(zip(word, test))

for c1, c2 in accuracy:
    if c1 == c2:
        result+=1
    else:
        result+=0

ratio = result / len(word) * 100
print("Accuracy:", str(ratio) + "%")

# Time
total_time = (end - start)
print("It took you", str(total_time), "seconds to type it out!")

# WPM
wpm = 60/total_time * len(word.split())
print("Your wpm is:", wpm)