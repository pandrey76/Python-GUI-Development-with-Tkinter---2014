#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     13.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self, master):
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid( row = 0, column = 0, columnspan = 2)#последний
        #параметр говорит о том, что элемент может располагатся сразу
        #в первом и втором столбце.

        ttk.Button( master, text = "Texas",
                    command = self.texas_hello).grid ( row = 1, column = 0)

        ttk.Button( master, text = "Hawaii",
                    command = self.hawaii_hello).grid ( row = 1, column = 1)

    def texas_hello(self):
        self.label.config( text = "Howdy, Tkinter!" )

    def hawaii_hello(self):
        self.label.config( text = "Aloha, Tkinter!" )

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == '__main__':    main()
