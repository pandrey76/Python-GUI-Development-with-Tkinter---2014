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
    line2 = canvas.create_line(0, 240, 640, 240, fill = 'yellow', width = 5)

    canvas.itemconfigure(line, smooth = "True")#Сглаживание:Прямая будет выглядеть как часть окружности, визуально сохраняются только координаты 1 и последних точек.
    canvas.itemconfigure(line, splinesteps = 4)#На сглаженной прямой определяются 4 равноудалённых друг от друга точки по которым проходит прямая в виде набора прямых отрезков.  прямой.
    canvas.itemconfigure(line, splinesteps = 100)#На сглаженной прямой определяются 100 равноудалённых друг от друга точки по которым проходит прямая в виде набора прямых отрезков.
                                                 #Визуально она выглядет, как после вызова метода "canvas.itemconfigure(line, smooth = "True")".

    print(canvas.coords(line))#[0.0, 0.0, 320.0, 240.0, 640.0, 0.0]

    canvas.delete(line) #Удаляем прямую из элемента canvas.

    ############################################################################

    #Создаем прямоугольник
    rect = canvas.create_rectangle(160,120,480,360)
    canvas.itemconfigure(rect, fill = 'red')#Заполняем красным

    #Создаем овал вписанный в прямоугольник
    oval = canvas.create_oval(160, 120, 480, 360)

    #Создаём дугу с радиусом в пол длинны прямоугольника
    arc = canvas.create_arc(160, 1, 480, 240)
    #Увеличиваем дугу (сектор) до 180 градусов и заполняем зеленым
    canvas.itemconfigure(arc,start = 0, extent = 180, fill = 'green')

    #Создаём многоугольник (в нашем случае треугольник)
    poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')#Заполняем синим

    #создаём текст
    text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

    logo = logo = PhotoImage(file = 'e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif')
    #Создаём изображение
    image = canvas.create_image(320, 240, image = logo)

    #Данные методы(lift и lower) определяют местоположение элементов, какой поверх какого будет отображаться
    canvas.lift(text)#Здесь мы видим текст нажодится поверх изображения
    canvas.lower(image)#Здесь мы видим, что изображение исчезло, оно просто располагается под нашим прямоугольником rect
    canvas.lower(image, text)#Здесь мы определяем, что изображение должно находится под текстом

    #Создаём кнопку
    button = Button(canvas, text = 'Click Me')
    button.config(command = PrintMess)
    canvas.create_window(320, 60, window = button)

    #Работа с тэгами, это может быть удобно чтобы обращаться к элементам внутри canvas
    canvas.itemconfigure(rect, tag = ('shape'))
    canvas.itemconfigure(oval, tag=('shape', 'round'))
    canvas.itemconfigure('shape', fill = 'grey')#прямоугольник и квадрат стали серыми
    canvas.itemconfigure('round', fill = 'brown')#Овал стал коричневым
    print(canvas.gettags(oval)) #('shape', 'round')

    canvas.lift(line2)#Линия отображается поверж всех элементов

    canvas.lower(line2)#Линия отображается под всеми элементами

    root.mainloop()

def PrintMess():
    print ('Click Me')

if __name__ == '__main__':
    main()
