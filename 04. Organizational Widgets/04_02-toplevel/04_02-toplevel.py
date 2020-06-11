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
from tkinter import ttk

def main():
    root = Tk()
    root.title('Main Window')
    window = Toplevel(root)
    window.title('New Window')

    #Если мы закроем главное окно ('Main Window'),
    #то дочернее окно тоже закроется ('New Window').

    window.lower()#Данное окно будет отображено под главным окном
    window.lift(root)#Данное окно будет отображено над главным окном
    window.state('zoomed')#Окно будет развернуто на весь экран

    window.state('withdrawn')#Новое окно не будет видно
    window.state('iconic')#для того чтобы окно стало видно пользователю
    window.state('normal')#Окно будет возвращено в изначальную состояние (zoomed)
    print(window.state())   #zoomed
    window.state('normal')#Еще один вызов приведёт окно в
                          #предыдущее состояние (normal)
    print(window.state())   #normal
    window.iconify()#Свернет окно в нижнюю панель
    window.deiconify()#Приведет в нормальное состояние
    print(window.state())   #normal

    #По умолчанию окно создаётся 200 x 200 пикселей.
    #geometry() Method
    #window.geometry('WIDTHxHEIGHT+X+Y')
    window.geometry('640x480+50+100')#640x480 - размер окна
                                     #50 - расстояние от левого края экрана до
                                     #крайней левой стороны окна.
                                     #100 - расстояние от верха экрана до
                                     #крайней верхней стороны окна.
    #window.geometry('1280x800+100+50')

    #По умолчанию мы можем менять размеры окна с помощью мыши.

    window.resizable(False,False)#Теперь мы не сможем менять размер окна не в
                                 #право, не в вниз. И кнопка "Развертывания"
                                 #будет недоступна.

    window.maxsize(640, 480)#Устанавливаем максимальные размеры окна
    window.minsize(200,200)#Устанавливаем минимальные размеры окна
    window.resizable(True,True)

    #window.destroy() #Вызов данного метода уничтожит дочернее окно('New Window')
    #root.destroy()#Вызов данного метода уничтожит главное окно ('Main Window')
                   #и его дочернее окно('New Window').

    root.mainloop()

if __name__ == '__main__':
    main()
