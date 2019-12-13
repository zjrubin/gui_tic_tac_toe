from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to The Gaming world TIC-Tac-Toe ")
window.geometry("400x300")

lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

turn = True


# For first person turn.
def clicked(id: int):
    global turn
    button = buttons[id]
    if not buttons[id]["text"]:  # For getting the text of a button
        if turn:
            button["text"] = "X"
        else:
            button["text"] = "O"
        turn = not turn
        check()


flag = 1


def check():
    global flag
    flag += 1

    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                            (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    marks = ('X', 'O')

    for combination in winning_combinations:
        for mark in marks:
            if all((buttons[id]['text'] == mark for id in combination)):
                win(mark)
                exit(0)
    if flag == 10:
        messagebox.showinfo('Tie', 'Try again!')
        window.destroy()
        exit(0)


def win(player):
    ans = "Game complete " + player + " wins "
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


btn1 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(1))
btn1.grid(column=1, row=1)
btn2 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(2))
btn2.grid(column=2, row=1)
btn3 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(3))
btn3.grid(column=3, row=1)
btn4 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(4))
btn4.grid(column=1, row=2)
btn5 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(5))
btn5.grid(column=2, row=2)
btn6 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(6))
btn6.grid(column=3, row=2)
btn7 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(7))
btn7.grid(column=1, row=3)
btn8 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(8))
btn8.grid(column=2, row=3)
btn9 = Button(window,
              bg="yellow",
              fg="Black",
              width=3,
              height=1,
              font=('Helvetica', '20'),
              command=lambda: clicked(9))
btn9.grid(column=3, row=3)

buttons = {
    1: btn1,
    2: btn2,
    3: btn3,
    4: btn4,
    5: btn5,
    6: btn6,
    7: btn7,
    8: btn8,
    9: btn9
}

window.mainloop()
