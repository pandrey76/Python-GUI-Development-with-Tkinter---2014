#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     27.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

def main():
    root = Tk()
    text = Text(root, width = 40, height = 10)#мы создали простой текстовый
            #редактор, который вместит в себя любой большой текст, он просто
            #если достигнет конца элемента сдвиет весь текст вверх и можно
            #будет продолжить печатать.

    text.config(wrap = 'word')#word - перенос строк будет осуществлятся без
                              #переноса слогов, т.е. слово полностью.

                              #char - перенос строк будет осуществлятся по
                              #достижении правой границы элемента.

                              #none - перенос строк осуществляется только по
                              #клавише "Enter", а так текст в строке будет
                              #смещатся влево.
    #при этом перенос строк, т.е. печатанье символа '\n' осуществляется только
    #после нажатия на клавишу "Enter".

    text.pack()

    #"base modifier modifier modifier"

    #    * Common Base Formats
    #      * line.char
    #      * end

    #    * Common Modifiers
    #      * +/-#chars and +/-#lines
    #      * linestart, lineend, wordstart, wordend


    text.insert('0.0', 'This is a long message in the text box which is more than 40 characters.\n\n\n\n\n\n\n\nIf the message hits the bottom of the text box it will run off the screen.\n')


    print(text.get('1.0', 'end')) #This is a long message in the text box which is
                           #more than 40 characters.\n\n\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    print(text.get('1.0', '1.end')) #This is a long message in the text box which is
                             #more than 40 characters.

    text.insert('1.0 + 2 lines', 'Insert message')

    print(text.get('1.0', 'end'))#This is a long message in the text box which is
                           #more than 40 characters.\n\nInsert message\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore...')
    print(text.get('1.0', 'end'))#This is a long message in the text box which is
                           #more than 40 characters.\n\nInsert message and\nmore and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n
    text.delete('1.0')
    print(text.get('1.0', 'end'))#his is a long message in the text box which is
                           #more than 40 characters.\n\nInsert message and\nmore and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    text.delete('1.0', '1.0 lineend')
    print(text.get('1.0', 'end'))#\n\nInsert message and\nmore and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    text.delete('1.0', '3.0 lineend + 1 chars ')#Удаляется три строки плюс символ новой строки.
    print(text.get('1.0', 'end'))#more and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    text.replace(1.0, '1.0 lineend', 'This is the first line.')
    print(text.get('1.0', 'end'))#This is the first line.\nmore and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n

    text.config(state = 'disabled')#При таком состоянии элемент будет не доступен для ввода.

    text.delete('1.0', 'end')#т.к элемент не доступен, то ничего не удалилось.
    print(text.get('1.0', 'end'))#This is the first line.\nmore and\nmore...\n\n\n\n\n\nIf the
                           #message hits the bottom of the text box it will
                           #run off the screen.\n


    text.config(state = 'normal')#При таком состоянии элемент будет не доступен для ввода.

    text.delete('1.0', 'end')#т.к элемент не доступен, то ничего не удалилось.
    print(text.get('1.0', 'end'))#Всё удалилось!!!

    root.mainloop()

if __name__ == '__main__':
    main()

