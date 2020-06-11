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

    text.insert('0.0', 'This is a long message in the text box which is more than 40 characters.\n\n\n\n\n\n\n\nIf the message hits the bottom of the text box it will run off the screen.\n')

    text.tag_add('my_tag', '1.0', '1.0 wordend')
    text.tag_configure('my_tag', background = 'yellow')#Первое слово "This" будет на желтом фоне.

    print(text.tag_ranges('my_tag'))#(<textindex object: '1.0'>, <textindex object: '1.4'>)

    #Ещё раз просмотреть видео по поводу возможных колизий между тегами и как с этим разбираться (01:40)!!!

    text.tag_remove("my_tag", "1.1", "1.3")#Теперь на желтом фоне будут первая буква 'T' и последняя 's'.

    print(text.tag_ranges('my_tag'))#(<textindex object: '1.0'>, <textindex object: '1.1'>, <textindex object: '1.3'>, <textindex object: '1.4'>)

    print(text.tag_names())#('sel', 'my_tag') sel - это специализированный тэг, который мы можем использовать для того чтобы определять и управлять выделенным текстом.

    print (text.tag_names(1.0))#('my_tag',)

    text.replace('my_tag.first', 'my_tag.last', 'That')#Мы поменяли "This" на "That", но при этом текст у нас напечатан уже не на желтом фоне.

    text.tag_delete('My_tag')#Удалили наш тэг

    print(text.mark_names())    #('insert', 'current')

    #Automatically Tracked Text Marks

    # * insert - current index of insertion cursor.
    # * current - index of character under mouse position

    text.insert('insert', '_')#В месте где находится курсор после выполнения этой команды появится символ '_'

    #С маркированием надо дополнительно разобраться!!!!
    text.mark_set('my_mark', 'end')#Мы создалм маркер, в качестве маркера весь текст.

    text.mark_gravity('my_mark', 'right')

    text.mark_unset('my_mark')

    image = PhotoImage(file = 'e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif')

    #text.image_create('insert',image = image)#После выполнения изображение будет отображено в месте где находится курсор
    text.image_create(2.0, image = image)#После выполнения изображение будет отображено вначале 3 строки.

    button = Button(text, text='Click Me')

    #text.window_create('insert', window = button)#После выполнения кнопка будет отображено в месте где находится курсор

    text.window_create(9.1, window = button)#После выполнения кнопка будет отображено на 10 строке между первой ("I") и вторым букывами ("f").

    root.mainloop()

if __name__ == "__main__":
    main()