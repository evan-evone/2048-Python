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
