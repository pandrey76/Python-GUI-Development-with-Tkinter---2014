#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     01.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

#   Pack Geometry Manager

#   * Pros
#       Simplest geometry manager
#       Use when a widget is expanded to fill its entire parent
#       Use to stack multiple widgets vertically or horizontally

#   * Cons
#       Limited capability for complex layouts

# Pack Geometry manager

#   *Pros
#       Simplest geometry manager
#       Use when a widget is expanded to fill its entire parent
#       Use to stack multiple widgets vertically or horizontally
#   *Cons
#       Limited capability for complex layouts

def main():
    root = Tk()

    #1 Вариант: Отображаем Label сверху и посередине окна на желтом фоне, при изменении размеров окна метка также перемещается по центру и сверху окна.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack()

    #2 Вариант: Отображаем Label слева и сверху окна на желтом фоне, текст находится слева и не изменяется, а сама метка увеличивается по оси X.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = X)

    #3 Вариант: Тоже самое, что и в 1 варианте.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = Y)

    #4 Вариант: Тоже самое, что и во 2 варианте.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = BOTH)

    #5 Вариант: Отображаем Label слева и посередине окна на желтом фоне, текст находится слева и смещается по оси Y при изменении размеров окна, а сама метка увеличивается по оси X и по оси Y.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = BOTH, expand = True)

    # Блок №1/////////////////////////////////////////////////////////
    #Label ведёт себя также как Вариант 5.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(fill = BOTH, expand = True)
    #Label ведёт себя также как Вариант 2.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(fill = BOTH)
    #Label ведёт себя также как Вариант 5.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(fill = BOTH, expand = True)
    #/////////////////////////////////////////////////////////

    # Блок №2/////////////////////////////////////////////////////////
    #Labels присоедины друг к другу по оси X и весь блок из 3 Labels при изменении размеров окна не меняит своего размера и премещается по оси Y.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(side = LEFT)
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT)
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(side = LEFT)
    #/////////////////////////////////////////////////////////

    # Блок №3/////////////////////////////////////////////////////////
    #Labels присоедины друг к другу по оси X.
    #При изменении размеров окна Label не меняет ни своего размера ни местоположения он находится в верхнем левом углу
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(side = LEFT, anchor = 'nw')
    #При изменении размеров окна Label 2 и Label 3 не меняют своего положения по оси X и смещаются по оси Y.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT)
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(side = LEFT)
    #/////////////////////////////////////////////////////////

    # Блок №4/////////////////////////////////////////////////////////
    #Labels присоедины друг к другу по оси X.
    #При изменении размеров окна Label не меняет ни своего размера ни местоположения он находится в верхнем левом углу
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(side = LEFT, anchor = 'nw')
    #Labek 2 отрисовывается 10 пикселов от правого  края Label 1,  10 пикселов от левого края Label 3 и 10 пикселов от верхнего края окна и 10 пикселов от нижнего края окна.
    #При изменении размеров окна Label 2 не меняют своего положения по оси X и смещаются по оси Y.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
    #При изменении размеров окна Label 3 не меняют своего положения по оси X и смещаются по оси Y.
#    ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(side = LEFT)
    #/////////////////////////////////////////////////////////

    # Блок №5/////////////////////////////////////////////////////////
    #Labels присоедины друг к другу по оси X.
    #При изменении размеров окна Label не меняет ни своего размера ни местоположения он находится в верхнем левом углу
    label = ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow').pack(side = LEFT, anchor = 'nw')
    #Метод pack() не возвращает объект, если нам надо создать экземпляр объекта, то необходимо сначала создать элемент и присвоить его переменной, а потом вызвать метод pack()
    print ( label ) #None
    #Label 2 отрисовывается 10 пикселов от правого  края Label 1,  10 пикселов от левого края Label 3 и 10 пикселов от верхнего края окна и 10 пикселов от нижнего края окна.
    #При изменении размеров окна Label 2 не меняют своего положения по оси X и смещаются по оси Y.
    label = ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue')
    label.pack(side = LEFT, padx = 10, pady = 10)
    print ( label )#.18082480
    #Labek 3 отрисовывается 10 пикселов больше по оси X и на 10 пикселов больше по оси Y.
    #При изменении размеров окна Label 3 не меняют своего положения по оси X и смещаются по оси Y.
    ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(side = LEFT, ipadx = 10, ipady = 10)
    #/////////////////////////////////////////////////////////

    #Здесь мы одинаково сконфигурируем все элементы упаковынные с помощью Pack Geometry Manager
    #Все Labels при изменении размера окна будут заполнять пространство, текст будет в элементах слевого края и перемещаться по оси Y.
    for widget in root.pack_slaves():
        widget.pack_configure(fill = BOTH, expand = True)
        #Отображаем свойства упаковки элементов Pack Geometry Manager.
        print ( widget.pack_info()) #{'fill': 'both', 'ipadx': 0, 'side': 'left', 'expand': 1, 'pady': 0, 'in': <tkinter.Tk object at 0x011594F0>, 'ipady': 0, 'padx': 0, 'anchor': 'nw'}
                                    #{'fill': 'both', 'ipadx': 0, 'side': 'left', 'expand': 1, 'pady': 10, 'in': <tkinter.Tk object at 0x011594F0>, 'ipady': 0, 'padx': 10, 'anchor': 'center'}
                                    #{'fill': 'both', 'ipadx': 10, 'side': 'left', 'expand': 1, 'pady': 0, 'in': <tkinter.Tk object at 0x011594F0>, 'ipady': 10, 'padx': 0, 'anchor': 'center'}

    #Label 2 будет удалена из области окна, но сам объект label при этом не будет удалён.
    label.forget()

    root.mainloop()
if __name__ == '__main__':
    main()
