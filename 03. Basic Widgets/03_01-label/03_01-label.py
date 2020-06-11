#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     14.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    label = ttk.Label ( root, text = "Hello, Tkinter!") #Hello, Tkinter
    label.pack ()
    label.config (text = "Howdy, Tkinter!") #Howdy, Tkinter!
    label.config (text = "Howdy, Tkinter! It\'s been a while since we last met.\
    Great to see you again!")
    #Howdy, Tkinter! It's been a while since we last met.Great to see you again!

    label.config(wraplength = 150)  #Howdy, Tkinter! It's been a
                                    #while since we last met.
                                    #Great to see you again!
                                    #Здесь мы ограничили ширину элемента

    label.config(justify = CENTER)  #Howdy, Tkinter! It's been a
                                    #  while since we last met.
                                    #  Great to see you again!
                                    #Позиционирование на элементе, как мы видим
                                    #текст будет напечатан на середине
    label.config(foreground = 'blue', background = 'yellow')
                            #foreground - цвет текста
                            #background - цвет фона

    label.config( font = ('Courier', 18, 'underline'))
                            #Courier - тип шрифта
                            #18 - размер шрифта
                            #bold - тип шрифта
                                    #bold - простой текст
                                    #underline - подчеркнутый
                                    #надо найти - жирный

    print (label.config())  #{'borderwidth': ('borderwidth', 'borderWidth',
    #'BorderWidth', '', ''), 'background': ('background', 'frameColor',
    #'FrameColor', '', <border object: 'yellow'>), 'style': ('style', 'style',
    #'Style', '', ''), 'wraplength': ('wraplength', 'wrapLength', 'WrapLength',
    #'', 150), 'justify': ('justify', 'justify', 'Justify', '',
    #<index object: 'center'>), 'state': ('state', 'state', 'State',
    #<index object: 'normal'>, <index object: 'normal'>),
    #'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
    #'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', ''),
    #'compound': ('compound', 'compound', 'Compound', <index object: 'none'>,
    #<index object: 'none'>), 'foreground': ('foreground', 'textColor',
    #'TextColor', '', <color object: 'blue'>), 'cursor': ('cursor', 'cursor',
    #'Cursor', '', ''), 'image': ('image', 'image', 'Image', '', ''),
    #'anchor': ('anchor', 'anchor', 'Anchor', '', ''), 'underline':
    #('underline', 'underline', 'Underline', -1, -1), 'padding':
    #('padding', 'padding', 'Pad', '', ''), 'width': ('width', 'width',
    #'Width', '', ''), 'relief': ('relief', 'relief', 'Relief', '', ''),
    #'text': ('text', 'text', 'Text', '', "Howdy, Tkinter! It's been
    #a while since we last met.    Great to see you again!"),
    #'font': ('font', 'font', 'Font', '', <font object: 'Courier 18 bold'>),
    #'class': ('class', '', '', '', '')}

    label.config (text = "Howdy, Tkinter!")#На желтом фоне , Синим подчеркнутым
                                           #шрифтом Courier размером 18
                                           #отобразится Howdy, Tkinter!

    #Добавляем изобрвжение к Label
    logo = PhotoImage( file = "e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif")
    print (logo)    #pyimage1
    label.config(image = logo)#отобразится изображение
                              #python_logo.gif в элементе Label (на желтом фоне)
    #выставляем приритет отображения
    #label.config(compound = 'text')#На желтом фоне , Синим подчеркнутым
                                   #шрифтом Courier размером 18 отобразится
                                   #Howdy, Tkinter!
    label.config(compound = 'image')#отобразится изображение
                              #python_logo.gif в элементе Label (на желтом фоне)
    label.config(background = 'red')#отобразится изображение python_logo.gif
                                    #в элементе Label (на красном фоне)

    label.config(compound = 'center')#отобразится изображение python_logo.gif
                                    #в элементе Label (на красном фоне) и по
                                    #центру надпись Синим подчеркнутым
                                    #шрифтом Courier размером 18 отобразится
                                    #Howdy, Tkinter!

    label.config(compound = 'left')#отобразится изображение python_logo.gif
                                   #в элементе Label (на красном фоне) и
                                   #справа от  изображения Синим подчеркнутым
                                   #шрифтом Courier размером 18 отобразится
                                   #Howdy, Tkinter!

    #Чтобы сборщик мусора не удалил изображение раньше времени
    #мы сохраним его в объекте Label и сконфигурируем его через свой же
    #внутренний объект
    label.img = logo
    label.config(image = label.img)
    #Теперь сборщик мусора освободит обект изображение (logo)
    #вместе с объектом Label

    print (label.config()) #{'compound': ('compound', 'compound',
    #'Compound', <index object: 'none'>, <index object: 'left'>),
    #'font': ('font', 'font', 'Font', '', <font object:
    #'Courier 18 underline'>), 'image': ('image', 'image', 'Image', '',
    #('pyimage1',)), 'underline': ('underline', 'underline', 'Underline',
    #-1, -1), 'relief': ('relief', 'relief', 'Relief', '', ''),
    #'justify': ('justify', 'justify', 'Justify', '', <index object: 'center'>),
    #'class': ('class', '', '', '', ''), 'takefocus': ('takefocus', 'takeFocus',
    #'TakeFocus', '', ''), 'background': ('background', 'frameColor',
    #'FrameColor', '', <border object: 'red'>), 'foreground':
    #('foreground', 'textColor', 'TextColor', '', <color object: 'blue'>),
    #'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
    #'wraplength': ('wraplength', 'wrapLength', 'WrapLength', '', 150),
    #'borderwidth': ('borderwidth', 'borderWidth', 'BorderWidth', '', ''),
    #'state': ('state', 'state', 'State', <index object: 'normal'>,
    #<index object: 'normal'>), 'width': ('width', 'width', 'Width', '', ''),
    #'anchor': ('anchor', 'anchor', 'Anchor', '', ''), 'padding': ('padding',
    #'padding', 'Pad', '', ''), 'cursor': ('cursor', 'cursor', 'Cursor', '',
    #''), 'text': ('text', 'text', 'Text', '', 'Howdy, Tkinter!'),
    #'style': ('style', 'style', 'Style', '', '')}

    root.mainloop()
if __name__ == '__main__':
    main()
