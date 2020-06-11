#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     01.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import messagebox

print ( messagebox.showinfo(title = 'A Friendly Message', message = 'Hello, Tkinter') )#'ok'

#   Messagebox Types: Informationnal

#   * showinfo()
#   * showwarning()
#   * showerror()

print ( messagebox.askyesno(title = "Hungry?", message = "Do you want SPAM?") ) #True/False

#   Messagebox Types: Questions

#   * askyesno()
#   * askokcancel()
#   * askretrycancel()
#   * askquestion()

from tkinter import filedialog

filename = filedialog.askopenfile()
print(filename.name)# E:/Rabota/Обучение/Python GUI Development with Tkinter - 2014/05. Advanced Widgets/05_10-dialog/05_10-dialog.py
                    # C:/1.xml

#   Filedialog Types

#   * askdirectory()
#   * asksaveasfile(mode)
#   * asksaveasfilename()

#   * askopenfile(mode)
#   * askopenfiles(mode)
#   * askopenfilename()
#   * askopenfilenames()

from tkinter import colorchooser

#Инициализируем белым цветом
print (colorchooser.askcolor(initialcolor = '#FFFFFF'))#((0.0, 0.0, 0.0), '#000000') выбрал черный
#((0.0, 128.5, 0.0), '#008000') Выбрал зелёный
#((0.0, 128.5, 255.99609375), '#0080ff') Выбрал какой то голубой.
#Возвращается два параметра
#Первый параметр возвращает список парметров компонент палитры (red, grin, blue).
#Второй параметр шестнадцатиричное пердставление выбранного цвета


#if __name__ == '__main__':
#    main()
