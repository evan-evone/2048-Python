#!/usr/bin/env python

import os
import time
from sys import argv

debug = False
if '--debug' in argv:
    debug = True

class ttysRenderer(str):
    size = [int(x) for x in os.popen('stty size').read().split()[::-1]]
    def __init__(self, body):
        self = body

    def render(self, prStr=0): 
        if type(prStr) is not str:
            prStr = self
        self.size = [int(x) for x in os.popen('stty size').read().split()[::-1]]
        lst = prStr.split('\n')
        new = []
        for ind, string in enumerate(lst):
            while len(string) > self.size[0]:
                part1 = string[:self.size[0]:]
                part2 = string[self.size[0]::]
                new.append(part1)
                string = part2
            new.append(string)
        lst = new
        if debug: print(self.size, prStr, lst)
        
        rslt = []
        for x in range(self.size[1]):
            if x < len(lst):
                y = lst[x]
                rslt.append(y + ' ' * (self.size[0] - len(y)))
            else:
                rslt.append(' ' * self.size[0])
        if debug: print(len(rslt), rslt); time.sleep(3)
        print('\r' + ''.join(rslt), end='')
        return(rslt)


renderer = ttysRenderer('Hello World!\nFoo and bar!\n' + 'a' * 365 + '\nFoo and bar (2)')
print(renderer.size)
foo = renderer.render()
if debug: print(foo)
time.sleep(3)
foo = [renderer.render(''.join(['Hello World! ({0})\n'.format(x) for x in range(60)]))]
if debug: print(foo)
time.sleep(3)
