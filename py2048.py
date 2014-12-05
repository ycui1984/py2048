#!/usr/bin/python2.7

# py2048 is a linux version of the popular game of 2048.
# Copyright (C) 2014 Ralph Embree
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is destributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from math import log
from sys import argv
from string import replace

from gtk import *
from random import random, randint, choice
from threading import Thread
from traceback import format_exception
import pickle
import os
import time


#Do not change this line or the one after it.
high_score = {(12, 12): 660, (4, 4): 975368, (12, 4): 52}
class dummy(object):
    pass

class Game(object):
    def __init__(self):
        data = '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\x00\x000\x08\x02\x00\x00\x00\xd8`n\xd0\x00\x00\x00\x03sBIT\x08\x08\x08\xdb\xe1O\xe0\x00\x00\x00\x18tEXtSoftware\x00mate-screenshot\xc8\x96\xf0J\x00\x00\x033IDATX\x85\xed\xd7[H\x14Q\x18\xc0\xf1\xef\x9c\x99\xdd\x9d\xdd5\xd7KZ\x14XN\x16\xb4\x85P&X\xd1\xcd\x82,\xa22)+\xac\x87\x82\x8a\xeeDi!\x15v\xa3\xb0\xe8\x0e\xdd\xa8\xa8,LB\x82(\xba\x1b\x85(\xdd\xa8\xb4\xa2{\xa9I\x1a\xab\xeeevf\xf6\xcc\x9c\x1e\xdc\xca\x82\xed\x80/\x15\x9c\xff\xe3|\x9c\x9d\xdf|\x9c\x97E\x94\xa6\xc1\xbf\x14\xfe\xdb\x80\xdf\xe3 V\x1c\xc4\x8a\x83Xq\x10+\x0eb\xc5A\xac8\x88\x15\x07\xb1\xfa\x7f@T!\xa7\n|c\x07yd\xd9\xd3\x7f\xb8w}\xb9\x11\xa4\xe1\x91\xd9\x16:\xbc\xb0m\xa0\xec\x91S\xdb\x96\x9d0\xfc\xf4\x97\x83\xa1\xf7jv\x8aG\xce\xd6\x9b\xcc\xf0\x13\xe5\x95\x96?\xa5\xa5\xaf\xec\x91\xfb\xb5\xe6\x14j\xef\xd4\xce\x81T\xea\x89\xb3\xac;\xee\xaa\xac\x8e9\xb5\x00_^\xed;\xf8\xb2}`\xde\xdd\xe8\xdf\xdfj;\xfb(\xf6\xe1Ik\xfd.\xdf\xd6*\xfa\x93d\x98\xe5E\xaa\xe6F\xe2\x8f\'\xbaqt\xb1r\xb7\xbf\xf3fm\\\xcdUG\xd2\xf5\xc0\xf2\x12\x93t\x02\x84\xe3,+\x0b\xa4q\x83\x84\xee\t8}\xa6=\xb7\xa7Y\xf5\x9aR\x00\xf0\x1a\xa7o\xa1)\xf9\xb6\xd4\x18\x14;X\xca\x1fO\xaf\x9c!\x81\xef_\xd1|M9\x04\xf6\x82L\xfc\xf3wu\xb3\xe6\x0b\x1a=\xdd\x92d\x07G\xb25w\x18n\xac5\xf4N\x80:f|%\xf7=8M\x06\x04\x10j"\xefB8\xbd\x17j\x1f%\x0f\xc1\xda\x1b\xd2L\x00\x00\xccVR\\l\xce\\o\xed!t8l\x17&g\xd0{e\xa4.\x08\xca\x07\xbd\xb4\x1a\x86f\x89R\xe4w\x89\x91G\xe1\xa8B\x8e\xaeP\x1a\'9\x17\xb9\x11\x00\x18*U\x01\xa2l\xedCd\x8bF\xa0R\xd5\x04\xa0\xf4\xf1~\xe5YVTQ\x1f\xd4\xd0\xf1\xbc\x80\xb36:oL\xf7\x8d\x1a\x00\x00\xd0cjTY&\xfa\xc3\x1aX\x1bR\x8d\x92%\xbe\xe3q\x8e3E\xd6X\x0c\x00 HH\x02\x08\x84\x97N5\x1f\x05\tI\x18\xd4\x17\xea\x86[\xe2\x86E\x82\xfd\xb7\xef\xf1\x93\xcd\xb3\x03\x9f\xf3\xa2\xab^\xc6>\xaf\x8c\x9e\xf66\x90WL\x82\x9d\x04i\xc6\xb9\xa5\xde\xdd\xa6\xbdd\xaf\xadwx%`I\x14\x93-\xe6\x83O\xed\xf7\x18}|hJ)b\x82H[\x1e\xeb/>\xea\xf32Z\xdc\xee\x96\x89\xbb\r\xfd\x89\x7f\xd4\x08\x7fe\x00Bu\xfa\x9d&a\xee,1\xd1\x8a\xa4\xee\xc2\xac\\\xdcp\x9b4F\xbe\xd5\x91A\xbaY\xb6\xc2\xbb\xadU:\xb6\xc7\x96\x84\xa9\xa6\xd1\x90\x01\x00\x00\xd1\xc2\x9cLzq\xa7\xf6\xdc\x0f\xde\xa7\xc1\x9dWPV\x9e\xe8\x04\xd4-\xa7Ku\x95\xebN\x85\xab\xa2\xc2uz\x81 \xba\x1d\x17\xca\x9d\xe9\x0e\x10\x13EY4J\xca\x88\x87@\xa8\x99\x9c/5l)B\xbc\x10\xf1\xb5\x11\xefP\xa8^?r\x8d\x06 \x98\x93\x16^p\xbf\xc2\x98K\xf3\xb1\x88\xf0\xc8\xa2\xa8\xc5k\x023R\x15\xc5)LX\xd5\xa50\x03!\x00$\xe1\x84\xefw\xd5\xeb\x04l\xc1]\xbb"\x0b\x02\x88\xb7n\xdfG\xd6n\xf1\r\xd9A\x01\xa1>c\xec\x076Y\\("\x08\xf1\xff\xf6\x8c8\x88\x15\x07\xb1\xe2 V\x1c\xc4\x8a\x83Xq\x10+\x0eb\xc5A\xac8\x88\xd57GzA*\xe6\x01@\x99\x00\x00\x00\x00IEND\xaeB`\x82'
        loader = gdk.PixbufLoader("png")
        loader.write(data)
        loader.close()
        pixbuf = loader.get_pixbuf()
        self.pixbuf = pixbuf
        window = Window()
        window.set_icon(pixbuf)
        self.delete_id = window.connect("delete-event", self.on_destroy)
        self.is_fullscreen = False
        window.connect("window-state-event", self.on_fullscreen_event)
        window.connect("configure-event", self.update_fonts)
        window.set_default_size(315, 400)
        window.set_title("2048")
        window.set_position(WIN_POS_CENTER)

        ev = EventBox()
        vbox = VBox()
        upper_hbox = HBox()
        lower_hbox = HBox()

        menu_items = (
            ("/_Game", None, None, 0, "<Branch>"),
            ("/Game/_Convert mouse", "<control>M", lambda widget, event: self.switch_mouse_mode(), 0, "<Item>"),
            ("/Game/", None, None, 0, "<Separator>"),
            ("/Game/_New Grid", "<control>N", self.new_grid, 0, "<StockItem>", STOCK_NEW),
            ("/Game/_Open...", "<control>O", self.open_dialog, 0, "<StockItem>", STOCK_OPEN),
            ("/Game/", None, None, 0, "<Separator>"),
            ("/Game/_Save", "<control>S", self.save_to_file, 0, "<StockItem>", STOCK_SAVE),
            ("/Game/Save _as...", "<control><shift>S", self.save_as_dialog, 0, "<StockItem>", STOCK_SAVE_AS),
            ("/Game/", None, None, 0, "<Separator>"),
            ("/Game/_Fullscreen", "F11", lambda widget, event: self.toggle_fullscreen(), 0, "<StockItem>", STOCK_FULLSCREEN),
            ("/Game/", None, None, 0, "<Separator>"),
            ("/Game/_Quit", "<control>Q", lambda widget, event: self.quit(), 0, "<StockItem>", STOCK_QUIT),
            ("/_Help", None, None, 0, "<Branch>"),
            ("/Help/_About", "F1", self.about, 0, "<StockItem>", STOCK_ABOUT)
        )
        accel_group = AccelGroup()
        item_factory = ItemFactory(MenuBar, "<main>", accel_group)
        item_factory.create_items(menu_items)
        window.add_accel_group(accel_group)
        menubar = item_factory.get_widget("<main>")
        item_factory.get_item("/Game/Convert mouse").set_tooltip_text("Convert mouse to swipe mode.")
        item_factory.get_item("/Game/New Grid").set_tooltip_text("Change the size of your grid.")
        item_factory.get_item("/Game/Open...").set_tooltip_text("Open a previously saved game.")
        item_factory.get_item("/Game/Save").set_sensitive(False)
        item_factory.get_item("/Game/Save").set_tooltip_text("Save this game.")
        item_factory.get_item("/Game/Save as...").set_tooltip_text("Save game with a different name.")
        item_factory.get_item("/Game/Fullscreen").set_tooltip_text("Toggle fullscreen view.")
        item_factory.get_item("/Help/About").set_tooltip_text("About py2048")
        self.item_factory = item_factory
        alignment = Alignment()
        alignment.add(menubar)
        self.alignment = alignment
        menubar.show()
        alignment.show()
        vbox.pack_start(alignment, False, False)
        vbox.pack_start(upper_hbox, False, False)
        vbox.pack_start(lower_hbox, False, False)

        self.fullscreen_button = Button("_Leave Fullscreen")
        self.fullscreen_button.connect("clicked", self.toggle_fullscreen)
        self.empty_label = Label()
        lower_hbox.pack_start(self.fullscreen_button, False, False)
        upper_hbox.pack_start(self.empty_label, False, False)
        table = Table()
        self.rows = []
        self.columns = []
        self.cells = []
        ev.add(table)
        ev.show()
        window.add(vbox)
        vbox.pack_end(ev)
        self.score = 0
        self.score_label = Label("Score: %i" % self.score)
        self.score_label.show()
        self.highscore_label = Label()
        self.highscore_label.show()
        upper_hbox.pack_start(self.score_label)
        lower_hbox.pack_start(self.highscore_label)
        self.table = table
        self.upper_hbox = upper_hbox
        self.lower_hbox = lower_hbox
        self.window = window
        self.eventbox = ev
        self.filter = FileFilter()
        self.filter.set_name("py2048 files")
        self.filter.add_pattern("*.2048")
        self.all_filter = FileFilter()
        self.all_filter.set_name("All files")
        self.all_filter.add_pattern("*")
        self.destroyed = False
        self.undo_button = Button("_Undo")
        self.undo_button.connect("clicked", self.undo)
        self.new_game_button = Button("_New game")
        self.new_game_button.connect("clicked", self.new_game)
        upper_hbox.pack_end(self.undo_button, False, False)
        self.undo_button.set_size_request(80, 30)
        lower_hbox.pack_end(self.new_game_button, False, False)
        self.new_game_button.set_size_request(80, 30)
        self.undo_button.show()
        self.new_game_button.show()
        vbox.show_all()
        self.fullscreen_button.hide()
        self.eventbox.modify_bg(STATE_NORMAL, gdk.Color("#3f3f3f"))

        self.saved_changes = []
        self.window.connect("key_press_event", self.onkey)
        self.window.add_events(gdk.POINTER_MOTION_MASK)
        self.window.connect("motion-notify-event", self._control_cursor)
        self.window.connect("button_press_event", self._control_cursor)
        self.window.connect("button_release_event", self.on_release)

        def got_data(widget, context, x, y, data, info, time, get_url):
            url = get_url(data.get_text())
            self.open_file(url['url'])
            context.finish(True, False, time)
        def get_url(url):
            url = url.splitlines()
            if len(url) > 1:
                return False
            url = url[0]
            url = replace(os.path.normpath(url.strip("file").strip(":")), "%20", " ")
            return {'url': url, 'isfile': os.path.isfile(url)}
        self.window.drag_dest_set(0, [], 0)
        self.window.connect(
            "drag_motion",
# call context.drag_status and return True.  The boolean equivalent of a
# list is its length.
            lambda w,c,x,y,t:[c.drag_status(gdk.ACTION_COPY, t)]
        )


        self.window.connect(
            "drag_drop",
# Call widget.drag_get_data and return True.
            lambda w,c,x,y,t:[w.drag_get_data(c, c.targets[-1], t)]
        )

        self.window.connect("drag_data_received", got_data, get_url)
        
        self.CLICK = 0
        self.DRAG = 1
        self.click_mode = self.CLICK
        self.pos = None

        self.changes = []

    def _control_cursor(self, widget, event):
        self.cursor_last_seen = time.time()
        x, y = self.window.window.get_pointer()[:2]
        size = self.table.get_allocation()
        width = size.width
        height = size.height
        y -= (self.window.get_size()[1] - height)
        if self.is_fullscreen and 0 <= y < 60:
            if self.upper_hbox.get_visible():
                self.upper_hbox.hide()
                self.lower_hbox.hide()
            else:
                self.table.window.set_cursor(None)
                self.window.dir = None
                self.upper_hbox.show_all()
                self.lower_hbox.show_all()
                return
        if self.over:
            self.table.window.set_cursor(None)
            return
        elif self.click_mode == self.CLICK:
            if y < 0:
                self.window.dir = None
                return
            half_width, half_height = width / 2.0, height / 2.0
            x_prop = (max(half_width, x) - min(half_width, x)) / width
            y_prop = (max(half_height, y) - min(half_height, y)) / height
            if x_prop > y_prop:
                if x > half_width:
                    self.table.window.set_cursor(gdk.Cursor(gdk.SB_RIGHT_ARROW))
                    self.window.dir = self.right
                else:
                    self.table.window.set_cursor(gdk.Cursor(gdk.SB_LEFT_ARROW))
                    self.window.dir = self.left
            else:
                if y > half_height:
                    self.table.window.set_cursor(gdk.Cursor(gdk.SB_DOWN_ARROW))
                    self.window.dir = self.down
                else:
                    self.table.window.set_cursor(gdk.Cursor(gdk.SB_UP_ARROW))
                    self.window.dir = self.up
        elif self.click_mode == self.DRAG and self.pos is None:
            self.table.window.set_cursor(None)

        if event.type == gdk.BUTTON_PRESS:
            if self.click_mode == self.CLICK and not self.window.dir is None:
                self.window.dir()
            elif self.click_mode == self.DRAG:
                self.pos = widget.get_pointer()
                self.table.window.set_cursor(gdk.Cursor(gdk.FLEUR))

    def on_release(self, widget, event):
        if self.click_mode != self.DRAG:
            return
        self.table.window.set_cursor(None)
        pos = widget.get_pointer()
        x_dif = max(pos[0], self.pos[0]) - min(pos[0], self.pos[0])
        y_dif = max(pos[1], self.pos[1]) - min(pos[1], self.pos[1])
        if x_dif > y_dif:
            (self.left, self.right)[pos[0] > self.pos[0]]()
        elif y_dif > x_dif:
            (self.up, self.down)[pos[1] > self.pos[1]]()
        self.pos = None
        self.cursor_last_seen = time.time()

    def switch_mouse_mode(self):
        if self.click_mode == self.CLICK:
            self.click_mode = self.DRAG
            self.table.window.set_cursor(None)
            self.item_factory.get_item("/Game/Convert mouse").set_tooltip_text("Convert mouse to click mode.")
        else:
            self.click_mode = self.CLICK
            self.item_factory.get_item("/Game/Convert mouse").set_tooltip_text("Convert mouse to swipe mode.")
        self._control_cursor(self.window, gdk.Event(gdk.MOTION_NOTIFY))

    def open_dialog(self, widget, event):
        file_chooser = FileChooserDialog(
            "Open...",
            None,
            FILE_CHOOSER_ACTION_OPEN,
            (STOCK_CANCEL, RESPONSE_CANCEL,
             STOCK_OPEN, RESPONSE_OK)
        )
        file_chooser.add_filter(self.all_filter)
        file_chooser.add_filter(self.filter)
        file_chooser.set_filter(self.filter)
        file_chooser.set_skip_taskbar_hint(True)
        file_chooser.set_icon(self.pixbuf)
        def func(widget, response):
            filename = file_chooser.get_filename()
            if response == RESPONSE_OK:
                self.item_factory.get_item("/Game/Save").set_sensitive(True)
                self.item_factory.get_item("/Game/Save").set_label("_Save to %r" % os.path.split(filename)[1])
                if not self.open_file(filename) is None:
                    file_chooser.destroy()
                    del self.file_chooser
            else:
                file_chooser.destroy()
                del self.file_chooser
        file_chooser.connect("response", func)
        self.file_chooser = file_chooser
        file_chooser.show()

    def save_as_dialog(self, widget=None, event=None):
        file_chooser = FileChooserDialog(
            "Save as...",
            self.window,
            FILE_CHOOSER_ACTION_SAVE,
            (STOCK_CANCEL, RESPONSE_CANCEL,
                STOCK_SAVE_AS, RESPONSE_OK)
        )
        file_chooser.set_current_name("saved-game.2048")
        file_chooser.set_current_folder(".")
        file_chooser.add_filter(self.all_filter)
        file_chooser.add_filter(self.filter)
        file_chooser.set_filter(self.filter)
        file_chooser.set_skip_taskbar_hint(True)
        file_chooser.set_do_overwrite_confirmation(True)
        self.file_chooser = file_chooser
        def func(widget, response):
            filename = file_chooser.get_filename()
            if response == RESPONSE_OK:
                if on_overwrite(file_chooser) == FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN:
                    return
                self.item_factory.get_item("/Game/Save").set_sensitive(True)
                self.item_factory.get_item("/Game/Save").set_label("_Save to %r" % os.path.split(filename)[1])
                if not self.save_to_file(filename) is None:
                    file_chooser.destroy()
                    del self.file_chooser
            else:
                file_chooser.destroy()
                del self.file_chooser
        def on_overwrite(widget):
            filename = widget.get_filename()
            filter = file_chooser.get_filter()
            if not os.path.splitext(filename)[1] == ".2048":
                if filter == self.filter:
                    error_dialog = MessageDialog(file_chooser, type=MESSAGE_ERROR)
                    error_dialog.set_markup("<b>Wrong file extension.</b>")
                    error_dialog.format_secondary_markup("Please change the file extension to .2048 or select 'all files' in the file extension selector.")
                    error_dialog.add_button("_OK", 0).connect("clicked", lambda *args: error_dialog.destroy())
                    error_dialog.set_modal(True)
                    error_dialog.show()
                else:
                    return FILE_CHOOSER_CONFIRMATION_CONFIRM
            elif os.path.splitext(filename)[1] == ".2048":
                return FILE_CHOOSER_CONFIRMATION_CONFIRM
            return FILE_CHOOSER_CONFIRMATION_SELECT_AGAIN

        file_chooser.connect("confirm-overwrite", on_overwrite)
        file_chooser.connect("response", func)
        file_chooser.show()

    def save_to_file(self, filename=None, *args):
        if filename is None or args:
            try:
                filename = self.filename
            except AttributeError:
                return
        try:
            file = open(filename, 'w+')
        except IOError:
            if 'file_chooser' in dir(self):
                parent = self.file_chooser
            else:
                parent = self.window
            error_dialog = MessageDialog(parent, type=MESSAGE_ERROR)
            error_dialog.set_markup("Permission denied: %r" % filename)
            error_dialog.show()
            return
        self.filename = filename
        pickler = pickle.Pickler(file)
        rows = self.rows
        labels = []
        evs = []
        for row in rows:
            for tile in row:
                evs.append(tile.ev)
                labels.append(tile.label)
                del tile.ev
                del tile.label
        pickler.dump(rows)
        pickler.dump(self.score)
        pickler.dump(self.changes)
        pickler.dump(self.changes_to_score)
        file.seek(0)
        lines = file.readlines()
        file.close()
        file = open(filename, "w")
        lines.insert(0, "2048 saved game\n")
        file.write("".join(lines))
        file.close()
        for row in rows:
            for tile in row:
                tile.ev = evs[0]
                tile.label = labels[0]
                evs.pop(0)
                labels.pop(0)
        self.saved_changes = self.changes[:]
        self.window.set_title("2048-" + os.path.split(file.name)[-1])
        return filename

    def open_file(self, filename):
        try:
            file = open(filename, 'r')
            original_lines = file.readlines()
            file.close()
            file = open(filename, 'w+')
        except IOError:
            if 'file_chooser' in dir(self):
                parent = self.file_chooser
            else:
                parent = self.window
            error_dialog = MessageDialog(parent, type=MESSAGE_ERROR)
            error_dialog.set_markup("Permission denied: %r" % filename)
            error_dialog.show()
            return
        if len(original_lines) > 0:
            if original_lines[0] == "2048 saved game\n":
                file.write("".join(original_lines[1:]))
        self.filename = filename
        file.seek(0)
        try:
            unpickler = pickle.Unpickler(file)
            rows = unpickler.load()
            score = unpickler.load()
            changes = unpickler.load()
            changes_to_score = unpickler.load()
            prev_num_rows = len(self.rows)
            prev_num_cols = len(self.columns)
            self.rows = rows
            self.columns = []
            num_rows = len(self.rows)
            num_cols = len(self.rows[0])
            if num_rows != prev_num_rows or num_cols != prev_num_cols:
                self.table.destroy()
                del self.table
                self.table = Table(num_rows, num_cols, True)
                self.eventbox.add(self.table)
                self.table.show()
            for column in range(num_cols):
                self.columns.append([])
                for row in range(num_rows):
                    self.columns[-1].append(None)
            self.cells = []
            for x in range(len(self.rows)):
                for y in range(len(self.rows[0])):
                    cell = (rows[x])[y]
                    (self.columns[y])[x] = cell
                    self.cells.append(cell)
            col_pos = 0
            for column in self.columns:
                row_pos = 0
                for tile in column:
                    tile.ev = EventBox()
                    tile.ev.show()
                    tile.label = Label()
                    tile.label.show()
                    tile.ev.add(tile.label)
                    self.table.attach(tile.ev, col_pos, col_pos+1, row_pos, row_pos+1)
                    row_pos += 1
                col_pos += 1

            self.table.set_col_spacings(5)
            self.table.set_row_spacings(5)

            self.score = score
            self.update_score()
            self.changes_to_score = changes_to_score
            num_rows = len(self.rows)
            self.window.set_title("2048-" + file.name.split("/")[-1])
            self.item_factory.get_item("/Game/Save").set_sensitive(True)
            self.item_factory.get_item("/Game/Save").set_label("_Save to %r" % os.path.split(file.name)[1])
            self.update_tiles()
            self.changes = changes
            self.saved_changes = self.changes[:]
        except BaseException as e:
            if 'file_chooser' in dir(self):
                parent = self.file_chooser
            else:
                parent = None
            error_dialog = MessageDialog(parent, type=MESSAGE_ERROR)
            error_dialog.set_markup("<b>Could not read from file.</b>")
            def func(error_dialog, response, dum, info):
                if response == 1:
                    error_dialog.destroy()
                    return
                if dum.value == "_More":
                    string = "\n".join(format_exception(*info))
                    dum.value = "_Less"
                    but = error_dialog.children()[0].children()[1].children()[1]
                    but.set_label("_Less")
                else:
                    string = "<b>Could not read from file.</b>"
                    dum.value = "_More"
                    but = error_dialog.children()[0].children()[1].children()[1]
                    but.set_label("_More")
                error_dialog.set_markup(string)
            dum = dummy()
            dum.value = "_More"
            error_dialog.add_button("_More", 0)
            error_dialog.add_button("_OK", 1)
            error_dialog.connect("response", func, dum, sys.exc_info())
            error_dialog.show()
            return
        finally:
            file.close()
            file = open(filename, 'w')
            file.write("".join(original_lines))
            file.close()
        return filename

    def update_score(self):
        self.score_label.set_text("Score: %i" % self.score)
        if self.score > high_score.get((len(self.rows), len(self.columns)), 0):
            if not self.beat_highscore:
                def on_response(self, response, widget):
                    widget.destroy()
                self.update_highscore()
                win = MessageDialog(self.window)
                win.add_button(STOCK_CLOSE, 0)
                win.set_markup("You beat the highscore!")
                win.connect("response", lambda widget, response: widget.destroy())
                win.show()
                self.beat_highscore = True
            self.update_highscore()

    def add_to_score(self, num):
        self.score += num
        self.update_score()

    def about(self, *args):
        def onlink(widget, website, data):
            from webbrowser import open_new_tab
            open_new_tab(website)

        about = AboutDialog()
        about.set_skip_taskbar_hint(True)
        about.set_program_name("py2048")
        about.set_version("0.1")
        about.set_website("http://brominator.org")
        about.set_authors(("Ralph Embree",))
        about.set_logo(self.pixbuf)
        about.set_comments("2048 was originally written as a web application, but since then many different versions have been made.  The author knows of no other linux versions of the game, however.  The object of the game is to create a tile containing the number 2048 by making the other tiles combine.  Only tiles of the same value can combine.  This version has features the original does not have: undoing, saving games, changing the grid size, and more.")
        about.set_copyright("Copyright \xc2\xa9 2014 Ralph Embree")
        about.set_license(
        """py2048 is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

py2048 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with py2048.  If not, see http://www.gnu.org/licenses""")
        about.run()
        about.destroy()

    def new_game(self, *args, **kwargs):
        self.changes_to_score = []
        title = self.window.get_title()
        try:
            self.over_win.destroy()
            del self.over_win
        except AttributeError:
            pass
        if "num_rows" in kwargs and isinstance(kwargs['num_rows'], int):
            num_rows = kwargs['num_rows']
        else:
            num_rows = len(self.rows)
        if "num_cols" in kwargs and isinstance(kwargs['num_cols'], int):
            num_cols = kwargs['num_cols']
        else:
            num_cols = len(self.columns)
        if num_rows == len(self.rows) and num_cols == len(self.columns):
            for cell in self.cells:
                cell.value = None
        else:
            self.table.destroy()
            del self.table
            self.table = Table(num_rows, num_cols, True)
            self.eventbox.add(self.table)
            self.table.show()
            cols = []
            for column in range(num_cols):
                cols.append([])
                for row in range(num_rows):
                    cols[-1].append(dummy())

            self.columns = cols
            rows = []
            for row in range(num_rows):
                rows.append([])
                for column in range(num_cols):
                    rows[-1].append(None)

            self.rows = rows
            self.cells = []
            for x in range(len(cols)):
                for y in range(len(cols[0])):
                    cell = (cols[x])[y]
                    (self.rows[y])[x] = cell
                    self.cells.append(cell)
            col_pos = 0
            for column in self.columns:
                row_pos = 0
                for tile in column:
                    tile.pos = [col_pos, row_pos]
                    tile.ev = EventBox()
                    tile.ev.show()
                    tile.label = Label()
                    tile.label.show()
                    tile.color = None
                    tile.ev.add(tile.label)
                    tile.value = None
                    self.table.attach(tile.ev, col_pos, col_pos+1, row_pos, row_pos+1)
                    row_pos += 1
                col_pos += 1
            self.table.set_col_spacings(5)
            self.table.set_row_spacings(5)
        self.highscore_label.set_text("Best: %i" % high_score.get((num_rows, num_cols), 0))
        if self.score > high_score.get((len(self.rows), len(self.columns)), 0):
            self.update_highscore()
        self.score = 0
        self.update_score()
        self.over = False
        self.new_tile()
        self.new_tile()
        self.table.set_size_request(17, 12 * len(str(2 ** (len(self.cells) + 1))))
        self.window.show()
        self.update_tiles()
        self.changes = []
        self.undo_button.set_sensitive(False)
        self.beat_highscore = False
        self.update_fonts()

    def onkey(self, widget, event):
        value = event.keyval
        if value == keysyms.Left:
            self.left()
        elif value == keysyms.Right:
            self.right()
        elif value == keysyms.Up:
            self.up()
        elif value == keysyms.Down:
            self.down()
        # Ctrl-z
        elif value == keysyms.z and event.state == gdk.CONTROL_MASK | gdk.MOD2_MASK:
            self.undo()
        elif value == keysyms.F11 and self.is_fullscreen:
            self.toggle_fullscreen()
        elif value == keysyms.Escape and self.is_fullscreen:
            self.toggle_fullscreen()
        elif value == keysyms.m and event.state == gdk.CONTROL_MASK | gdk.MOD2_MASK and self.is_fullscreen:
            self.switch_mouse_mode()

    def random_available_cell(self):
        cells = []
        for tile in self.cells:
            if tile.value is None:
                cells.append(tile)
        if len(cells) == 0:
            return []
        return choice(cells)

    def game_over(self):
        self.over = True
        self.table.window.set_cursor(None)
        if self.score > high_score.get((len(self.rows), len(self.columns)), 0):
            self.update_highscore()
        def on_response(widget, response):
            widget.destroy()
            if response == NEW:
                self.new_game()
            elif response == EXIT:
                self.on_destroy(None, None)

        NEW = 0
        EXIT = 1
        self.over_win = MessageDialog(
            self.window,
        )
        self.over_win.add_buttons("_New game", NEW, STOCK_QUIT, EXIT)
        self.over_win.set_markup("Game is over.")
        self.over_win.connect("response", on_response)
        self.over_win.run()

    def new_tile(self):
        tile = self.random_available_cell()
        if tile is None:
            self.game_over()
            return
        value = random()
        if value > 0.9:
            value = 4
        else:
            value = 2
        tile.value = value
        return tile

    def update_tiles(self):
        changes = []
        self.undo_button.set_sensitive(True)
        self.over = False
        for tile in self.cells:
            value = tile.value
            if value is None:
                try:
                    prev_val = int(tile.label.get_text())
                except:
                    prev_val = None
                if value != prev_val:
                    changes.append((tile, prev_val))
                tile.label.set_text("")
                value = 0
                new_val = 0
            else:
                new_val = int(log(value, 2))
                try:
                    prev_val = int(tile.label.get_text())
                except:
                    prev_val = None
                if value != prev_val:
                    changes.append((tile, prev_val))
            num = int((768.0 * new_val) / (len(self.cells) - 1))
            if num > 384:
                fg_color = gdk.Color("black")
            else:
                fg_color = gdk.Color("white")
            red, green, blue = ("00", "00", "00")
            if num >= 256:
                green = "ff"
                num -= 256
                if num >= 256:
                    red = "ff"
                    num -= 256
                    if num >= 256:
                        blue = "ff"
                    else:
                        blue = hex(num)[2:]
                        num_0 = 2 - len(blue)
                        blue = ("0" * num_0) + blue
                else:
                    red = hex(num)[2:]
                    num_0 = 2 - len(red)
                    red = ("0" * num_0) + red
            else:
                green = hex(num)[2:]
                num_0 = 2 - len(green)
                green = ("0" * num_0) + green
            num = "%s%s%s" % (red, green, blue)
            z_num = 6 - len(str(num))
            color = "#" + ("0" * z_num) + num
            tile.color = color
            tile.ev.modify_bg(STATE_NORMAL, gdk.Color(color))
            tile.label.modify_fg(STATE_NORMAL, fg_color)
        self.changes.append(changes)
        self.update_fonts()
        self.check_game_over()

    def update_fonts(self, *dummies):
        for tile in self.cells:
            value = tile.value
            if value is None:
                continue
            label = tile.label
            size = self.table.get_allocation()
            width = size.width / len(self.columns)
            height = size.height / len(self.rows)
            height_size = 588 * height
            num_chars = len(str(value))
            width_size = (1200 / num_chars) * width
            tile.label.set_markup('<span size="%i">%i</span>' % (min(height_size, width_size), value))

    def left(self, *args):
        if self.over:
            return
        if not self.window.get_title().startswith("*"):
            self.window.set_title("*" + self.window.get_title())
        prev_score = self.score
        changed = False
        for row in self.rows:
            for cell in row[:-1]:
                value = cell.value
                if value is None:
                    continue
                place = cell.pos[0]
                gotten = False
                for adj in row[place + 1:]:
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                if adj.value == value:
                    changed = True
                    self.add_to_score(cell.value * 2)
                    cell.value *= 2
                    adj.value = None
        for row in self.rows:
            for cell in row[:-1]:
                value = cell.value
                if not value is None:
                    continue
                place = cell.pos[0]
                gotten = False
                for adj in row[place + 1:]:
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                changed = True
                cell.value = adj.value
                adj.value = None
        if changed:
            self.new_tile()
            self.changes_to_score.append(prev_score)
            self.update_tiles()
            self.check_game_over()
        return

    def right(self, *args):
        if self.over:
            return
        if not self.window.get_title().startswith("*"):
            self.window.set_title("*" + self.window.get_title())
        prev_score = self.score
        changed = False
        for row in self.rows:
            for cell in list(reversed(row[1:])):
                value = cell.value
                if value is None:
                    continue
                place = cell.pos[0]
                gotten = False
                for adj in list(reversed(row[:place])):
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                if adj.value == value:
                    changed = True
                    self.add_to_score(cell.value * 2)
                    cell.value *= 2
                    adj.value = None
        for row in self.rows:
            for cell in list(reversed(row[1:])):
                value = cell.value
                if not value is None:
                    continue
                place = cell.pos[0]
                gotten = False
                for adj in list(reversed(row[:place])):
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                changed = True
                cell.value = adj.value
                adj.value = None
        if changed:
            self.new_tile()
            self.update_tiles()
            self.changes_to_score.append(prev_score)
            self.check_game_over()

    def up(self, *args):
        if self.over:
            return
        if not self.window.get_title().startswith("*"):
            self.window.set_title("*" + self.window.get_title())
        prev_score = self.score
        changed = False
        num = 0
        for column in self.columns:
            num += 1
            for cell in column[:-1]:
                value = cell.value
                if value is None:
                    continue
                place = cell.pos[1]
                gotten = False
                for adj in column[place + 1:]:
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                if adj.value == value:
                    changed = True
                    self.add_to_score(cell.value * 2)
                    cell.value *= 2
                    adj.value = None
        for column in self.columns:
            for cell in column[:-1]:
                value = cell.value
                if not value is None:
                    continue
                place = cell.pos[1]
                gotten = False
                for adj in column[place + 1:]:
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                changed = True
                cell.value = adj.value
                adj.value = None
        if changed:
            self.new_tile()
            self.update_tiles()
            self.changes_to_score.append(prev_score)
            self.check_game_over()

    def down(self, *args):
        if self.over:
            return
        if not self.window.get_title().startswith("*"):
            self.window.set_title("*" + self.window.get_title())
        prev_score = self.score
        changed = False
        num = 0
        for column in self.columns:
            num += 1
            for cell in list(reversed(column[1:])):
                value = cell.value
                if value is None:
                    continue
                place = cell.pos[1]
                gotten = False
                for adj in list(reversed(column[:place])):
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                if adj.value == value:
                    changed = True
                    self.add_to_score(cell.value * 2)
                    cell.value *= 2
                    adj.value = None
        for column in self.columns:
            for cell in list(reversed(column[1:])):
                value = cell.value
                if not value is None:
                    continue
                place = cell.pos[1]
                gotten = False
                for adj in list(reversed(column[:place])):
                    if not adj.value is None:
                        gotten = True
                        break
                if not gotten:
                    continue
                changed = True
                cell.value = adj.value
                adj.value = None
        if changed:
            self.new_tile()
            self.update_tiles()
            self.changes_to_score.append(prev_score)
            self.check_game_over()

    def undo(self, *args):
        try:
            self.over_win.destroy()
            del self.over_win
        except AttributeError:
            pass
        if len(self.changes) < 1 or len(self.changes_to_score) < 1:
            return
        self.score = self.changes_to_score[-1]
        self.update_score()
        self.changes_to_score.pop()
        changes = list(reversed(self.changes[-1]))
        prev_changes = self.changes[:]
        for tile, value in changes:
            tile.value = value
        prev_changes.pop()
        self.update_tiles()
        self.changes = prev_changes
        if len(self.changes) == 0:
            self.undo_button.set_sensitive(False)
        title = self.window.get_title()
        if self.changes == self.saved_changes and title.startswith("*"):
            self.window.set_title(title[1:])
        elif self.changes != self.saved_changes and not title.startswith("*"):
            self.window.set_title("*" + get_title)

    def on_destroy(self, widget, event):
        if self.changes == self.saved_changes or self.over:
            self.quit()
        else:
            def func(widget, response):
                if response == CLOSE:
                    self.quit()
                elif response == SAVE:
                    if not self.save_to_file(self.filename) is None:
                        self.quit()
                else:
                    self.delete_id = self.window.connect("delete-event", self.on_destroy)
                    widget.destroy()
                    return True

            self.window.disconnect(self.delete_id)
            me = MessageDialog(self.window, DIALOG_DESTROY_WITH_PARENT)
            CLOSE = 0
            SAVE = 1
            CANCEL = 2
            me.add_buttons(
                "Close _Without Saving", CLOSE,
                STOCK_CANCEL, CANCEL,
                STOCK_SAVE, SAVE
            )
            if self.saved_changes == []:
                me.set_markup("<b>Would you like to save this game to a file?</b>")
            else:
                me.set_markup("<b>Save changes to %r before closing?</b>" % self.filename.split("/")[-1])
            me.format_secondary_text("Your changes will be lost if you don't save them.")
            me.connect("response", func)
            me.show()
            return True

    def quit(self, arg=None):
        self.destroyed = True
        if self.window.get_property("visible"):
            self.window.destroy()
        if self.score > high_score.get((len(self.rows), len(self.columns)), 0):
            self.update_highscore()
        try:
            mainquit()
        except RuntimeError:
            pass

    def check_game_over(self):
        for tile in self.cells:
            value = tile.value
            if value is None:
                return False
            col_num = tile.pos[0]
            row_num = tile.pos[1]
            if row_num > 0:
                adj = (self.rows[row_num - 1])[col_num]
                if adj.value in (None, tile.value):
                    return False
            if row_num < len(self.rows) - 1:
                adj = (self.rows[row_num + 1])[col_num]
                if adj.value in (None, tile.value):
                    return False
            if col_num > 0:
                adj = (self.columns[col_num - 1])[row_num]
                if adj.value in (None, tile.value):
                    return False
            if col_num < len(self.columns) - 1:
                adj = (self.columns[col_num + 1])[row_num]
                if adj.value in (None, tile.value):
                    return False
        self.game_over()
        return True

    def update_highscore(self):
        global high_score
        high_score[len(self.rows), len(self.columns)] = self.score
        f = open(__file__)
        contents = f.readlines()
        f.close()
        index = contents.index("#Do not change this line or the one after it.\n")
        contents[index + 1] = "high_score = %r\n" % high_score
        f = open(__file__, "w")
        f.write("".join(contents))
        f.close()
        self.highscore_label.set_text("Best: %i" % self.score)

    def new_grid(self, *args):
        def onclick(widget):
            window.destroy()
            if widget == canc_but:
                return
            self.new_game(
                num_rows=rows.get_value_as_int(),
                num_cols=cols.get_value_as_int()
            )

        window = Window()
        table = Table(4, 2)
        table.show()
        window.add(table)
        window.set_transient_for(self.window)
        window.set_skip_taskbar_hint(True)
        window.set_modal(True)
        label = Label('How many rows and how many columns would you like in your new grid?\nNote: once you hit "Ok", You will not be able to undo.')
        label.set_line_wrap(True)
        label.show()
        table.attach(label, 0, 2, 0, 1)
        row_label = Label()
        row_label.set_text_with_mnemonic("_Rows:")
        row_label.show()
        table.attach(row_label, 0, 1, 1, 2)
        rows = SpinButton(Adjustment(len(self.rows), 0, 12, 1, 2), digits=0)
        row_label.set_mnemonic_widget(rows)
        rows.set_numeric(True)
        rows.show()
        table.attach(rows, 1, 2, 1, 2)
        col_label = Label()
        col_label.set_text_with_mnemonic("Co_lumns:")
        col_label.show()
        table.attach(col_label, 0, 1, 2, 3)
        cols = SpinButton(
            Adjustment(len(self.columns), 0, 12, 1, 2),
            digits=0
        )
        col_label.set_mnemonic_widget(cols)
        cols.set_numeric(True)
        cols.show()
        table.attach(cols, 1, 2, 2, 3)
        canc_but = Button("_Cancel")
        canc_but.connect("clicked", onclick)
        canc_but.show()
        table.attach(canc_but, 0, 1, 3, 4, FILL)
        okay_but = Button("_Ok")
        okay_but.connect("clicked", onclick)
        okay_but.show()
        table.attach(okay_but, 1, 2, 3, 4, FILL)
        window.set_title("Size")
        window.set_icon(self.pixbuf)
        window.set_position(WIN_POS_CENTER_ON_PARENT)
        window.show()

    def on_fullscreen_event(self, widget, event):
        if event.changed_mask & gdk.WINDOW_STATE_FULLSCREEN:
            self.is_fullscreen = event.new_window_state & gdk.WINDOW_STATE_FULLSCREEN
            if self.is_fullscreen:
                self.alignment.hide()
                self.upper_hbox.hide()
                self.lower_hbox.hide()
                self.empty_label.set_size_request(107, 28)
                event = gdk.Event(gdk.MOTION_NOTIFY)
                event.window = self.window.window
                event.send_event = True
                self.window.emit("motion-notify-event", event)
            else:
                self.empty_label.set_size_request(-1, -1)
                self.alignment.show()
                self.upper_hbox.show()
                self.lower_hbox.show()
                self.fullscreen_button.hide()

    def toggle_fullscreen(self, *dummies):
        self.check_fonts = True
        if self.is_fullscreen:
            self.window.unfullscreen()
        else:
            self.window.fullscreen()
            self.last_cursor_seen = time.time()
            timeout_add(100, self.update_cursor)

    def update_cursor(self):
        if self.check_fonts:
            self.update_fonts()
            self.check_fonts = False
        if not self.is_fullscreen:
            return False
        if self.over:
            self.table.window.set_cursor(None)
            return True
        if time.time() - self.cursor_last_seen >= 1 and \
                    (self.table.window.get_cursor() is None or \
                    not self.table.window.get_cursor().type is gdk.FLEUR):
            self.table.window.set_cursor(gdk.Cursor(gdk.BLANK_CURSOR))
        return True


if __name__ == '__main__':
    game = Game()
    # Here is where the default grid size can be changed permanently.
    # Nothing else is needed.
    game.new_game(num_rows=4, num_cols=4)
    if len(argv) > 1:
        game.open_file(argv[1])
    mainloop()

