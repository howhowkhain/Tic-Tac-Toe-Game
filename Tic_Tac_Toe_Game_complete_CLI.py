import random
import time

# We will represent the board by a dictionary. The keys are the locations and initially their values will be empty spaces which later after every move will be updated as per PC/Player choice.
board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}
# Define working variables: "X" -  will be the symbol used by pc
# win - will be used to count the number of wins (meaning 1 win only possible)
# count - will be used to count the number of moves for each player
count = 0
sign = "X"
win = 0


def display_board(board):
    # We have to print out the updated board after each player's move.
    # For this we will create a function so we can easily print out the board everytime by calling the function.
    # The function accepts one parameter containing the board's current status and prints it out to the console.
    print("+-------" * 3, "+", sep="")
    print("|       |       |       |\n", f"|   {board['7']}   |   {board['8']}   |   {board['9']}   |\n",
          "|       |       |       |\n", sep="", end="")
    print("+-------" * 3, "+", sep="")
    print("|       |       |       |\n", f"|   {board['4']}   |   {board['5']}   |   {board['6']}   |\n",
          "|       |       |       |\n", sep="", end="")
    print("+-------" * 3, "+", sep="")
    print("|       |       |       |\n", f"|   {board['1']}   |   {board['2']}   |   {board['3']}   |\n",
          "|       |       |       |\n", sep="", end="")
    print("+-------" * 3, "+", sep="")


def draw_move(board):
    # The function accepts the board current status
    # and shows the computer's move and updates the board.
    global count
    global sign
    if count in range(0, 9):
        computer_input = random.randrange(1, 10)
        while board[f"{computer_input}"] != " ":
            computer_input = random.randrange(1, 10)
        board[f"{computer_input}"] = sign
        count += 1


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    global count
    global sign
    while count != 9:
        user_input = int(input("Input a number from 1 - 9: "))
        if user_input not in range(1, 10):
            print("Invalid number. Try again, please!")
        elif board[f"{user_input}"] == " ":
            board[f"{user_input}"] = sign
            count += 1
            break
        else:
            print("That place is already filled. Try again, please!")
            continue


def victory_for(board, sign):
    # The function analyzes the board status in order to check if the player using 'O's or 'X's has won the game.
    global win
    if count >= 5:
        if board[f"{1}"] == board[f"{2}"] == board[f"{3}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{4}"] == board[f"{5}"] == board[f"{6}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{7}"] == board[f"{8}"] == board[f"{9}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{1}"] == board[f"{4}"] == board[f"{7}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{2}"] == board[f"{5}"] == board[f"{8}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{3}"] == board[f"{6}"] == board[f"{9}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{1}"] == board[f"{5}"] == board[f"{9}"] != " ":
            print("Game over. ")
            win += 1
        elif board[f"{3}"] == board[f"{5}"] == board[f"{7}"] != " ":
            print("Game over. ")
            win += 1


def game():
    # Now we'll write the main function which has all the gameplay functionality
    global count
    global sign
    global win
    print("\nWelcome to Tic Tac Toe Game by AlexLTD\n")
    name = input("Input your name: ").upper()
    print(f"\nHello {name} ! Let's play Tic-Tac-Toe Game!\n")
    display_board(board)
    time.sleep(1)
    game_play = input("Choose: playing with PC (1) or with player (2): ")
    if game_play == "1":
        print("Game is about to start! Good Luck!\n")
        time.sleep(1)
        print(f"Let's play. PC is using 'X' and {name} 'O':")
        for i in range(9):
            if count in range(0, 9):
                draw_move(board)
                print("PC turn")
                display_board(board)
                victory_for(board, sign)
                if win == 1:
                    print("PC won!")
                    break
                if sign == "X":
                    sign = "O"
                enter_move(board)
                display_board(board)
                victory_for(board, sign)
                if win == 1:
                    print(f"{name} won!")
                    break
                if sign == "O":
                    sign = "X"
            else:
                print("Game over! It's a Tie")
                break
    elif game_play == "2":
        other_player = input("Input other player name: ").upper()
        print(
            f"Good luck both of you! {name} is using 'X' and {other_player} 'O' ")
        print("Game is about to start! Best Luck!\n")
        time.sleep(1)
        print("Let's play:")
        for i in range(9):
            if count in range(0, 9):
                print(f"{name} turn")
                enter_move(board)
                display_board(board)
                victory_for(board, sign)
                if win == 1:
                    print(f"{name} won!")
                    break
                if sign == "X":
                    sign = "O"
                print(f"{other_player} turn")
                enter_move(board)
                display_board(board)
                victory_for(board, sign)
                if win == 1:
                    print(f"{other_player} won!")
                    break
                if sign == "O":
                    sign = "X"
            else:
                print("Game over! It's a Tie.")
                break
    restart = input("Would you like to play again? (y/n) ").lower()
    while restart != "y" and restart != "n":
        print("Invalid input. Try again!")
        restart = input("Choose y=yes or n=no ").lower()
    if restart == "y":
        for key in board:
            board[f"{key}"] = " "
            count = 0
            win = 0
            sign = "X"
        game()
    elif restart == "n":
        quit()


# Start the game by calling the main function game().
game()
