import random
import time
import tk


already = []

listfile = input("What is the name of the list you want to learn? (without .txt): ")

with open(listfile + '.txt', 'r') as document:
    answer = []
    word = []
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        word += [line[0]]
        answer += [line[1]]

print("Learn words by guessing \n\n")

def go():
    global already
    question = random.randint(0, len(word))
    if question in already:
        if len(word) == len(already):
            print("You are ready")
        else:
            go()
    else:
        print("The word is: " + word[question - 1])
        inp = input("Your answer is: ")
        if inp == answer[question - 1]:
            already.append(question)
            print("\n\nCongratulations")
        else:
            print("\nNo it is wrong. The good answer was " + answer[question - 1])
        time.sleep(2)
        go()

go()
