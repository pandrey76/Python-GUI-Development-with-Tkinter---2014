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

from tkinter import *
def main():
    root = Tk()

    #!!!!Данная строка обязательно должна присутствовать пред созданием меню
    #Надо более детально разобраться!!!
    root.option_add('*tearOff', False)

    menubar = Menu(root)#Создаём меню

    root.config(menu = menubar)#Связываем меню с главным окном

    #Создаём элементы главного меню
    file = Menu(menubar)
    edit = Menu(menubar)
    help_ = Menu(menubar)

    #Настраиваем и связываем элементы главного меню
    menubar.add_cascade(menu = file, label = 'File')
    menubar.add_cascade(menu = edit, label = 'Edit')
    menubar.add_cascade(menu = help_, label = 'Help')

    #добавляем и настраиваем элементы подменю, определяем команды меню
    file.add_command(label = 'New', command = lambda: print('New File'))
    file.add_separator()#добавляем разделитель
    file.add_command(label = 'Open', command = lambda: print('Opening File...'))
    file.add_command(label = 'Save', command = lambda: print('Save File...'))


    #!!!!Добавляем Hot key, но почему то не работает надо разобраться.
    file.entryconfig('New', accelerator = 'Ctrl + N')#В меню справа от заголовка "New" будет надпись "Ctrl + N".

    #Добавляем изображение
    logo = logo = PhotoImage(file = 'e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif').subsample(10,10)
    file.entryconfig('Open', image = logo, compound = 'left') #Справа от изображения будет заголовок меню.


    file.entryconfig('Open', state = 'disabled') #Делаем элемент меню неактивным

    file.delete('Save') #Удаляем элемент меню

    #Создаем подменю
    save = Menu(file)
    #Добавляем подменю
    file.add_cascade(menu = save, label = "Save")
    #Добавляем подэлементы и конфигурируем
    save.add_command(label = 'Save As', command = lambda: print ('Saving As...'))
    save.add_command(label = 'Save All', command = lambda: print ('Saving All...'))

    #Добавляем radiobutton в элементы меню
    choice = IntVar()
    edit.add_radiobutton(label = 'One', variable = choice, value = 1)
    edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
    edit.add_radiobutton(label = 'Three', variable = choice, value = 3)

    #Создаём Popup меню.
    #Здесь не рассматривается вопрос как получить координаты курсора и перехватить событие нажатия на правую кнопку мыши.
    file.post(400,300)#Меню будет отображено 400 пикселов правее от левой стороны экрана и 300 пикселов вниз от верхней стороны экрана.


    root.mainloop()


if __name__ == '__main__':
    main()
