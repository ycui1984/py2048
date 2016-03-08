py2048
======

Play the popular game of 2048

A PyGTK implementation of [Gabriele Cirulli's game of 2048](https://github.com/gabrielecirulli/2048) which is itself a clone of [1024](https://play.google.com/store/apps/details?id=com.veewo.a1024) and based on [Saming's 2048](http://saming.fr/p/2048/) (also a clone).

##Installation
Open a terminal and enter the following command:

    wget https://raw.githubusercontent.com/ralphembree/py2048/master/install.sh -q -O - | bash

This will put the executable file in /usr/games.
To run the program, simply type py2048 into the command prompt or click py2048 in your Games menu.

##Features
* There is an undo button.  You can guess what it does.
* You can save your game to a file and open it later.
* You can change the size of your grid.
* There are two kinds of mouse interaction possible (toggled by a menu item)
* The colors in the grid can be rerandomized at any time (without messing up your game)

###The two kinds of mouse interaction are:
* Swipe: click and hold and then move in the direction desired
* Click: each section of the grid (top, bottom, left, right) will move the tiles in a different direction.  The cursor will be an arrow pointing in the direction the tiles would go if you clicked.

##Screenshot

<p align="center">
  <img src="https://github.com/ralphembree/py2048/blob/master/screenshot.gif" alt="Screenshot-gif"/>
</p>

##How to play

The arrow keys determine which direction all of the tiles move.  Tiles with the same number that hit each other merge into one tile.  Each time tiles are moved, another tile is added to the board.  The game is over when no more tiles can be merged.

##Shortcut keys:

`Alt-N` Start new game
`Ctrl-N` New grid size (user defined)
`Alt-U`/`Ctrl-Z` Undo
`Ctrl-C` New color scheme
`Ctrl-M` Toggle mouse modes (swipe or click)
`Ctrl-O` Open saved game
`Ctrl-Shift-S` Open save game dialog
`Ctrl-S` Save game to previously defined file
`F11` Toggle fullscreen
`F1` Help
`Ctrl-Q` Quit

##License
py2048 is a Python implementation of the popular game of 2048.
Copyright © 2014 Ralph Embree

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is destributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program.  If not, see [http://www.gnu.org/licenses](http://www.gnu.org/licenses).

