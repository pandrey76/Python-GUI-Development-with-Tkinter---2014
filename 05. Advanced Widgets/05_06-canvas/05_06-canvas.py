#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     28.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Canvas предоставляет пространство для рисования и отображения других элементов управления

from tkinter import *
def main():
    root = Tk()
    canvas = Canvas(root)
    canvas.pack()
    canvas.config(width = 640, height = 480)

    #Создаём прямую в элементе canvas по двуь точкам, синего цвета и толщиной 5 пикселей
    line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)

    #Меняем цвет прямой на зелёный
    canvas.itemconfigure(line, fill = 'green')

    print(canvas.coords(line))#[160.0, 360.0, 480.0, 120.0]

    #Здесь мы передаём три координаты по которым будет перестроена прямая
    canvas.coords(line, 0, 0, 320, 240, 640, 0)#Отобразится две стороны равнобедренного треугольника.
    lene2 = canvas.create_line(0, 240, 640, 240, fill = 'yellow', width = 5)

    canvas.itemconfigure(line, smooth = "True")#Сглаживание:Прямая будет выглядеть как часть окружности, визуально сохраняются только координаты 1 и последних точек.
    canvas.itemconfigure(line, splinesteps = 4)#На сглаженной прямой определяются 4 равноудалённых друг от друга точки по которым проходит прямая в виде набора прямых отрезков.  прямой.
    canvas.itemconfigure(line, splinesteps = 100)#На сглаженной прямой определяются 100 равноудалённых друг от друга точки по которым проходит прямая в виде набора прямых отрезков.
                                                 #Визуально она выглядет, как после вызова метода "canvas.itemconfigure(line, smooth = "True")".

    print(canvas.coords(line))#[0.0, 0.0, 320.0, 240.0, 640.0, 0.0]

    canvas.delete(line) #Удаляем прямую из элемента canvas.
    root.mainloop()

if __name__ == '__main__':
    main()
