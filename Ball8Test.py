from tkinter import *
import tkinter.messagebox as box
from random import randint as rnd

window = Tk()

window.title('8 Ball Game')

frame = Frame(window)
frame_2 = Frame(window)
bottomframe = Frame(window)

entry = Entry(frame)
entry_2 = Entry(frame_2)


def dialog():
    box.showinfo('Greetings', 'Welcome ' + entry.get())

btn = Button(frame, text = 'Enter your name', command = dialog)

btn.pack(side = RIGHT, padx = 5)
entry.pack(side = LEFT)
frame.pack(padx = 20, pady = 20)




def question():
    box.showinfo('Lets Play', 'Your question is: ' + entry_2.get())
    
botn = Button(frame_2, text = 'Enter your question', command = question)

botn.pack(side = RIGHT, padx = 5)
entry_2.pack(side = LEFT)
frame_2.pack(padx = 20, pady = 20)




def game():

    answer = ''

    random_number = rnd(1, 9)

    if random_number == 1:
        answer = '\n\tYes - definitely.'
    elif random_number == 2:
        answer = '\n\tIt is decidedly so.'
    elif random_number == 3:
        answer = '\n\tWithout a doubt.'
    elif random_number == 4:
        answer = '\n\tReply hazy, try again.'
    elif random_number == 5:
        answer = '\n\tAsk again later.'
    elif random_number == 6:
        answer = '\n\tBetter not tell you now.'
    elif random_number == 7:
        answer = '\n\tMy sources say no.'
    elif random_number == 8:
        answer = '\n\tOutlook not so good.'
    elif random_number == 9:
        answer = '\n\tVery doubtful.'
    else:
        answer = '\n\tError'

    box.showinfo('8 Ball Says','Welcome ' + entry.get() + '\n\nYour question was: ' + entry_2.get() + '\n\nMagic 8-Ball\'s answer is: ' + answer)
    
boton = Button(bottomframe, text = 'Play!', command = game)

boton.pack(side = BOTTOM)

bottomframe.pack(padx = 20, pady = 20)

window.mainloop()