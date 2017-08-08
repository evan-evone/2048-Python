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

### Running the game

To run the game normally, type the following:

    $ ./2048.py

To run the game in debug mode, type the following:

    $ ./2048.py --debug  OR  $ ./2048.py -db

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

# 2048 - Python - Two Players
### Also for the command line

    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    [  1  ] [  8  ] [ 256 ] [  2  ]     [  1  ] [  4  ] [ 16  ] [2048 ]
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    [  4  ] [ 16  ] [  2  ] [2048 ]     [  4  ] [  8  ] [ 256 ] [  4  ]
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    [  1  ] [ 256 ] [2048 ] [  4  ]     [  4  ] [ 64  ] [  4  ] [  1  ]
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]
    [  2  ] [ 16  ] [ 32  ] [  2  ]     [     ] [  4  ] [  8  ] [  2  ]
    [     ] [     ] [     ] [     ]     [     ] [     ] [     ] [     ]


The two player game works with the same
controls, but the players each have their own
board, and take turns making moves. Additionally,
moves made by Player 1 will also occur on
Player 2's board, adding an element of strategy
to the game. This game also has a debug mode.

The first player who has no room for new tiles loses,
and the other is declared the winner.

### Running for two players

To run the game normally, type the following:

     $ ./2048.py --two-player  OR  $ ./2048.py -t

To run the game in debug mode, type the following:

    $ ./2048.py --two-player --debug  OR  $ ./2048.py -t -db

Commands in debug mode are the same.
