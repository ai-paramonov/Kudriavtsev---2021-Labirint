from game2dboard import Board
import random as rd
import numpy as np
import pymsgbox

Diff = pymsgbox.confirm("WELCOME TO THE LABIRINT!\nControls:\n Left-Right-Up-Down arrows - to move\n M - return to choosing difficulty\nChoose your difficult",
                     "Welcome",['Easy','Normal','Hard'])
m = 0
n = 0
if Diff == 'Easy':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        m = 15
        n = 15
elif Diff == 'Normal':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        m = 20
        n = 20
elif Diff == 'Hard':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        m = 25
        n = 25
lastkey = ""
player = []
rotation = ""

def walls():
    global m,n
    if Diff == 'Easy':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        mass = np.array([
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
                            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                            [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
                            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                            [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                            [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
                            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1],
                            [2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        m = 15
        n = 15
        
    elif Diff == 'Normal':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        mass = np.array([
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                    [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],                    
                    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 2],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],                    
                    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
        m = 20
        n = 20
    elif Diff == 'Hard':
        FIELD_WIDTH = 25
        FIELD_HEIGHT = 25
        BLOCK_SIZE = 30
        m = 25
        n = 25
        mass = np.array([
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    for i in range(m):
        for j in range(n):
            if mass [i][j] == 1:
                field [i][j] = 'WALL'
            elif mass [i][j] == 2:
                    field [i][j] = 'EXIT'
        
def keysPress(key):
    global lastkey,Diff
    if key == "m" or key == "M":
        Diff = ""
        start()
    elif key in ["Left","Right","Up","Down"]:
        lastkey = key

def move():
    global lastkey, rotation
    flag = False
    head_row,head_col = player[0]
    if lastkey == "Left" and field[head_row][head_col-1] != 'WALL':
        head_col -=1
        flag = True
        rotation = "L"
    elif lastkey == "Right" and field[head_row][head_col+1] != 'WALL':
        head_col +=1
        flag = True
        rotation = "R"
    elif lastkey == "Up" and field[head_row-1][head_col] != 'WALL':
        head_row -=1
        flag = True
    elif lastkey == "Down" and field[head_row+1][head_col] != 'WALL':
        head_row +=1
        flag = True
    if rotation == "L":
            field[head_row][head_col] = "PlayerL"
    else:
            field[head_row][head_col] = "PlayerR"
    if flag:
        player.insert(0,(head_row,head_col))
        last_row,last_col = player[-1]
        field[last_row][last_col] = None
        player.pop()
    if head_col <= 0 or head_row<= 0 or head_col>=m-1 or head_row>=n-1:
        field.stop_timer()
        endm = pymsgbox.confirm("Congratulations! You Win!\nRestart?",
                             "Restart?",["Yes","No"])
        lastkey = ""
        if endm == "Yes":
            start()
            return
        else:
            field.close()
    lastkey = ""
def start():
    global player,Diff
    if Diff == "":
        Diff = pymsgbox.confirm("Controls:\n Left-Right-Up-Down arrows - to move\n M - return to choosing difficulty\nChoose your difficult",
                         "Difficult",['Easy','Normal','Hard'])
    field.fill(None)
    walls()
    wc = m // 2
    hc = n // 2
    field [hc][wc] = "Player"
    player = [(hc,wc)]
    lastkey = ""
    field.start_timer(300)

    
field = Board(FIELD_HEIGHT, FIELD_WIDTH)
field.cell_size = BLOCK_SIZE
field.title = "Labirint"
field.grid_color = "DarkGray"
field.cell_color = "DarkGray"
field.on_key_press = keysPress
field.on_timer = move
start()
field.show()
