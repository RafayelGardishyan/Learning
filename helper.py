import random
import time

def learn(listfile):
    global answer
    global word
    global already
    already = []


    with open(listfile + '.txt', 'r') as document:
        answer = []
        word = []
        for line in document:
            line = line.split()
            if not line:  # empty line?
                continue
            word += [line[0]]
            answer += [line[1]]


def go(status, _quest, textget,  _input):
    question = random.randint(0, len(word))
    if question in already:
        if len(word) == len(already):
            status.config(fg="blue", text="You are ready")
        else:
            go()
    else:
        _quest.config(text="The word is: " + word[question - 1])
        textget.config(text="Your answer is: ")
        inp = _input.get()
        if inp == answer[question - 1]:
            already.append(question)
            status.config(fg="green", text="Good going!")
        else:
            status.config(fg="red", text="No it is wrong. The good answer was " + answer[question - 1])
        time.sleep(2)
        go()
