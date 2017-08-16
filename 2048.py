#!/usr/bin/env python

#
#  ______      _                   _     _ _                    _          
#  |  _  \    | |          ___    | |   (_| |                  (_)         
#  | | | |__ _| |_ __ _   ( _ )   | |    _| |__  _ __ __ _ _ __ _  ___ ___ 
#  | | | / _` | __/ _` |  / _ \/\ | |   | | '_ \| '__/ _` | '__| |/ _ / __|
#  | |/ | (_| | || (_| | | (_>  < | |___| | |_) | | | (_| | |  | |  __\__ \
#  |___/ \__,_|\__\__,_|  \___/\/ \_____|_|_.__/|_|  \__,_|_|  |_|\___|___/
#                                                                          
#                                                                          

from board import board
from sys import argv                                                                    # for debug
import random                                                                           # for new spots
import time                                                                             # for debug instructions
import os

debug = False
suppressPrint = True
if '--debug' in argv or '-db' in argv:
    debug = True
    suppressPrint = False

twoPlayer = False
localmt = False
if '-t' in argv or '--two-player' in argv:
    twoPlayer = True
    if '-l' in argv or '--local' in argv:
        localmt = True

game = ''
doCatchup = False
if localmt:
    game = input('Game Name: ') + '.txt'
    if game == '.txt': game = 'game.txt'
    
    if debug and not suppressPrint: print(game)
    if debug and not suppressPrint: 
        print(os.popen('if [ -f {0} ]; then echo true; fi'.format(game)).read())
    
    startup = True
    if len(os.popen('if [ -f {0} ]; then echo true; fi'.format(game)).read()) > 0:
        if input('Game File Found. Would you like to import the game? ') in\
            ['yes', 'Yes', 'y', 'Y']:
            doCatchup = True
            startup = False                                                             # says that new file need not be created.
            if debug and not suppressPrint:
                myfile = open(game, 'r')
                print(myfile.read())
                myfile.close()

#
#  ______      __ _       _ _   _                 
#  |  _  \    / _(_)     (_| | (_)                
#  | | | |___| |_ _ _ __  _| |_ _  ___  _ __  ___ 
#  | | | / _ |  _| | '_ \| | __| |/ _ \| '_ \/ __|
#  | |/ |  __| | | | | | | | |_| | (_) | | | \__ \
#  |___/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
#                                                 
#                                                 

class thisBoard(board):                                                                 # Modifications for what is necessary
    def __init__(self, comp, width, height):
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], 
                           [0, 1], [1, -1], [1, 0], [1, 1]]
        self.width = width
        self.height = height
          # self.represent = []                                                         # no use for self.represent 
        self.spots = []
        for x in range(width):
            for y in range(height):
                self.spots.append([x, y])
        
        for i in range(height):
            self.append([])
              # self.represent.append([])
            for x in range(width):
                self[i].append(comp)
                  # self.represent[i].append(' ' + str(comp) + ' ')
    
    def change(self, lst, new):
        self[lst[1]][lst[0]] = new
        self.update()
    
    def update(self):
        self.spots = []
        for x in range(self.width):
            for y in range(self.height):
                if not self.get([x, y]).num:
                    self.spots.append([x, y])
    
    def showBoard(self):
        rslt = '\n'
        for x in self[::-1]:
            for y in range(3):
                rslt += ' '.join([z[y] for z in x]) + '\n'
            rslt += '\n'
        return(rslt)
    
    def doMove(self, udlr=None):
        if udlr is None: return()
        duplicate = [[x.num for x in y] for y in self]
        if debug and not suppressPrint: print(duplicate)                                # testing

        if udlr == 'u':
            duplicate = [[y[x] for y in duplicate] for x in range(self.height)]
            if debug and not suppressPrint: print(duplicate)                            # testing
            duplicate = moveAll(duplicate)
            for ind0, x in enumerate(duplicate):
                for ind1, y in enumerate(x):
                    self.change([ind0, ind1], tile(y))
            return(duplicate)

        elif udlr == 'd':
            duplicate = [[y[x] for y in duplicate[::-1]] for x in range(self.height)]   
            if debug and not suppressPrint: print(duplicate)                            # testing
            duplicate = moveAll(duplicate)
            for ind0, x in enumerate(duplicate):
                for ind1, y in enumerate(x[::-1]):
                    self.change([ind0, ind1], tile(y))
            return(duplicate)

        if udlr == 'l':
            duplicate = [y[::-1] for y in duplicate]
            if debug and not suppressPrint: print(duplicate)                            # testing
            duplicate = moveAll(duplicate)
            for ind1, x in enumerate(duplicate):
                for ind0, y in enumerate(x):
                    self.change([3 - ind0, ind1], tile(y))
            return(duplicate)

        if udlr == 'r':
            duplicate = [y for y in duplicate]
            if debug and not suppressPrint: print(duplicate)                            # testing
            duplicate = moveAll(duplicate)
            for ind1, x in enumerate(duplicate):
                for ind0, y in enumerate(x):
                    self.change([ind0, ind1], tile(y))
        if debug and not suppressPrint: print(duplicate)
        return(duplicate)

class tile(list):
    def __init__(self, num=''):
        if num == '':
            num = 0
        self.num = int(num)
        for x in range(3):
            self.append('[     ]')
        self.update()
    
    def update(self):
        self[1] = '[{:^5}]'.format(self.num)
        if self.num == 0:
            self[1] = '[{:^5}]'.format('')
        return(self)
          
    def numSet(self, num):
        self.num = num

def moveAll(lst):
    for row in lst:
        for index in range(len(row)):
            going2 = True
            while going2:
                for num in range(index):
                    if debug and not suppressPrint: print(index, num, row)              # testing
                    if type(row[num]) is str:
                        if int(row[num + 1]) == 0:
                            row[num + 1] = row[num]; row[num] = 0
                    elif row[num] > 0 and int(row[num + 1]) == 0:
                        row[num + 1] = row[num]; row[num] = 0
                    elif row[num] == row[num + 1]:
                        row[num + 1] = str(2 * row[num]); row[num] = 0
                    if debug and not suppressPrint: print()                             # testing
                    
                true = True
                true2 = True
                for x in range(index):
                    if int(row[x]) != 0:
                        true2 = False
                    if not true2 and int(row[x]) == 0:
                        true = False
                if true:
                    going2 = False
                    
        row = [int(x) for x in row]
    return(lst)

def showBoards():
    rslt = 'Player 1:' + ' ' * (8 * 4 - 1) + 'Player 2:' +'\n' * 2
    foo = [[board1[x], board2[x]] for x in range(len(board1))]
    if debug and not suppressPrint: print(foo)
    for x in foo[::-1]:
        for y in range(3):
            rslt += ' '.join(z[y] for z in x[0]) + '\011\011'                           # horizontal-tab
            rslt += ' '.join(z[y] for z in x[1]) + '\n'
        rslt += '\n'
    return(rslt)

def export(turn, lst, name=game):
    myfile = open(name, 'w')
    if not localmt: return('fatal: local multiplayer is not active')                    # currently only save for multiplayer for ease
    dic = {}
    for x in range(board1.width):
        for y in range(board1.height):
            dic['[{0}, {1}]'.format(x, y)] = \
                [board1.get([x, y]).num, board2.get([x, y]).num]
    mystr = '{0}\n{1}\n{2}\n'.format(turn, dic, lst)
    myfile.truncate(0)
    myfile.write(mystr)
    if debug and not suppressPrint: print(mystr)                                        # make sure things are correct
    myfile.close()


def catchup(boards, name=game):
    myfile = open(name, 'r')
    global turn
    global players
    turn = eval(myfile.readline())
    dic = eval(myfile.readline())
    players = eval(myfile.readline())
    myfile.close()
    if debug and not suppressPrint: print(turn, dic, sep='\n')                          # make sure things are correct
    for spot in [eval(x) for x in dic.keys()]:
        for y, x in enumerate(boards):
            x.change(spot, tile(dic[str(spot)][y]))

def toggleSuppress():
    global suppressPrint
    suppressPrint = not suppressPrint

#
#   _____      _               
#  /  ___|    | |              
#  \ `--.  ___| |_ _   _ _ __  
#   `--. \/ _ | __| | | | '_ \ 
#  /\__/ |  __| |_| |_| | |_) |
#  \____/ \___|\__|\__,_| .__/ 
#                       | |    
#                       |_|    

if debug:
    print('Debug mode: ON')
    print('All suppressed output will be displayed')
    print('Input will be evaluated as python3 input')
    time.sleep(3)
if not twoPlayer:
    board = thisBoard(tile(), 4, 4)
    print(board.showBoard())
    for x in range(2):
        foo = random.choice(board.spots)
        board.change(foo, tile(2))

if twoPlayer:
    board1 = thisBoard(tile(), 4, 4)
    board2 = thisBoard(tile(), 4, 4)
    print(showBoards())
    for x in range(2):
        foo1 = random.choice(board1.spots)
        foo2 = random.choice(board2.spots)
        board1.change(foo1, tile(2))
        board2.change(foo2, tile(2))
    
    turn = 0

    if startup:
        players = [''.join(os.popen('tty').read().split()), input('Path to P2 tty: ')]
        export(0, players)

    if doCatchup: catchup([board1, board2])
    print(showBoards())

going = True

#
#   _____                        _                       
#  |  __ \                      | |                      
#  | |  \/ __ _ _ __ ___   ___  | |     ___   ___  _ __  
#  | | __ / _` | '_ ` _ \ / _ \ | |    / _ \ / _ \| '_ \ 
#  | |_\ | (_| | | | | | |  __/ | |___| (_) | (_) | |_) |
#   \____/\__,_|_| |_| |_|\___| \_____/\___/ \___/| .__/ 
#                                                 | |    
#                                                 |_|    

while going:
    if twoPlayer:
        going3 = True                                                                   # True until good input received
        if localmt:
            catchup([board1, board2])
            if debug and not suppressPrint:
                print(players[turn])
                print(''.join(os.popen('tty').read().split()))
            if not players[turn] == ''.join(os.popen('tty').read().split()):
                going3 = False                                                          # Will stop input loop until change in file
                print('Waiting for player {0}.'.format(turn + 1), end='\r')             # Note '\r' to stop message from overflowing terminal
        while going3:
            order = input(showBoards() + ['>>> ', '... '][turn])                        
            if order in ['u', 'd', 'l', 'r']:
                board1.doMove(order)
                board2.doMove(order)
                going3 = False
                turn = turn ^ 1
                if localmt:
                    
                    foo1 = random.choice(board1.spots)
                    foo2 = random.choice(board2.spots)
                    if debug and not suppressPrint: print([foo1, foo2])
                    board1.change(foo1, tile(2))
                    board2.change(foo2, tile(2))

                    print(showBoards())
                    export(turn, players)
            elif debug:
                eval(order)
            else:
                print('Error: Unknown direction:')
                print('Direction must be a \'u\', \'d\', \'l\', or \'r\'.')
        
        if len(board1.spots) == 0:                                                      # check for game over.
            print('Player 2 Wins!'); break
        elif len(board2.spots) == 0:
            print('Player 1 Wins!'); break
        else:
            foo1 = random.choice(board1.spots)
            foo2 = random.choice(board2.spots)
            if debug and not suppressPrint: print([foo1, foo2])
            board1.change(foo1, tile(2))
            board2.change(foo2, tile(2))
        
    else:
        going3 = True                                                                   # True until good input received
        while going3:
            order = input(board.showBoard() + '>>> ')
            if order in ['u', 'd', 'l', 'r']:
                board.doMove(order)
                going3 = False
            elif debug:
                eval(order)
            else:
                print('Error: Unknown direction: ')
                print('Direction must be a \'u\', \'d\', \'l\', or \'r\'.')
    
        if len(board.spots) == 0:                                                       # check for game over
            print(board.showBoard())
            score = 0
            for x in board:
                for y in x:
                    score += y.num
            print('Game Over!\nYour Score: {0}.'.format(score))
            break
        else:                                                                           # add new tile
            foo = random.choice(board.spots)
            if debug and not suppressPrint: print(foo)
            board.change(foo, tile(2))
