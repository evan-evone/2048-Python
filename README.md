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

### Running the game

To run the game normally, type the following:

    ./2048.py

To run the game in debug mode, type the following:

    ./2048.py --debug

In debug mode, the computer will print information as
it is executing the commands to move tiles in any direction.
Additionally, input from the prompt ('>>> ') will be
interpreted as a Python3 command, if not a _u_, _d_, _l_, or
 _r_. Be careful, as a typo will cause your game to exit in
debug mode.

### Some commands to know in debug mode:

    board.change(<spot>, tile(<num>))
        # Will change the tile at <spot> (list: [x, y]) to the value of <num>
    
    [board.change(<spot>, tile(<num>)) for <index>, <spot> in enumerate(board.spots)]
        # Will change the all tiles to <num> (which can be an expression, such ass 2 ** <index>);
        # <index> and <spot> are any variable
    
    toggleSuppress()
        # Will turn print during tile movement on or off (default is on), while leaving commands enabled

### Note: renderer.py
On branch renderer, there is a file known as **renderer.py**. This
file is an experiment with deleting text after it is printed to "render"
and "re-render" objects–in this case the 2048 board–on the screen. Modification
and improvement upon this file are welcomed, but currently I cannot make this
idea work. If you have any ideas, _PLEASE_ fork the project and include them.
