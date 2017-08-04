# 2048 - Python

### A command-line version

    [     ] [     ] [     ] [     ]
    [     ] [ 128 ] [ 64  ] [  8  ]
    [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]
    [  4  ] [ 32  ] [ 16  ] [  1  ]
    [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]
    [ 16  ] [ 64  ] [  1  ] [  4  ]
    [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]
    [  4  ] [     ] [  8  ] [     ]
    [     ] [     ] [     ] [     ]


This repository will eventually include a python
file for a single-player game, the option to run a
computer simulation of the game, and (possibly),
the ability to run a two player game. The idea is,
of course, the same as that of the original game.
The main differnce is that _u_, _d_, _l_, and _r_
are used instead of swipes, arrow keys, or any
other form of input.

The main script - **2048.py** - runs with the library
in **board.py**, which contains code for creating lists
that act as &rdquo;boards.&ldquo; Some of the functions
are modified by **2048.py** to be more appropriate for
what is necessary for 2048. 

The two player game will work with the same
controls, but the players will each have their own
board, and take turns making moves. Additionally,
move is made by player one will also occur on
player two's board, adding an element of strategy
to the game.
