# Tic-Tac-Toe Milestone Project
# To add: auto-replay, computer player, stats, saves

from os import system
from random import choice

# Variables and Data Structures

# Board
dct = {x:" " for x in range(9)}

# wins is a list of lists holding board locations of win conditions
wins = [[0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 4, 8], 
        [2, 4, 6]]

# remaining is a list of lists holding board locations of win conditions for the computer
remaining = wins.copy()

# player_wins is a list of lists holding board locations of win conditions for the player
player_wins = wins.copy()

# poppedwins is a list of lists holding board locations of win conditions that have been removed from remaining
poppedwins = []

# popped is a list of lists holding board locations of win conditions that have been removed from player_wins
popped = []

# computer turns checking win states of any 2 marked and 1 open spot
cpu_checks = [[0, 1, 2], 
              [0, 2, 1], 
              [1, 2, 0]]

# Function: creates the data structure that contains the computer second-turn moveset
def create_cpumoveset():
    return {0: 8,
            1: 4, 
            2: 6, 
            3: 4, 
            4: choice([0, 2, 6, 8]), 
            5: 4, 
            6: 2,
            7: 4,
            8: 0}


# Function: displays the current board with "X" and "O"
def board(d):
    print("\n")
    print(f"   ||   ||   ")
    print(f" {d[0]} || {d[1]} || {d[2]} ")
    print(f"   ||   ||   ")
    print("=============")
    print(f"   ||   ||   ")
    print(f" {d[3]} || {d[4]} || {d[5]} ")
    print(f"   ||   ||   ")
    print("=============")
    print(f"   ||   ||   ")
    print(f" {d[6]} || {d[7]} || {d[8]} ")
    print(f"   ||   ||   ")
    print("\n")


# Function: takes a spot location and removes all wins associated with that spot from remaining 
# and appends to poppedwins
def remove_win(spot, win_lst, popped):
    temp = win_lst.copy()
    for win in temp:
        if spot in win:
            popped.append(win_lst.pop(win_lst.index(win)))
    return


# Function: Takes player input and changes board with selection
def player_turn():
    while True:
        # Take player input
        raw = input("Please Select a Number 0-8: ")
        # Check for allowable inputs -> continue (reloop) if NOT allowed
        if raw not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]: continue
        # Change player raw input into integer
        else: spot = int(raw)
        # Check for if board selection has already been played -> break if not played yet
        if dct[spot] == " ": break
        # Else reloop to select a new board location
        else: print("Already selected. Choose again: ")
    # Changes board using player token
    dct[spot] = "X"
    # Remove win condition from allowed computer wins
    remove_win(spot, remaining, poppedwins)
    print(f"Player has chosen: {spot}")
    print(f"CPU cannot win with: {poppedwins}")
    print(f"CPU can still win with: {remaining}")
    # Clears console output
    # system('clear')


def cpu_losecheck():
    # Loops through win conditions and attempts to prevent a loss
    for win in wins:
    
        # check for loss combinations
        for check in cpu_checks:

            # immediate losses
            if dct[win[check[0]]] == dct[win[check[1]]] == "X" and dct[win[check[2]]] == " ":
                dct[win[check[2]]] = "O"
                remove_win(win[check[2]], player_wins, popped)
                print(f"Prevent Loss Move: The computer will choose {win[check[2]]}")
                return True
    return False


def cpu_winmove():
    # Loops through remaining win conditions and attempts to win
    for win in remaining:
            
        # check for all win combinations
        for check in cpu_checks:

            # immediate wins
            if dct[win[check[0]]] == dct[win[check[1]]] == "O" and dct[win[check[2]]] == " ":
                dct[win[check[2]]] = "O"
                remove_win(win[check[2]], player_wins, popped)
                print(f"Win Move: The computer will choose {win[check[2]]}")
                return True
    return False


def cpu_move():
    # Loop through remaining to check for win conditions with one "O"
    # From the win condition with one "O" check for overlap of other two spots
    # Overlap means same position in a different win condition
    # If there is overlap, check the different win condition for "X"
    # ?maybe the popped items from remaining should populate a second data structure to check?
    possible = []
    # Loops through remaining win conditions and attempts to start a win
    for win in remaining:
        if dct[win[0]] == "O" or dct[win[1]] == "O" or dct[win[2]] == "O":
            possible.extend([x for x in win if dct[x] != "O"])
    # print(possible)
    for spot in possible:
        for win in player_wins:
            if spot in win:
                print(f"Overlap Player wins: {win}")
            pass
        pass
    print(possible)
        # check for all win combinations
    return


# Function: Creates computer decision
# Arguments: player - takes a string 'X' or 'O'
def cpu_turn(count):

    # # computer turns checking win states of any 2 marked and 1 open spot
    # cpu_checks = [[0, 1, 2], 
    #               [0, 2, 1],
    #               [1, 2, 0]]
    
    # Loops through remaining win conditions and removes unwinable conditions
    # for win in remaining:
    #     for spot in range(9):
    #         pass

    # if check for computer first turn
    if count == 1:
        
        for spot in range(9):
            if dct[spot] == "X":
                cpu_spot = create_cpumoveset()[spot]
                dct[cpu_spot] = "O"
                remove_win(cpu_spot, player_wins, popped)

                print(f"CPU first turn: {cpu_spot}")
                
    # else checks for any other turn count above 1
    else:
        if cpu_losecheck():
            pass
        elif cpu_winmove():
            pass
        else:
            print("Run cpu_move()")
            cpu_move()

    print(f"Player cannot win with: {popped}")
    print(f"Player can still win with: {player_wins}")


        # # Loops through win conditions and attempts to prevent a loss
        # for win in wins:
        
        #     # check for loss combinations
        #     for check in cpu_checks:

        #         # immediate losses
        #         if dct[win[check[0]]] == dct[win[check[1]]] == "X" and dct[win[check[2]]] == " ":
        #             dct[win[check[2]]] = "O"
        #             print(f"Prevent Loss Move: The computer will choose {win[check[2]]}")
        

        # # Loops through remaining win conditions and attempts to win
        # for win in remaining:
                
        #     # check for all win combinations
        #     for check in cpu_checks:

        #         # immediate wins
        #         if dct[win[check[0]]] == dct[win[check[1]]] == "O" and dct[win[check[2]]] == " ":
        #             dct[win[check[2]]] = "O"
        #             print(f"Win Move: The computer will choose {win[check[2]]}")
                    

        # first elif-elif-elif check for immediate wins (2 'O' with 1 open spot)
        # elif dct[win[0]] == dct[win[1]] == player and dct[win[2]] == " ":
        #     dct[win[2]] = player
        #     break
        # elif dct[win[0]] == dct[win[2]] == player and dct[win[1]] == " ":
        #     dct[win[1]] = player
        #     break
        # elif dct[win[1]] == dct[win[2]] == player and dct[win[0]] == " ":
        #     dct[win[0]] = player
        #     break

        # # second elif-elif-elif check for any immediate losses (2 'X' with 1 open spot)
        # elif dct[win[0]] == dct[win[1]] == "X" and dct[win[2]] == " ":
        #     dct[win[2]] = player
        #     break
        # elif dct[win[0]] == dct[win[2]] == "X" and dct[win[1]] == " ":
        #     dct[win[1]] = player
        #     break
        # elif dct[win[1]] == dct[win[2]] == "X" and dct[win[0]] == " ":
        #     dct[win[0]] = player
        #     break

        # third elif-elif-elif check for any 1 with 2 open spots
        # elif dct[win[0]] == player and dct[win[1]] == dct[win[2]] == " ":
        #     dct[win[1]] = player
        #     break
        # elif dct[win[1]] == player and dct[win[2]] == dct[win[0]] == " ":
        #     dct[win[2]] = player
        #     break
        # elif dct[win[2]] == player and dct[win[0]] == dct[win[1]] == " ":
        #     dct[win[0]] = player
        #     break

        # last elif check for any three open
        # elif dct[win[0]] == dct[win[1]] == dct[win[2]] == " ":
        #     pass

        # last else check for random placement due to draw
        # else:
        #     # Selects spots 0-9 in order and places a spot if empty
        #     while True:
        #         attempt = choice(range(9))
        #         if dct[attempt] == " ":
        #             spot = attempt
        #             break
        #     # Changes board using player variable
        #     dct[spot] = player
        #     break

    # Clears console output
    # system('clear')


# Function: checks for win and draw end game states of the board and returns True if game over
# Variable: turn - takes a string "X" or "O"
# Variable: spaces - takes an integer amount of board spots left
def game_check(token, spaces):
    # for loop through each win condition
    for win in wins:
        if dct[win[0]] == dct[win[1]] == dct[win[2]] == token:
            print(f"Game Over! {token} Wins!")
            return True
    # if no spaces left then the game is over and ends in a draw
    if spaces == 0:
            print("Game Over! Draw!")
            return True
    

# Function: to reset game and game board
def reset():
    while True:
        # take player input
        raw = input("Would you like to play again? (Yes or No) ")
        select = raw.lower()[0]
        if select not in ["y", "n"]: continue
        elif select == 'y':
            count = 1
            spaces = 9
            for x in range(9):
                dct[x] = " "
            system('clear')
            break
        else:
            gameOn = False
            break


# Function: tic-tac-toe two-player game 
def tic_tac_toe():
    # boolean controls main game while loop
    gameOn = True
    print("Welcome to Eric's Tic-Tac-Toe Game in Python!")
    # board(dct)
    # count is integer value of rounds
    count = 1
    # spaces is integer value of board locations open to play
    spaces = 9
    # win/lose/draw stats data structure
    # stats = [0, 0 , 0]
    while gameOn:

        board(dct)

        print(f"Round {count}")

        player_turn()

        if game_check("X", spaces):
            reset()

        cpu_turn(count)

        if game_check("O", spaces):
            reset()

        spaces -= 1

        board(dct)

        print(f"Spaces: {spaces}")
        count += 1


tic_tac_toe()
