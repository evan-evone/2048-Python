#!/usr/bin/env python

from board import board
import random

#
#  ______      __ _       _ _   _                 
#  |  _  \    / _(_)     (_| | (_)                
#  | | | |___| |_ _ _ __  _| |_ _  ___  _ __  ___ 
#  | | | / _ |  _| | '_ \| | __| |/ _ \| '_ \/ __|
#  | |/ |  __| | | | | | | | |_| | (_) | | | \__ \
#  |___/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
#                                                 
#                                                 

class thisBoard(board): # Slight modifications for what is necessary
    def __init__(self, comp, width, height):
        self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], 
                           [0, 1], [1, -1], [1, 0], [1, 1]]
        self.width = width
        self.height = height
          # no use for self.represent
          # self.represent = []
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
          # print(duplicate) # testing

        if udlr == 'u':
            duplicate = [[y[x] for y in duplicate] for x in range(self.height)]
              # print(duplicate) # testing
            duplicate = moveAll(duplicate)
            for ind0, x in enumerate(duplicate):
                for ind1, y in enumerate(x):
                    self.change([ind0, ind1], tile(y))
            return(duplicate)

        elif udlr == 'd':
            duplicate = [[y[x] for y in duplicate[::-1]] for x in range(self.height)]
              # print(duplicate) # testing
            duplicate = moveAll(duplicate)
            for ind0, x in enumerate(duplicate):
                for ind1, y in enumerate(x[::-1]):
                    self.change([ind0, ind1], tile(y))
            return(duplicate)

        if udlr == 'l':
            duplicate = [y[::-1] for y in duplicate]
              # print(duplicate) # testing
            duplicate = moveAll(duplicate)
            for ind1, x in enumerate(duplicate):
                for ind0, y in enumerate(x):
                    self.change([3 - ind0, ind1], tile(y))
            return(duplicate)

        if udlr == 'r':
            duplicate = [y for y in duplicate]
            print(duplicate) # testing
            duplicate = moveAll(duplicate)
            for ind1, x in enumerate(duplicate):
                for ind0, y in enumerate(x):
                    self.change([ind0, ind1], tile(y))
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
            for num in range(index):
                  # print(index, num, row) # testing
                if row[num] == row[num + 1] or row[num + 1] == 0:
                    row[num + 1] += row[num]; row[num] = 0
                  # print() # testing
    return(lst)

#
#   _____      _               
#  /  ___|    | |              
#  \ `--.  ___| |_ _   _ _ __  
#   `--. \/ _ | __| | | | '_ \ 
#  /\__/ |  __| |_| |_| | |_) |
#  \____/ \___|\__|\__,_| .__/ 
#                       | |    
#                       |_|    

board = thisBoard(tile(), 4, 4)
print(board.showBoard())
for x in range(4):
    foo = random.choice(board.spots)
    board.change(foo, tile(2))
    print(board.showBoard())

  # print(board.doMove('u')) # working
  # print(board.showBoard())
  # print(board.doMove('d')) # working
  # print(board.showBoard())
  # print(board.doMove('l')) # working
  # print(board.showBoard())
  # print(board.doMove('r')) # working
  # print(board.showBoard())
