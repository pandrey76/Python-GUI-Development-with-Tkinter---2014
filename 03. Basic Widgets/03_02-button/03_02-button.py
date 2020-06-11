#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     17.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    button = ttk.Button ( root, text='Click Me')
    button.pack()#Создали и отобразили простую кнопку
    button.config ( command = callback ) #При каждом нажатии на кнопку в
                                         #консоли будет выведено Clicked!
    #Данный метод вызывает функцию кнопки ("callback") и возвращает то что фунция
    #"callback" возвратила
    print (button.invoke()) #Clicked!
                            #None

    #устанавливаем состояние кнопки
    button.state ( ['disabled'])    #Кнопка будет засерена и не доступна

    #Проверка состояния кнопки
    print (button.instate ( ['disabled']))  #True

    #устанавливаем новое состояние кнопки
    button.state ( ['!disabled']) #Кнопка будет доступна для нажатий

    print (button.instate ( ['!disabled']))  #True

    logo = PhotoImage( file = "e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif")
    button.config ( image = logo, compound = LEFT ) #Кнопка будет иметь
    #достаточно большой размер видимо размер python_logo.gif по умолчанию,
    #т.е высоту и ширину плюс растояние необходимое, чтобы вместилась
    #надпись Click Me, т.к. справа от изображения будет надпись Click Me.

    small_logo = logo.subsample(5, 5)
    button.config ( image = small_logo )#Кнопка будет иметь
    #намного меньший размер: высоту равную 5 пикселям, т.е. равную высоте
    #изображения и ширину 5 + растояний необходимое, чтобы вместилась
    #надпись Click Me (слева будет изображение, а с справа от изображения
    #будет надпись Click Me).

    root.mainloop()


def callback ():
    print ( "Clicked!" )

if __name__ == '__main__':
    main()
