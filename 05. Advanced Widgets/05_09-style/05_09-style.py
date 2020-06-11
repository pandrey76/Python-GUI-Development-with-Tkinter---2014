#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     31.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#       Widget States

#   *active                 *background
#   *disable                *readonly
#   *focus                  *alternate
#   *pressed                *invalid
#   *selected               *hover

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    button1 = ttk.Button(root, text = 'Button 1')
    button2 = ttk.Button(root, text = 'Button 2')

    button1.pack()
    button2.pack()

    style = ttk.Style()

    #поддерживаемые темы окна
    print ( style.theme_names() )   #('winnative', 'clam', 'alt', 'default', 'classic', 'xpnative')

    #тема, которая сейчас используется для представления элементов
    print ( style.theme_use())  #xpnative

    #Меняем стиль окно будет выглядеть по другому
    style.theme_use('classic')
    #Возвращаем стиль к первоначальному
    style.theme_use('xpnative')

#    Widget Style Names

#   Usually "T" + widget name
#    * Example: TButton, TFrame, TCombobox

#   Exception to the rule
#   * Treeview (no extra 'T')
#   * TPanedwindow ('w' is only lowercase)
#   * Horizontal. TScale or Vertical.TScale
#   * Horizontal. TScrollbar or Vertical.TScrollbar
#   * Horizontal. TProgressbar or Vertical.TProgressbar

    #определяем класс (стиля)
    print ( button1.winfo_class())  #TButton

    #Меняем стиль
    style.configure('TButton', foreground = 'blue')

    #Создаём новый стиль
    style.configure('Alarm.TButton', foreground = 'orange', font = ('Arial', 24, 'bold') )

    #Вторая кнопка будет иметь тексе 'Arial', 24, 'bold' оранжевого цавета
    button2.config(style = 'Alarm.TButton')

    #связываем определённый стиль с сотоянием элемента:
    #                       * При нажатии на вторую кнопку текст будет розоваго цвета
    #                       * При отключённой кнопке текст будет серым.
    style.map('Alarm.TButton', foreground = [("pressed", 'pink'), ('disabled', 'grey')])


    #Цвет второй кнопки будет серым.
    print ( button2.state(['disabled']) )   #('!disabled',)

    #Печатаем все свойства стиля
    print ( style.layout('TButton'))#[('Button.button', {'sticky': 'nswe', 'children': [('Button.focus', {'sticky': 'nswe', 'children': [('Button.padding', {'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nswe'})]})]})]})]


    #Посмотреть ещё раз 8:10.

#   style.layout("TButton")
#   [('Button.button', {'sticky': 'nswe', 'children' :
#            [('Button.focus', {'sticky: 'nswe', 'children':
#            [('Button.padding', {'sticky: 'nswe', 'children':
#                    [('Button.label', {'sticky: 'nswe'})]})]})]})]

#            |-----------------------------|
#            |      Button Element         |
#            |  |-----------------------|  |
#            |  |    Focus Element      |  |
#            |  | |-------------------| |  |
#            |  | |  Padding Element  | |  |
#            |  | | |---------------| | |  |
#            |  | | | Label Element | | |  |
#            |  | | |---------------| | |  |
#            |  | |-------------------| |  |
#            |  |-----------------------|  |
#            |-----------------------------|
#


    #Определяем аттрибуты элемента 'Button.label', которые отвечают за его стиль отрисовки
    print ( style.element_options('Button.label') )#('-compound', '-space', '-text', '-font', '-foreground', '-underline', '-width', '-anchor', '-justify', '-wraplength', '-embossed', '-image', '-stipple', '-background')

    #Отображаем конкретный стиль аттрибута элемента (цвет шрифта у стиля TButton)
    print ( style.lookup('TButton', 'foreground'))  #blue

    root.mainloop()

if __name__ == '__main__':
    main()
