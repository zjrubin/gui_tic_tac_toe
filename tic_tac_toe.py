import tkinter as tk
from tkinter import messagebox


def main() -> None:
    program = Tic_Tac_Toe()
    program.window.mainloop()


class Tic_Tac_Toe:
    def __init__(self) -> None:
        self.next_move = True
        self.turn = 1
        self.window = self.create_window()
        self.buttons = self.create_buttons()

    def create_window(self) -> tk.Tk:
        window = tk.Tk()
        window.title("Welcome to Tic-Tac-Toe!")
        window.geometry("400x250")
        lbl = tk.Label(window, text="Tic-tac-toe Game", font=('Futura', '15'))
        lbl.grid(row=0, column=0)
        lbl = tk.Label(window, text="Player 1: X", font=('Futura', '10'))
        lbl.grid(row=1, column=0)
        lbl = tk.Label(window, text="Player 2: O", font=('Futura', '10'))
        lbl.grid(row=2, column=0)
        return window

    def create_buttons(self) -> dict:
        buttons = dict()
        counter = 1
        for row in range(1, 4):
            for column in range(1, 4):
                buttons[counter] = tk.Button(
                    self.window,
                    bg="yellow",
                    fg="black",
                    width=3,
                    height=1,
                    font=('Futura', '20'),
                    command=lambda id=counter: self.clicked(id))
                buttons[counter].grid(column=column, row=row)
                counter += 1
        return buttons

    def clicked(self, id: int) -> None:
        button = self.buttons[id]
        if not button["text"]:
            if self.next_move:
                button["text"] = "X"
            else:
                button["text"] = "O"
            self.next_move = not self.next_move
            self.check()

    def check(self) -> None:
        winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        marks = ('X', 'O')

        for combination in winning_combinations:
            for mark in marks:
                if all(
                    (self.buttons[id]['text'] == mark for id in combination)):
                    self.win(mark)
                    exit(0)
        if self.turn == 9:
            messagebox.showinfo('Tie', 'Try again!')
            self.window.destroy()
            exit(0)

        self.turn += 1

    def win(self, player: str) -> None:
        ans = "Game complete " + player + " wins "
        messagebox.showinfo("Congratulations", ans)
        self.window.destroy()


if __name__ == '__main__':
    main()
