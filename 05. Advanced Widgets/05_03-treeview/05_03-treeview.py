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
def main():
    root = Tk()
    treeview = ttk.Treeview(root)
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


    root.mainloop()
if __name__ == '__main__':
    main()
