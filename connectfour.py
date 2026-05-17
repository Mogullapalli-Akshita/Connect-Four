import random
import numpy as np

strow = 6
stdcol = 7

board = np.zeroes((stdrow, stdcol), dtype = int)



def startby():
    return random.randint(1,2)

def onturn(player, column):
    if any(board[:column-1] == 0):
        rack = list(board[:, column-1])[::-1]
        empty = [r for r in range(len(rack)) if rack[r] == 0]
        board[stdrow-1-empty[0]][column-1] = player
    else:
        onturn(player, column+1)

i = 15

while(i):
    print("player", turn, "enter column number:")
    column = int(input())
    onturn(turn, column)
    print(board)
    turn = 3 - turn
    i = i - 1
