py2048
======

Play the popular game of 2048

A PyGTK implementation of `Gabriele Cirulli's game of
2048 <https://github.com/gabrielecirulli/2048>`__ which is itself a
clone of
`1024 <https://play.google.com/store/apps/details?id=com.veewo.a1024>`__
and based on `Saming's 2048 <http://saming.fr/p/2048/>`__ (also a
clone).

Installation
------------

Open a terminal and enter the following command:

::

    pip install py2048-game

In case you don't have the right things installed and you don't feel
like installing them, there is still the old way that I created before I
learned setuptools:

::

    wget https://raw.githubusercontent.com/ralphembree/py2048/master/install.sh -q -O - | bash

The old way does a little bit more than the new way because I'm still
learning the new way. Either one will create the py2048 executable, so
the game can be started from the command prompt with a simple "py2048".
The old way, in addition, puts an entry in your Games menu.

Features
--------

-  Moves can be undone with the click of a button.
-  Games can be saved in user-specified files to be resumed later.
-  Grid can be resized to preference.
-  In addition to the keyboard, there are two kinds of mouse
   interaction:
-  Swipe: click and hold and then move in the direction desired
-  Click: each section of the grid (top, bottom, left, right) when
   clicked will move the tiles in a different direction. The cursor will
   be an arrow pointing in the direction the tiles would go if you
   clicked.
-  The colors in the grid can be rerandomized at any time (without
   messing up your game).

Screenshot
----------

.. figure:: https://github.com/ralphembree/py2048/blob/master/screenshot.gif
   :alt: Screencapture of game

How to play
-----------

The arrow keys determine which direction all of the tiles move. Tiles
with the same number that hit each other merge into one tile. Each time
tiles are moved, another tile is added to the board. The game is over
when no more tiles can be merged.

Shortcut keys
-------------

+------------------------+----------------------------------------+
| Key                    | Action                                 |
+========================+========================================+
| ``Alt-N``              | Start new game                         |
+------------------------+----------------------------------------+
| ``Ctrl-N``             | New grid size (user defined)           |
+------------------------+----------------------------------------+
| ``Alt-U``/``Ctrl-Z``   | Undo                                   |
+------------------------+----------------------------------------+
| ``Ctrl-C``             | New color scheme                       |
+------------------------+----------------------------------------+
| ``Ctrl-M``             | Toggle mouse modes (swipe or click)    |
+------------------------+----------------------------------------+
| ``Ctrl-O``             | Load saved game                        |
+------------------------+----------------------------------------+
| ``Ctrl-Shift-S``       | Save game under a different name       |
+------------------------+----------------------------------------+
| ``Ctrl-S``             | Save game to previously-defined file   |
+------------------------+----------------------------------------+
| ``F11``                | Toggle fullscreen                      |
+------------------------+----------------------------------------+
| ``F1``                 | Help                                   |
+------------------------+----------------------------------------+
| ``Ctrl-Q``             | Quit                                   |
+------------------------+----------------------------------------+

License
-------

py2048 is a Python implementation of the popular game of 2048. Copyright
© 2014 Ralph Embree

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

This program is destributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see http://www.gnu.org/licenses
