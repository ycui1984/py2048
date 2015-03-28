py2048
======

Play the popular game of 2048

A PyGTK implementation of [Gabriele Cirulli's game of 2048](https://github.com/gabrielecirulli/2048) which is itself a clone of [1024](https://play.google.com/store/apps/details?id=com.veewo.a1024) and based on [Saming's 2048](http://saming.fr/p/2048/) (also a clone).

##Installation
1. sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/py2048 -O /usr/bin/py2048
2. sudo chmod +x /usr/bin/py2048
3. sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/2048.png -O /usr/share/icons/hicolor/64x64/apps/py2048.png

##Screenshot

<p align="center">
  <img src="https://github.com/ralphembree/py2048/blob/master/screenshot.png" alt="Screenshot"/>
</p>

##Features
* There is an undo button.  You can guess what it does.
* You can save your game to a file and open it later.
* You can change the size of your grid.
* There are two kinds of mouse interaction possible (toggled by a menu item)

### The two kinds of mouse interaction are:
* Swipe: click and hold and then move in the direction desired
* Click: each section of the grid (top, bottom, left, right) will move the tiles in a different direction.  The cursor will be an arrow pointing in the direction the tiles would go if you clicked.

## License
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

