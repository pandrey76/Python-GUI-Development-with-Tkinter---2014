﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     10.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Создадим первую программу на Python с простым GUI,
#используя пакета tkinter


from tkinter import *   #Импортируем все из пакета tkinter
#В Python 3 версии пакет tkinter начинается с маленькой буквы, тогда как
#в версии Python 2 начиналась с большой Tkinter, поэтому у вас не будет
#работать файлы второй версии в третей и на оборот.

def main():
    root = Tk() #Создаем верхний (головной) элемент (главное окно)
    Label(root, text="Hello, Tkinter").pack() #Создаем элемент Lable
                                #(Надпись с текстом "Hello, Tkinter", как
                                #дочерний относительно головного элемента root и
                                #используем управляющий метод pack для того
                                #чтобы положить элемент на главное окно
    root.mainloop() #Для окна root запускаем основной цикл обработки сообщений
    #После запуска мы видим окно с одной нажписью "Hello, Tkinter". Это окно
    #можно перемещать, разворачивать, менять размеры и закрыть.
if __name__ == '__main__':
    main()
