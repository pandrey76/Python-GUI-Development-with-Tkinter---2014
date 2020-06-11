#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     26.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from  tkinter import ttk

def main():
    root = Tk()
    panedwindow = ttk.Panedwindow(root,orient = HORIZONTAL)

    panedwindow.pack(fill = BOTH, expand = True)    #???

    frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
    frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)

    #Добавляем элемент на panedwindow
    panedwindow.add(frame1, weight = 1)#параметр 'weight' определяет
    #во сколько раз элемент относительно других будет менять свой размер при
    #разворачивании и сворачивании окна.
    panedwindow.add(frame2, weight = 4)
    frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)

    panedwindow.insert(1, frame3)#вставляем элемент между 1 и 2 элементами Frame
    #panedwindow.insert(1, frame3, weight = 2)

    panedwindow.forget(1)#данный метод скрывает 2 элемент на panedwindow, данный
                         #элемент не удаляется он просто скрыт.
    root.mainloop()

if __name__ == '__main__':
    main()
