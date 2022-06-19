import cv2
import numpy as np

# Constant variables
RADIUS = 25
COMPUTER = (0, 0, 255) # RED
PLAYER = (0, 255, 0) # GREEN

# Blank Screen
blank = np.ones(shape=[720, 1080, 3], dtype=np.uint8)*230

# Move Number
# Every odd move is made by player
move = 0

# Cirlces filled in each Column
filled = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

def drawEmptyBoard():
    global blank
    cv2.rectangle(blank, (40, 200), (1040, 700), (0, 0, 0), -1)

    # Draw circles (12x8)
    for i in range(0, 8):
        for j in range(0, 12):
            y = ((i+1)*12) + i*2*RADIUS
            x = ((j+1)*25) + j*2*RADIUS
            cv2.circle(blank, (x+90, y+225), RADIUS, (255, 255, 255), -1)

# Fills color in one circle showing that player/computer has played
def addToken(x, y, color):
    #    x -> [1,12]     y -> [1, 8]
    global blank, filled
    filled[x] = y
    x = x*25 + (x-1)*2*RADIUS + 90
    y = y*12 + (y-1)*2*RADIUS + 225
    cv2.circle(blank, (x, y), RADIUS, color, -1)

# call back function for mouse click event
# Checks whether the cell has already been clicked or not
def click_event(event, x, y, flags, params):
    global move, filled
    if event == cv2.EVENT_LBUTTONDOWN:
        xCord = checkClick(x, y)
        if(xCord > 0 and filled[xCord] < 8):
            yCord = filled[xCord]+1
            move += 1
            if move%2 == 1:
                addToken(xCord, yCord, PLAYER)
            else:
                addToken(xCord, yCord, COMPUTER)

# returns the cell numbers of the clicked cell
def checkClick(x, y):
    for i in range(0, 8):
        for j in range(0, 12):
            if x <= (j+1)*25 + j*2*RADIUS + 90 + RADIUS and x >= (j+1)*25 + j*2*RADIUS + 90 - RADIUS and y <= (i+1)*12 + i*2*RADIUS + 225 + RADIUS and y >= (i+1)*12 + i*2*RADIUS + 225 - RADIUS:
                return j+1
    return -1

drawEmptyBoard()

while True:
    cv2.imshow("Play Area", blank)
    cv2.setMouseCallback("Play Area", click_event)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break