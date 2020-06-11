#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     09.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.logo = PhotoImage(file = 'e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\tour_logo.gif')

        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
        #   Один из способов записи нескольких строк (multyline).
        ttk.Label(self.frame_header,
                   wraplength = 300, #t
                    text = ("We're glade you chose Explore California for you recent adventure.   "
                            "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(padx = 5)

        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_name.grid(row = 1, column = 0)

        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.entry_email.grid(row = 1, column = 1)

        self.text_comments = Text(self.frame_content, width = 50, height = 10)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2)

        ttk.Button(self.frame_content, text = 'Submit').grid(row = 4, column = 0)
        ttk.Button(self.frame_content, text = 'Clear').grid(row = 4, column = 1)


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == '__main__':
    main()