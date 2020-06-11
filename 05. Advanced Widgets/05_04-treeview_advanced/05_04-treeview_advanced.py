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
from tkinter import ttk

root = Tk()
treeview = ttk.Treeview(root)

def main():

    treeview.pack()
    #Создали первую элемент
    print(treeview.insert('', '0', 'item1', text = 'First Item'))#item1
    #Создали второй элемент
    print(treeview.insert('', '1', 'item2', text = 'Second Item'))#item2

    print(treeview.insert('', 'end', 'item3', text = 'Third Item'))#item3

    logo = PhotoImage(file = 'e:\\Rabota\\Обучение\\Python GUI Development with Tkinter - 2014\\Exercise Files\\python_logo.gif').subsample(10,10)

    print(treeview.insert('item2', 'end', 'python', text = 'Python', image = logo))#python

    treeview.config(height = 5)#Уменьшаем размер элемента Treeview по высоте.

    treeview.move('item2', 'item1', "end")#Перемещаем item2 внутрь item1 в конец.

    #С помощью данного метода можно конфигурировать отдельные элементы Treeview
    treeview.item('item1', open = True)#При первом запуске элемент item1 будет
                                       #рвскрыт.
    print(treeview.item('item1', 'open'))#1

    #С помощью даного метода можно удалить элемент из Treeview, но при этом
    #элемент не улаляется.
    treeview.detach('item3')#Элемет item3 будет удалён из элемента Treeview

    treeview.move('item3', 'item2', '0')#Перемещаем item3 внутрь item2 вначало списка.

    #С помощью даного метода можно полностью удалить элемент.
    treeview.delete('item3')
    #treeview.move('item3', 'item2', '0')#_tkinter.TclError: Item item3 not found.

    ###########################################################################

    #Добавляем столбцы
    treeview.config(columns = ('version'))

    #Конфигурируем столбец
    treeview.column('version', width = 50, anchor = 'center')#Для столбца
                            #version устанавливаем ширину и расположение текста.

    treeview.column('#0', width = 150)#Определяем ширину певого столбца

    #С помощью даного метода можно настраивать заголовок столбца.
    treeview.heading("version", text = 'Version')#Для столбца version устанавливаем текст заголовка.

    #С помощью даного метода можно устанавливать строки для элемента под столбцами.
    treeview.set('python', 'version', '3.4.1')#Устанавливаем для элемента python строку в столбец version.

    #С помощью даного метода можно определить тэги для элемента.
    treeview.item('python', tags = ('software'))
    #С помощью даного метода можно конфигурировать тэги элемента.
    treeview.tag_configure('software', background = 'yellow')#весь элемент python будет на желтом фоне.

    #Определяем метод, который будет вызываться при выделении элемента в Treeview
    #Если держать клавишу "Ctrl" то можно выделить несколькл элементов
    treeview.bind('<<TreeviewSelect>>', callback)

    #Настраиваем режим выделения
    treeview.config(selectmode='browse')#выделяем один элемент, даже если держать клавишу "Ctrl" всё равно будет выделятся по одному элементу

    treeview.config(selectmode = 'none')#элементы больше выделятся не будут из UserMode

    #Элемент python будет выделен
    print(treeview.selection_add('python'))# ('python',)
    #Будет снято выделение с элемента python
    print(treeview.selection_remove('python'))#None
    #Элемент python будет снова выделен
    print(treeview.selection_toggle('python'))# ('python',)

    root.mainloop()


def callback(event):
    print(treeview.selection()) #выделен один элемент ('item1',)
    #Выделено несколько элементов ('item1', 'item2', 'python')


if __name__ == '__main__':
    main()
