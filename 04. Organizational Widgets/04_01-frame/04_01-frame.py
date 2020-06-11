#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     25.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Элемент Frame представляет из себя прямоугольник, в котором можно
#организовывать другие элементы,  который содержит параметры, указатель
#на владельца  (Parent), элемент в котором располагается сам элемент Frame
#и свой собственный Geomrtry Manager.
#Посмотреть пример 00:26

from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    frame = ttk.Frame(root)
    frame.pack()
    frame.config(height = 100, width = 200)#В пикселях
    #relief = [FLAT(No Border), RAISED, SUNKEN, SOLID, RIDGE, GROOVE]
    frame.config(relief = RIDGE)

    #Для элемента Frame мы используем Grid Geometry Manager.
    ttk.Button(frame, text = 'Click Me').grid()
    #Данное свойство определяет размер элемента Frame в зависимости от своих дочерних элементов

    frame.config(padding = (30, #мимнимальное расстояние от левой стороны
                                #элемента Frame до ближайшего элемента,
                                #который является дочерним элементу Frame

                            15  #мимнимальное расстояние от верхней стороны
                                #элемента Frame до ближайшего элемента,
                                #который является дочерним элементу Frame
                            ))

    #Для элемента главного окна (root) мы используем Pack Geometry Manager.

    #У данного элемента есть дополнительное свойство 'text', данный заголовок
    #отображается на фоне верхней стороны элемента Frame.
    ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()
    root.mainloop()

class ExtButton(ttk.Button):
    def __init__(self, master=None, **kw):
        self._current = 0
        Widget.__init__(self, master, "ttk::button", kw)

    #current_time  = property( lambda self : self._current  )
    """
        Property return object type "_current"
    """
    @property
    def current_num(self):
        """
            Property return object type "_current"
        """
        return self._current

    @current_num.setter
    def current_num(self, cur):
        """
            Property setting string object type "_current"
        """
        if type(cur) is int:
            self._current = cur
        else:
            raise TypeError()

class ConstructFrameElement:

    def __init__(self):
        self._root = Tk()
        self._frame = ttk.Frame(self._root)

        self._lable_frame = ttk.LabelFrame(self._root, height = 100, width = 200,
                                                            text = 'My Frame')
        self._lable_frame.config(padding = (30, 15))
        self._change_board_button = ExtButton(self._lable_frame,
                                                text = 'Change board')

    def main(self):
        self._frame.pack()
        self._frame.config(relief = RIDGE, height = 100, width = 200)

        self._lable_frame.pack()
        self._change_board_button.config ( command = self.ChangeFrameBoard )
        self._change_board_button.grid()
        self._root.mainloop()

    def ChangeFrameBoard(self):
         Relief = [FLAT, RAISED, SUNKEN, SOLID, RIDGE, GROOVE]
         self._change_board_button.current_num += 1
         self._change_board_button.current_num %= len(Relief)

         print (Relief[self._change_board_button.current_num])

         #Почемуто для ttk.LabelFrame это не работает
         self._lable_frame.config(relief = Relief[self._change_board_button.current_num])

         self._frame.config(relief = Relief[self._change_board_button.current_num])


if __name__ == '__main__':
    construct_elem = ConstructFrameElement()
    construct_elem.main()
    #main()
