# Typing Speed Chacker

import time

sen = "Python is an easiest language, developed by Guido Van Rossom in 1991."

print(sen)

start = time.time()

test = input("Type the Sentence here: \n")

end = time.time()

time_taken = end - start 

print(time_taken)

word = len(test.split())

wpm = (word / time_taken) * 60

print('Your typing speed in WPM : ', wpm)

if test == sen:
    print("Correct")
else:
    print("Oops! Better Luck Next Time..")
