#!/usr/bin/env python

  # Default board --> Numbered like a coordinate plane
class board(list):
   def __init__(self, comp, width, height):
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.width = width
      self.height = height
      self.represent = []
      self.spots = []
      for x in range(width):
         for y in range(height):
            self.spots.append([x, y])
      
      for i in range(height):
         self.append([])
         self.represent.append([])
         for x in range(width):
            self.represent[i].append(' ' + str(comp) + ' ')
            self[i].append(comp)
      
   def showBoard(self):
      print()
      for x in self.represent[::-1]:
         print(''.join(x))
   
   def showList(self):
      print()
      for x in self.represent:
         print(x)
   
   def showActual(self):
      print()
      for x in self:
         print(x)
   
   def get(self, lst):
      return self[lst[1]][lst[0]]
   
   def change(self, lst, str):
      str = str.lower()
      self[lst[1]][lst[0]] = str
      self.represent[lst[1]][lst[0]] = ' ' + str + ' '
   
   def show(self, str):
      pos = self.find(str)
      if not pos[0]:
         return
      start = pos[1][0]
      dir = pos[1][1]
      for x in range(len(str)):
         newPos = [start[0] + dir[0] * x, start[1] + dir[1] * x]
         self.represent[newPos[1]][newPos[0]] = '[' + str[x].upper() + ']'
      
   def find(self, str):
      str = str.lower()
      rslt = []
      
      #Finding starting spots
      startSpots = []
      char = str[0]
      for y in range(self.height):
         spots = []
         lst = list(''.join(self[y]))
         spots = [g for g, h in enumerate(lst) if char == h]
         for x in spots:
            startSpots.append([x, y])
      
      char = str[1]
      mayWork = []
      
      #Finding Working Spots and Directions
      for x in startSpots:
         for y in self.directions:
            newSpot = [x[0]+y[0], x[1]+y[1]]
            if 0 <= newSpot[0] < self.width:
               if 0 <= newSpot[1] < self.height:
                  if char in list(self.get(newSpot)):
                     mayWork.append([x, y])
      
      #Checking if the possibilities actually work
      works = []
      for x in mayWork:
         working = True
         for y in range(len(str)):
            char = str[y]
            curSpot = [x[0][0]+(y*x[1][0]), x[0][1]+(y*x[1][1])]
            if working:
               if 0 <= curSpot[0] < self.width and 0 <= curSpot[1] < self.height:
                  if char == self.get(curSpot):
                     working = True
                  else:
                     working = False
               else:
                  working = False
         
         if working and works == []:
            works = x
      
      if works != []:
         rslt = [True, works]
      else:
         rslt = [False]
   
      return rslt

  # A textboard using more standard numbers/orders (i.e. for ws)
class textBoard(board):
   def showBoard(self):
      print()
      for x in self.represent:
         print(''.join(x))
   def showList(self):
      print()
      for x in self.represent:
         print(x)
   def showActual(self):
      print()
      for x in self:
         print(x)
