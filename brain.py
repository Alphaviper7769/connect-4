import cv2

RADIUS = 25

def checkWin(blank):
    # Return [Win code, Starting Token, Ending Token]
    # Return/Win code:
    # 1 -> Horizontal, 2 -> Vertical, 3 -> Diagonal
    # Return [0, 0, 0] for no result

    # Check Horizontal
    count = 0
    for i in range(7, -1, -1):
        startingToken = 0
        # prevX -> [noColor: 0, Red: 1, Green: 2]
        prevX = 0
        y = 212 + i*2*RADIUS + i*12 + 25
        for j in range(0, 12):
            x = 90 + j*2*RADIUS + j*RADIUS + 25
            # BGR
            color = 0
            if blank[y, x, 1] == 255 and blank[y, x, 2] == 0:
                # GREEN
                color = 2
            elif blank[y, x, 2] == 255 and blank[y, x, 1] == 0:
                # RED
                color = 1
            if color == prevX and prevX != 0:
                count += 1
            else:
                prevX = color
                count = 1
                startingToken = j
            if count == 4:
                return [1, startingToken, j]

    # Check Vertical
    count = 0
    for i in range(0, 12):
        startingToken = 0
        # prevX -> [noColor: 0, Red: 1, Green: 2]
        prevY = 0
        x = 90 + i*2*RADIUS + i*RADIUS + 25
        for j in range(0, 8):
            y = 212 + j*2*RADIUS + j*12 + 25
            # BGR
            color = 0
            if blank[y, x, 1] == 255 and blank[y, x, 2] == 0:
                # GREEN
                color = 2
            elif blank[y, x, 2] == 255 and blank[y, x, 1] == 0:
                # RED
                color = 1
            if color == prevY and prevY != 0:
                count += 1
            else:
                prevY = color
                count = 1
                startingToken = j
            if count == 4:
                return [1, startingToken, j]

    # Check Diagonal


    return [0, 0, 0]

def checkHowMuchToWin(player):
    # Finds the Min number of tokens required to win
    # Returns an integer
    return 0

def comparePoints():
    # Check whether it's better to add Token to Win or to spoil the PLAYER's move
    # Points System -> Min Number of tokens required to win < Min Number of tokens PLAYER requires to win
    # Return [xCord, yCord]
    return