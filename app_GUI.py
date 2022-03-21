import tkinter as tk
from tkinter import messagebox
import random


# function for toggle the state of the entries: User Name entry and Player 2 Name entry
# if choose PC, entry Player 2 will be disabled
# if choose Player 2, entry Player 2 will be enabled, ready for entering the Player 2 name
def toggle_button_state(switch):
    if switch.get() == 0:
        entry_player_2_name.config(state=tk.DISABLED)
        entry_player_2_name.config(bg="#f7dc92")
        player_2_name_variable.set("")
    elif switch.get() == 1:
        entry_player_2_name.config(state=tk.NORMAL)
        player_2_name_variable.set("Enter Player 2 name")


# function for Player 2 Name entry
# if no user name entered (empty entry), a defalut message "Enter your name" will be displayed
# otherwise the user name entered will be preserved, waiting only for Player 2 name to be
# entered
def edit_entry_player_2(event):
    global player_2_name_variable
    if player_name_variable.get() == "":
        player_name_variable.set("Enter your name")
        player_2_name_variable.set("")
    else:
        player_2_name_variable.set("")


# function for User Name entry
# if PC option selected, User Name will be set to empty and Player 2 entry will be disabled
# and set to emtpy
# if Player 2 selected, User Name will be set to empty and Player 2 entry will be enabled
# and if Player 2 name not set default message "Entry Player 2 name" will be displayed otherwise
# Player 2 name will be retained
def edit_entry_user(event):
    global player_name_variable
    if switch.get() == 0:
        player_2_name_variable.set("")
        player_name_variable.set("")
    else:
        if player_2_name_variable.get() == "":
            player_2_name_variable.set("Enter Player 2 name")
            player_name_variable.set("")
        else:
            player_name_variable.set("")


# function for switching to the game window corresponding to the choosen Player(PC or Player 2)
def next_window(switch, player_name_variable, player_2_name_variable):
    global window, option, player_name_1, player_name_2
    option = switch.get()
    player_name_1 = player_name_variable.get()
    player_name_2 = player_2_name_variable.get()
    # if player choosed is PC
    if option == 0:
        # check if user name is entered otherwise message to enter the user name is displayed
        if player_name_1 == "Enter your name" or player_name_1 == "":
            messagebox.showwarning("Your Name", "Enter your name, please!")
            entry_your_name.focus_set()
            player_name_variable.set("")
        else:
            # create game GUI with PC
            entry_window.destroy()
            window = tk.Tk()
            window.title("TicTacToe")
            window.config(bg="#fcba03")
            # replace tkinter window icon with a specific icon
            icon = tk.PhotoImage(
                file="C:/Users/user/Desktop/Python/Python Projects/Tic Tac Toe Game/images/tic-tac-toe.png")
            window.call("wm", "iconphoto", window._w, icon)
            window.resizable(width=False, height=False)
            # create players display with their respective symbols
            players_label = tk.Label(
                window, text=f"Player 1: PC (X)     Player 2: {player_name_1} (O)", font=("Helvetica", "10", "bold"), bg="#fcba03")
            players_label.grid(row=0, columnspan=3)
            # create game's buttons
            reset()
            # create START button
            b_start = tk.Button(window, text="START", font=(
                "Helvetica", "20", "bold"), bg="#f7dc92", command=pc_move)
            b_start.grid(row=4, columnspan=3)
            # create menu bar
            main_menu = tk.Menu(window)
            window.config(menu=main_menu)
            # create menu bar option object as a cascade
            option_menu = tk.Menu(main_menu, tearoff=False)
            main_menu.add_cascade(
                label="Option", menu=option_menu, underline=0)
            # create option commmands "Reset" & "Back"
            option_menu.add_command(label="Reset", command=reset, underline=0)
            option_menu.add_command(
                label="Back", command=lambda: main(window), underline=0)
            # create main menu comand "Close"
            main_menu.add_command(
                label="Close", command=lambda: close(window), underline=0)
            # bind main window close button to a specific close function which pops-up a message box asking user if continue closing main
            # window or not
            window.protocol("WM_DELETE_WINDOW", lambda: close(window))
            window.mainloop()
    else:
        # check if user name is entered otherwise message to enter the user name is displayed
        if player_name_1 == "Enter your name" or player_name_1 == "":
            messagebox.showwarning("Your Name", "Enter your name, please!")
            entry_your_name.focus_set()
            player_name_variable.set("")
        else:
            # check if Player 2 name is entered otherwise message to enter the Player 2 name
            # is displayed
            player_name_2 = player_2_name_variable.get()
            if player_name_2 == "Enter your name" or player_name_2 == "":
                messagebox.showwarning(
                    "Your Name", "Enter Player 2 name, please!")
                entry_your_name.focus_set()
                player_2_name_variable.set("")
            else:
                # create game GUI with Player 2
                entry_window.destroy()
                window = tk.Tk()
                window.title("TicTacToe")
                window.config(bg="#fcba03")
                # replace tkinter window icon with a specific icon
                icon = tk.PhotoImage(
                    file="C:/Users/user/Desktop/Python/Python Projects/Tic Tac Toe Game/images/tic-tac-toe.png")
                window.call("wm", "iconphoto", window._w, icon)
                window.resizable(width=False, height=False)
                # create players display with their respective symbols
                players_label = tk.Label(
                    window, text=f"Player 1: {player_name_1} (X)     Player 2: {player_name_2} (O)", font=("Helvetica", "10", "bold"), bg="#fcba03")
                players_label.grid(row=0, columnspan=3)
                # create game's buttons
                reset()
                # create menu bar
                main_menu = tk.Menu(window)
                window.config(menu=main_menu)
                # create menu bar option object as a cascade
                option_menu = tk.Menu(main_menu, tearoff=False)
                main_menu.add_cascade(
                    label="Option", menu=option_menu, underline=0)
                # create option commmands "Reset" & "Back"
                option_menu.add_command(
                    label="Reset", command=reset, underline=0)
                option_menu.add_command(
                    label="Back", command=lambda: main(window), underline=0)
                # create main menu comand "Close"
                main_menu.add_command(
                    label="Close", command=lambda: close(window), underline=0)
                # bind main window close button to a specific close function which pops-up a message box asking user if continue closing main
                # window or not
                window.protocol("WM_DELETE_WINDOW", lambda: close(window))
                window.mainloop()


# function simulating PC moves
def pc_move():
    global turn, count
    if count != 9:
        # PC start first move in center position
        if b5["text"] == " " and turn == True:
            b5["text"] = "X"
            b5["foreground"] = "red"
            # once the position is filled, the button will be removed from the next available
            # buttons list.
            buttons_list.remove(b5)
            # check if there is a winner
            check_if_won()
            if not winner:
                turn = False
                count += 1
        # PC choose a random position from the available once and will fill it up
        else:
            random_button = random.choice(buttons_list)
            if random_button["text"] == " " and turn == True:
                random_button["text"] = "X"
                random_button["fg"] = "red"
                # once the position is filled, the button will be removed from the next
                # available buttons list.
                buttons_list.remove(random_button)
                # check if there is a winner
                check_if_won()
                if not winner:
                    turn = False
                    count += 1


# create specific close function asking user if he wants exit the game or not
def close(window):
    window.bell()
    if messagebox.askyesno(title="Exit", message="Do you want to exit\nthis beautifull game?"):
        window.destroy()


# function for creating game's buttons and same used for reseting the buttons for a new game
def reset():
    global count, turn, winner, buttons_list, b1, b2, b3, b4, b5, b6, b7, b8, b9, window
    # variable used to count the valid clicked buttons
    count = 0
    # variable used to identify who's turn is.
    # if True: X turn (pc turn), if False: O tunr(player's turn)
    turn = True
    # variable used to identify if ther is a winner or not
    # True: for a winner and game completed
    # False: there is no winner yet
    winner = False
    # a list with all the clickable buttons used for the game, except START button. Total 9 buttons
    buttons_list = []

    b1 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b1))
    buttons_list.append(b1)
    b2 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b2))
    buttons_list.append(b2)
    b3 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b3))
    buttons_list.append(b3)
    b4 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b4))
    buttons_list.append(b4)
    b5 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b5))
    buttons_list.append(b5)
    b6 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b6))
    buttons_list.append(b6)
    b7 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b7))
    buttons_list.append(b7)
    b8 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b8))
    buttons_list.append(b8)
    b9 = tk.Button(window, text=" ", width=6, height=3, font=("Helvetica", "20"),
                   background="#fcba03", command=lambda: b_click(b9))
    buttons_list.append(b9)
    b1.grid(row=3, column=0)
    b2.grid(row=3, column=1)
    b3.grid(row=3, column=2)
    b4.grid(row=2, column=0)
    b5.grid(row=2, column=1)
    b6.grid(row=2, column=2)
    b7.grid(row=1, column=0)
    b8.grid(row=1, column=1)
    b9.grid(row=1, column=2)


# function for disabling all buttons after game completed
def disable_all_buttons():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)
    b7.config(state=tk.DISABLED)
    b8.config(state=tk.DISABLED)
    b9.config(state=tk.DISABLED)


# function used to check if there is a winner or not
def check_if_won():
    global winner
    # conditions to be satisfied for win, when playing with PC
    if option == 0:
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"
            b1["fg"] = "black"
            b2["fg"] = "black"
            b3["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
            b4["fg"] = "black"
            b5["fg"] = "black"
            b6["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"
            b7["fg"] = "black"
            b8["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"
            b1["fg"] = "black"
            b4["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
            b2["fg"] = "black"
            b5["fg"] = "black"
            b8["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"
            b3["fg"] = "black"
            b6["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"
            b1["fg"] = "black"
            b5["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"
            b3["fg"] = "black"
            b5["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      PC won")
            disable_all_buttons()
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"
            b1["fg"] = "black"
            b2["fg"] = "black"
            b3["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
            b4["fg"] = "black"
            b5["fg"] = "black"
            b6["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"
            b7["fg"] = "black"
            b8["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"
            b1["fg"] = "black"
            b4["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
            b2["fg"] = "black"
            b5["fg"] = "black"
            b8["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"
            b3["fg"] = "black"
            b6["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"
            b1["fg"] = "black"
            b5["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"
            b3["fg"] = "black"
            b5["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
    # condition to be satisfied for win, when playing with Player 2
    elif option == 1:
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"
            b1["fg"] = "black"
            b2["fg"] = "black"
            b3["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
            b4["fg"] = "black"
            b5["fg"] = "black"
            b6["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"
            b7["fg"] = "black"
            b8["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"
            b1["fg"] = "black"
            b4["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
            b2["fg"] = "black"
            b5["fg"] = "black"
            b8["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"
            b3["fg"] = "black"
            b6["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"
            b1["fg"] = "black"
            b5["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"
            b3["fg"] = "black"
            b5["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_1} won")
            disable_all_buttons()
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"
            b1["fg"] = "black"
            b2["fg"] = "black"
            b3["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
            b4["fg"] = "black"
            b5["fg"] = "black"
            b6["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"
            b7["fg"] = "black"
            b8["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"
            b1["fg"] = "black"
            b4["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
            b2["fg"] = "black"
            b5["fg"] = "black"
            b8["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"
            b3["fg"] = "black"
            b6["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"
            b1["fg"] = "black"
            b5["fg"] = "black"
            b9["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"
            b3["fg"] = "black"
            b5["fg"] = "black"
            b7["fg"] = "black"
            winner = True
            messagebox.showinfo(
                title="Win!", message=f"Congratulation!\n      {player_name_2} won")
            disable_all_buttons()
    # condition to be satisfied after all above conditions failed and there is a tie.
    # no one wins.
    if buttons_list == [] and winner == False:
        messagebox.showinfo(
            title="Info", message="Game over!\nIt's a Tie\nNo one wins!")
        disable_all_buttons()


# function used to evaluate user clicks
def b_click(b):
    global count, turn
    # condition used for PC gameplay.
    if option == 0 and count != 0 and buttons_list != []:
        if b["text"] == " " and turn == False:
            b["text"] = "O"
            b["foreground"] = "green"
            # if the clicked button proves valid it will be removed from buttons list
            buttons_list.remove(b)
            # check for a winner
            check_if_won()
            # if no winner switch for the next player (PC) and count the clicked button
            if not winner:
                turn = True
                count += 1
                pc_move()
        # if button was already clicked pops-up the info message that button already clicke and
        # try again
        else:
            messagebox.showinfo(
                title="Info", message="That place is already filled.\nTry again, please!")
    # Player 1 condition used for the Player 2 gameplay.
    elif option == 1:
        # Player 1 (user) conditions for validating the clicked button
        if b["text"] == " " and turn == False:
            b["text"] = "O"
            b["foreground"] = "green"
            # if the clicked button proves valid it will be removed from buttons list
            buttons_list.remove(b)
            # check for a winner
            check_if_won()
            # if no winner switch for the next player (Player 2) and count the clicked button
            if not winner:
                turn = True
                count += 1
        # Player 2 condition used for validating the clicked button
        elif b["text"] == " " and turn == True:
            b["text"] = "X"
            b["foreground"] = "red"
            # if the clicked button proves valid it will be removed from buttons list
            buttons_list.remove(b)
            # check for a winner
            check_if_won()
            # if no winner switch for the next player (Player 2) and count the clicked button
            if not winner:
                turn = False
                count += 1
        # if button was already clicked pops-up the info message that button already clicke and
        # try again
        else:
            messagebox.showinfo(
                title="Info", message="That place is already filled.\nTry again, please!")


# function used to recreate the first GUI window when going back from the game window
def main(window):
    if messagebox.askyesno(title="TicTacToe", message="Are you sure?"):
        global entry_window, player_name_variable, switch, player_2_name_variable, entry_player_2_name, entry_your_name
        window.destroy()
        entry_window = tk.Tk()
        entry_window.title("TicTacToe")
        # replace tkinter winow icon with the specific icon
        icon = tk.PhotoImage(
            file="C:/Users/user/Desktop/Python/Python Projects/Tic Tac Toe Game/images/tic-tac-toe.png")
        entry_window.call("wm", "iconphoto", entry_window._w, icon)
        # window not to be resizable.
        entry_window.resizable(width=False, height=False)
        entry_window.config(bg="#fcba03")
        # label for the welcome message
        label_1 = tk.Label(
            entry_window, text="Welcome to Tic Tac Toe Game", anchor=tk.CENTER, font=("Helvetica", "20"), bg="#fcba03")
        label_1.grid(row=0, columnspan=3)
        # label for the welcome message
        label_2 = tk.Label(
            entry_window, text="by AlexLTD", anchor=tk.CENTER, font=("Helvetica", "10"), bg="#fcba03")
        label_2.grid(row=1, columnspan=3)
        # label for Your Name title
        label_3 = tk.Label(entry_window, text="Your Name:",
                           font=("Helvetica", "15"), bg="#fcba03")
        label_3.grid(row=2, column=1)
        # observable variable used to store User Name
        player_name_variable = tk.StringVar()
        # setting the default message for the User Name
        player_name_variable.set("Enter your name")
        # creating entry for the User Name
        entry_your_name = tk.Entry(
            entry_window, width=30, textvariable=player_name_variable, font=("Helvetica", "10", "italic"), border=3, bg="#f7dc92")
        # bind user entry to a function which sets the behaviour of the user entry
        entry_your_name.bind("<Button-1>", edit_entry_user)
        entry_your_name.grid(row=2, column=2)
        # observable variable used to determine which gameplay is selected: PC or Player 2
        switch = tk.IntVar()
        # frame which enclose the two options: PC(value 0) and Player 2(value 1)
        choose_player = tk.LabelFrame(entry_window, borderwidth=3, text="Choose Player", font=(
            "Helvetica", "15"), labelanchor="n", bg="#fcba03")
        # frame for PC option
        frame_PC = tk.LabelFrame(choose_player, borderwidth=3,
                                 text="PC", font=("Helvetica", "15"), labelanchor="n", bg="#fcba03")
        # radiobutton PC option
        choice_PC = tk.Radiobutton(
            frame_PC, text="Playing with PC", font=("Helvetica", "15"), variable=switch, value=0, command=lambda: toggle_button_state(switch), bg="#fcba03")
        choice_PC.pack()
        # label for a free space(design purpose only)
        choice_PC_free_space = tk.Label(frame_PC, text=" ", bg="#fcba03")
        choice_PC_free_space.pack()
        frame_PC.grid(row=0, column=0)
        # label for a free space(design purpose only)
        label_free_space = tk.Label(choose_player, text=" ", bg="#fcba03")
        label_free_space.grid(row=0, column=1)
        # Player 2 frame which enclose Player 2 option button
        frame_Player_2 = tk.LabelFrame(choose_player, borderwidth=3,
                                       text="Player 2", font=("Helvetica", "15"), labelanchor="n", bg="#fcba03")
        # radiobutton Player 2 option
        choice_Player_2 = tk.Radiobutton(
            frame_Player_2, text="Playing with Player 2", font=("Helvetica", "15"), variable=switch, value=1, command=lambda: toggle_button_state(switch), bg="#fcba03")
        choice_Player_2.pack()
        # observable variable used to store Player 2 name
        player_2_name_variable = tk.StringVar()
        # create Player 2 entry for input Player 2 Name
        entry_player_2_name = tk.Entry(
            frame_Player_2, width=30, textvariable=player_2_name_variable, font=("Helvetica", "10", "italic"), state=tk.DISABLED, border=3, bg="#f7dc92", disabledbackground="#fcba03")
        # bind Player 2 entry to a function which sets the behaviour of the Player 2 entry
        entry_player_2_name.bind("<Button-1>", edit_entry_player_2)
        entry_player_2_name.pack()
        frame_Player_2.grid(row=0, column=2)
        choose_player.grid(row=3, columnspan=3, padx=10, pady=10)
        # label for a free space(design purpose only)
        label_free_space_row = tk.Label(entry_window, text=" ", bg="#fcba03")
        label_free_space_row.grid(row=4, columnspan=3)
        # create Next button for switching to the gameplay choosen as per option selected (PC or Player 2)
        next_button = tk.Button(entry_window, text="Next", font=(
            "Helvetica", "10", "bold"), width=10, background="#fcba03", foreground="black", command=lambda: next_window(switch, player_name_variable, player_2_name_variable))
        next_button.grid(row=5, columnspan=4)
        # create main menu bar
        main_menu = tk.Menu(entry_window)
        entry_window.config(menu=main_menu)
        # add Close command to the main menu bar
        main_menu.add_command(
            label="Close", command=lambda: close(entry_window))
        entry_window.protocol("WM_DELETE_WINDOW",
                              lambda: close(entry_window))
        entry_window.mainloop()


entry_window = tk.Tk()
entry_window.title("TicTacToe")
# replace tkinter winow icon with the specific icon
icon = tk.PhotoImage(
    file="C:/Users/user/Desktop/Python/Python Projects/Tic Tac Toe Game/images/tic-tac-toe.png")
entry_window.call("wm", "iconphoto", entry_window._w, icon)
# window not to be resizable.
entry_window.resizable(width=False, height=False)
entry_window.config(bg="#fcba03")
# label for the welcome message
label_1 = tk.Label(
    entry_window, text="Welcome to Tic Tac Toe Game", anchor=tk.CENTER, font=("Helvetica", "20"), bg="#fcba03")
label_1.grid(row=0, columnspan=3)
# label for the welcome message
label_2 = tk.Label(
    entry_window, text="by AlexLTD", anchor=tk.CENTER, font=("Helvetica", "10"), bg="#fcba03")
label_2.grid(row=1, columnspan=3)
switch = tk.IntVar()
# label for Your Name title
label_3 = tk.Label(entry_window, text="Your Name:",
                   font=("Helvetica", "15"), bg="#fcba03")
label_3.grid(row=2, column=1)
# observable variable used to store User Name
player_name_variable = tk.StringVar()
# setting the default message for the User Name
player_name_variable.set("Enter your name")
# creating entry for the User Name
entry_your_name = tk.Entry(
    entry_window, width=30, textvariable=player_name_variable, font=("Helvetica", "10", "italic"), border=3, bg="#f7dc92")
# bind user entry to a function which sets the behaviour of the user entry
entry_your_name.bind("<Button-1>", edit_entry_user)
entry_your_name.grid(row=2, column=2)
# observable variable used to determine which gameplay is selected: PC or Player 2
switch = tk.IntVar()
# frame which enclose the two options: PC(value 0) and Player 2(value 1)
choose_player = tk.LabelFrame(entry_window, borderwidth=3, text="Choose Player", font=(
    "Helvetica", "15"), labelanchor="n", bg="#fcba03")
# frame for PC option
frame_PC = tk.LabelFrame(choose_player, borderwidth=3,
                         text="PC", font=("Helvetica", "15"), labelanchor="n", bg="#fcba03")
# radiobutton PC option
choice_PC = tk.Radiobutton(
    frame_PC, text="Playing with PC", font=("Helvetica", "15"), variable=switch, value=0, command=lambda: toggle_button_state(switch), bg="#fcba03")
choice_PC.pack()
# label for a free space(design purpose only)
choice_PC_free_space = tk.Label(frame_PC, text=" ", bg="#fcba03")
choice_PC_free_space.pack()
frame_PC.grid(row=0, column=0)
# label for a free space(design purpose only)
label_free_space = tk.Label(choose_player, text=" ", bg="#fcba03")
label_free_space.grid(row=0, column=1)
# Player 2 frame which enclose Player 2 option button
frame_Player_2 = tk.LabelFrame(choose_player, borderwidth=3,
                               text="Player 2", font=("Helvetica", "15"), labelanchor="n", bg="#fcba03")
# radiobutton Player 2 option
choice_Player_2 = tk.Radiobutton(
    frame_Player_2, text="Playing with Player 2", font=("Helvetica", "15"), variable=switch, value=1, command=lambda: toggle_button_state(switch), bg="#fcba03")
choice_Player_2.pack()
# observable variable used to store Player 2 name
player_2_name_variable = tk.StringVar()
# create Player 2 entry for input Player 2 Name
entry_player_2_name = tk.Entry(
    frame_Player_2, width=30, textvariable=player_2_name_variable, font=("Helvetica", "10", "italic"), state=tk.DISABLED, border=3, bg="#f7dc92", disabledbackground="#fcba03")
# bind Player 2 entry to a function which sets the behaviour of the Player 2 entry
entry_player_2_name.bind("<Button-1>", edit_entry_player_2)
entry_player_2_name.pack()
frame_Player_2.grid(row=0, column=2)
choose_player.grid(row=3, columnspan=3, padx=10, pady=10)
# label for a free space(design purpose only)
label_free_space_row = tk.Label(entry_window, text=" ", bg="#fcba03")
label_free_space_row.grid(row=4, columnspan=3)
# create Next button for switching to the gameplay choosen as per option selected (PC or Player 2)
next_button = tk.Button(entry_window, text="Next", font=(
    "Helvetica", "10", "bold"), width=10, background="#fcba03", foreground="black", command=lambda: next_window(switch, player_name_variable, player_2_name_variable))
next_button.grid(row=5, columnspan=4)
# create main menu bar
main_menu = tk.Menu(entry_window)
entry_window.config(menu=main_menu)
# add Close command to the main menu bar
main_menu.add_command(
    label="Close", command=lambda: close(entry_window), underline=0)
entry_window.protocol("WM_DELETE_WINDOW",
                      lambda: close(entry_window))
entry_window.mainloop()
