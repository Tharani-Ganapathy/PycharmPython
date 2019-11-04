import random
import numpy as np


def tic_tac_toe():
    # to count the total turns took by the player
    count = 0
    # to create an 3x3 array
    arr = np.full([3, 3], '_')
    print(arr)
    # players start filling the array alternatively until one wins
    for i in range(9):
        # to count the turns took by each player
        ocount = 0
        xcount = 0

        print("First Player, Place the 'O': ")
        # input to place 'O' in an array
        row = int(input("Enter the row number"))
        col = int(input("Enter the col number"))
        # to check whether the given position is unused
        if arr[row, col] == '_':
            arr[row, col] = 'O'
            count = count+1

            # to check whether the player has placed the 'O' continuously
            if count > 4:
                for j in range(3):
                    if arr[row, j] == 'O':
                        ocount = ocount + 1
                if ocount == 3:
                    print("First Player Wins!!!")
                    print(arr)
                    break
            print(arr)
        else:
            break

        print("Second Player, Place the 'X': ")
        row = random.choice([0, 1, 2])
        print("Generated row number: {}".format(row))
        col = random.choice([0, 1, 2])
        print("Generated col number: {}".format(col))
        # to check whether the given position is unused
        if arr[row, col] == '_':
            arr[row, col] = 'X'
            count = count + 1

            # to check whether the player has placed the 'X' continuously
            if count > 4:
                for j in range(3):
                    if arr[row, j] == 'X':
                        xcount = xcount + 1
                if xcount == 3:
                    print("Second Player Wins!!!")
                    print(arr)
                    break
            print(arr)
        else:
            break


print("Tic Tac Toe!!")
print("Let's start the game!!")
tic_tac_toe()
