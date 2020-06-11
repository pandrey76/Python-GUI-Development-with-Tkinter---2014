#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     07.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()


    #   Mouse Button Number

#   Левая кнопка                         - 1
#   Средняя кнопка (нажатие и скролинг)  - 2
#   Правая кнопка                        - 3

                #   Mouse Events: Click-Related
#    ________________________________________________________________________
#   |  Event Format                |   Event Describtion                     |
#   |______________________________|_________________________________________|
#   | <Button>, <ButtonPress>      |   Any button was pressed.               |
#   |______________________________|_________________________________________|
#   | <Button-1>, <ButtonPress-1,  |   Button 1 was pressed.                 |
#   | <1>                          |                                         |
#   |______________________________|_________________________________________|
#   | <ButtonRelease-1>            |   Button 1 was released.                |
#   |______________________________|_________________________________________|
#   | <Double-Button-1> or         |  Button 1 was double- or triple-ckicked.|
#   | <Triple-Button-1>            |                                         |
#   |_____________________________ |_________________________________________|


                #   Mouse Events: Movement-Related
#    ________________________________________________________________________
#   |  Event Format                |   Event Describtion                     |
#   |______________________________|_________________________________________|
#   | <Enter>                      |   Mouse entered widget area.            |
#   |______________________________|_________________________________________|
#   | <Leave>                      |   Mouse left widget area.               |
#   |______________________________|_________________________________________|
#   | <Motion>                     |   Mouse was moved.                      |
#   |______________________________|_________________________________________|
#   | <B1-Motion>                  |   Mouse was moved with Button 1         |
#   |                              |   held down                             |
#   |_____________________________ |_________________________________________|

   #Блок №1 /////////////////////////////////////////////////////////////////////
def mouse_press(event):
    print('type: {}'.format(event.type))        # 4 (Собыиие ButtonPress)
    print('widget: {}'.format(event.widget))    # .18085872 (canvas)
    print('num: {}'.format(event.num))          # 1 (Левая кнопка)
    print('X: {}'.format(event.x))              # 413
    print('Y: {}'.format(event.y))              # 363
    #Координаты отностительно основного экрана.
    print('X_root: {}'.format(event.x_root))    # 439
    print('Y_root: {}'.format(event.y_root))    # 422

#если мы расширим окно, то при нажатии на кнопки мыши за пределами "canvas" ничего не происходит
#Событие срабатывает, только когда мы кликаем в области элемента "canvas"
canvas.bind( '<ButtonPress>', mouse_press)

    #//////////////////////////////////////////////////////////////////////////////

   #Блок №2 /////////////////////////////////////////////////////////////////////
   #Данный блок не работает (у автора работает у меня нет )
   #NameError: name 'prev' is not defined
def draw (event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5 )
    prev = event

canvas.bind("<B1-Motion>", draw )

    #//////////////////////////////////////////////////////////////////////////////



root.mainloop()

class DrawLine:

    def __init__(self):
        self._root = Tk()
        self._canvas = Canvas(self._root, width = 640, height = 480, background = 'white')
        self._prev = None


    def draw (self, event):
        """
            При одновремменом нажатии на левую кнопку мыши и движении мыши
            вызывается данный метод.
        """
        if self._prev == None:
            self._prev = event
        self._canvas.create_line(self._prev.x, self._prev.y, event.x, event.y, width = 5 )
        self._prev = event

    def main_window(self):
        self._canvas.pack()
        self._canvas.bind("<B1-Motion>", self.draw )
        self._root.mainloop()


if __name__ == '__main__':
    draw_line = DrawLine()
    draw_line.main_window()