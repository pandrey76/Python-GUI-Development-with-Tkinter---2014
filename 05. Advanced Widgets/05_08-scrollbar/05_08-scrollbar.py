#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     31.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    text = Text(root, width = 20, height = 3, wrap = 'word')
    text.grid(row = 0, column = 0)
    print(text.config())
    #command - определяет какую команду вызывать, когда пользователь скроллит
    scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)

    scrollbar.grid(row = 0,column = 1, sticky = "ns")#'ns' - North/South положение кнопок скролбра сверху и снизу
    #После этого скролбар будет активным всегда, даже когда ничего не будет введено элемент Text и длина полосы прокрутки будет во всю длину Scrollbarа.

    #далее мы оперделим обратное взаимодействие между элементом Text и элементом Scrollbar
    text.config(yscrollcommand = scrollbar.set)
    #После этого Scrollbar будет неактивный пока мы не заполним всё поле элемента Text и с увеличением текста длина полрсы прокрутки будет уменьшаться при
    #захвате мышкой полосы прокрутки можно будет прокручивать Text вверх и вниз.

#Элементы, которые поддерживают скроллинг
#       Scroll-Enabled Widgets

#    X-Scroll                               Y-Scroll
#
#   * Text                                  * Text
#   *Canvas                                 *Canvas
#   *Treeview                               *Treeview

#   *Entry
#   *Spinbox
#   *Combobox

    root.mainloop()

main()

root = Tk()
canvas = Canvas(root, scrollregion = (0, 0, 640, 480), bg = 'white')
xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = canvas.xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = canvas.yview)
canvas.config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

canvas.grid(row = 1, column = 0)
xscroll.grid(row = 2, column = 0, sticky = 'ew')
yscroll.grid(row = 1, column = 1, sticky = 'ns')

def canvas_click(event):
    #так как метод не знает, что мы скролим по y или x, то круги создаются только в рамка созданного региона Canvas,
    #т.е. если кликаем вне этого региона, то круги создаются в крайних точках региона Canvas не там где мы кликаем.
    x = event.x
    y = event.y

    #Для этого мы должны передать в метод правильную позицию в canvas
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    canvas.create_oval((x-5, y-5, x+5, y+5), fill = 'green')

canvas.bind('<1>', canvas_click)

root.mainloop()

#if __name__ == '__main__':
#    pass
#    main()

