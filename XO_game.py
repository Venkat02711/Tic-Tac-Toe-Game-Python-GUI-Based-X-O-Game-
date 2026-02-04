import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [""] * 9
buttons = []

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def on_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(text=current_player)

    if check_winner(current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
        return

    if "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
        return

    current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, board
    current_player = "X"
    board = [""] * 9
    for btn in buttons:
        btn.config(text="")

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
