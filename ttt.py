import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.geometry('300x300')


board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def x1():
    if board[0] == 0:
        btn_text1.set('x')
        board[0] = 1
        rand()
        win()
def x2():
    if board[1] == 0:
        btn_text2.set('x')
        board[1] = 1
        rand()
        win()
def x3():
    if board[2] == 0:
        btn_text3.set('x')
        board[2] = 1
        rand()
        win()
def x4():
    if board[3] == 0:
        btn_text4.set('x')
        board[3] = 1
        rand()
        win()
def x5():
    if board[4] == 0:
        btn_text5.set('x')
        board[4] = 1
        rand()
        win()
def x6():
    if board[5] == 0:
        btn_text6.set('x')
        board[5] = 1
        rand()
        win()
def x7():
    if board[6] == 0:
        btn_text7.set('x')
        board[6] = 1
        rand()
        win()
def x8():
    if board[7] == 0:
        btn_text8.set('x')
        board[7] = 1
        rand()
        win()
def x9():
    if board[8] == 0:
        btn_text9.set('x')
        board[8] = 1
        rand()
        win()

# generate natural stupidity
def rand():
    while True:
        num = random.randint(0,8)
        if board[num] == 0:
            board[num] = 2
            if num == 0:
                btn_text1.set('o')
            elif num == 1:
                btn_text2.set('o')
            elif num == 2:
                btn_text3.set('o')
            elif num == 3:
                btn_text4.set('o')
            elif num == 4:
                btn_text5.set('o')
            elif num == 5:
                btn_text6.set('o')
            elif num == 6:
                btn_text7.set('o')
            elif num == 7:
                btn_text8.set('o')
            elif num == 8:
                btn_text9.set('o')
            break
        
def win():
    # show winner and end game
    def msg(winner):
        popup = tk.Tk()
        popup.wm_title('winner winner')
        if winner == 1:
            txt = 'you won'
        elif winner == 2:
            txt = 'computer won'
        elif winner == 3:
            txt = 'draw'
        label = ttk.Label(popup, text = txt)
        label.pack()
        btn = ttk.Button(popup, text = 'ok', command = lambda:[root.destroy(), popup.destroy()])
        btn.pack()
        
    # check 8 possible win cases with stalemate
    if board[0] != 0 and board[0] == board[1] == board[2]:
        msg(board[0])
    elif board[3] != 0 and board[3] == board[4] == board[5]:
        msg(board[3])
    elif board[6] != 0 and board[6] == board[7] == board[8]:
        msg(board[6])
    elif board[0] != 0 and board[0] == board[3] == board[6]:
        msg(board[0])
    elif board[1] != 0 and board[1] == board[4] == board[7]:
        msg(board[1])
    elif board[2] != 0 and board[2] == board[5] == board[8]:
        msg(board[2])
    elif board[0] != 0 and board[0] == board[4] == board[8]:
        msg(board[0])
    elif board[2] != 0 and board[2] == board[4] == board[6]:
        msg(board[2])
    elif board[0] != 0 and board[1] != 0 and board[2] != 0 and board[3] != 0 and board[4] != 0 and board[5] != 0 and board[6] != 0 and board[7] != 0 and board[8] != 0:
        msg(3)
        


# initialize board
btn_text1 = tk.StringVar()
btn1 = ttk.Button(root, textvariable = btn_text1, command = x1)
btn_text1.set('_')

btn_text2 = tk.StringVar()
btn2 = ttk.Button(root, textvariable = btn_text2, command = x2)
btn_text2.set('_')

btn_text3 = tk.StringVar()
btn3 = ttk.Button(root, textvariable = btn_text3, command = x3)
btn_text3.set('_')

btn_text4 = tk.StringVar()
btn4 = ttk.Button(root, textvariable = btn_text4, command = x4)
btn_text4.set('_')

btn_text5 = tk.StringVar()
btn5 = ttk.Button(root, textvariable = btn_text5, command = x5)
btn_text5.set('_')

btn_text6 = tk.StringVar()
btn6 = ttk.Button(root, textvariable = btn_text6, command = x6)
btn_text6.set('_')

btn_text7 = tk.StringVar()
btn7 = ttk.Button(root, textvariable = btn_text7, command = x7)
btn_text7.set('_')

btn_text8 = tk.StringVar()
btn8 = ttk.Button(root, textvariable = btn_text8, command = x8)
btn_text8.set('_')

btn_text9 = tk.StringVar()
btn9 = ttk.Button(root, textvariable = btn_text9, command = x9)
btn_text9.set('_')

btn1.grid(row = 1, column = 1)
btn2.grid(row = 2, column = 1)
btn3.grid(row = 3, column = 1)
btn4.grid(row = 1, column = 2)
btn5.grid(row = 2, column = 2)
btn6.grid(row = 3, column = 2)
btn7.grid(row = 1, column = 3)
btn8.grid(row = 2, column = 3)
btn9.grid(row = 3, column = 3)

root.mainloop()
