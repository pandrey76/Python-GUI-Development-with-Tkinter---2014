#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     11.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#В этом уроке мы научимся как создавать графические элементы tkinter,
#попробуем несколькими способами их настроить
#и разберемся какая между ними разница.

#               "Root"
#               Window
#   /      /      |      \        \
#Lable  Entry   Lable   Frame   Button
#                     /   |   \
#                Lable  Radio   Radio
#                       Button  Button

from tkinter import *   #Импортируем все из tkinter
from tkinter import ttk #импортируем пакет ttk
                        #для работы с виджетами с префиксом ttk.


def main():
    root = Tk() #Создаётся новое окно самого верхнего уровеня

    button = ttk.Button(root, text = 'Click Me!')
    button.pack()   #отражаем элемент на окне
    print(button['text'])   #Click Me!
    button['text'] = 'Press Me' #Ещё один способ настройки аттрибутов виджета
    print(button['text'])   #Press Me
    #На главном окне у кнопки будет текст "Press Me"
    button.config(text = 'Push Me') #И ещё один способ настройки
                                    #аттрибутов виджета.
    #На главном окне у кнопки будет текст "Push Me"

    print (button.config()) #{'class': ('class', '', '', '', ''),
    #'width': ('width', 'width', 'Width', '', ''),
    #'state': ('state', 'state', 'State', <index object: 'normal'>,
    #<index object: 'normal'>), 'default': ('default', 'default', 'Default',
    #<index object: 'normal'>, <index object: 'normal'>),
    #'underline': ('underline', 'underline', 'Underline', -1, -1),
    # 'style': ('style', 'style', 'Style', '', ''),
    #'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
    # 'cursor': ('cursor', 'cursor', 'Cursor', '', ''),
    #'takefocus': ('takefocus', 'takeFocus', 'TakeFocus',
    #'ttk::takefocus', 'ttk::takefocus'),
    #'command': ('command', 'command', 'Command', '', ''),
    #'compound': ('compound', 'compound', 'Compound',
    #<index object: 'none'>, <index object: 'none'>),
    #'text': ('text', 'text', 'Text', '', 'Push Me'),
    #'image': ('image', 'image', 'Image', '', ''),
    #'padding': ('padding', 'padding', 'Pad', '', '')}
    #метод возвращает словарь, содержащий все возможные аттрибуты объекта,
    #которые можно настроить. Каждый объект tkinter содержет уникальный
    #псевдоним (идентификатор), ссылку на объект в библиотеке Tk.

    print(str(button))  #.18085936 идентификатор элемента в библитеке Tk.
                        #точнее ссылка на элемент.

    print( str (root))  # . - главное окно

    #ttk.Label (root, text = 'Hello, Tkinter!').pack()
    lable = ttk.Label (root, text = 'Hello, Tkinter!')
    lable.pack()

    print( str ( lable) )   #.18086192
    root.mainloop()

if __name__ == '__main__':
    main()
