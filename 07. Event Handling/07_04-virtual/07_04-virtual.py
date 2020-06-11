#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     07.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root)
entry.pack()

#надо ещё раз посмотреть!!!

#При событии считывания из элемента управления в буфер обмена будет вызываться lambda функция которая будет отображать в консоли строку 'Copy'.
entry.bind('<<Copy>>', lambda e: print('Copy'))
#При событии добавления строки из буфера обмена в элемент управления будет вызываться lambda функция которая будет отображать в консоли строку 'Paste'.
entry.bind('<<Paste>>', lambda e: print('Paste'))

#Создаём событие 'OddNumber'
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9' )

#Теперь когда я буду вводить в Entry цифры 1 или 3 или 5 или 7 или 9, то в консоли будет печататься 'OddNumber'
entry.bind('<<OddNumber>>', lambda e: print ('OddNumber'))

#Информация о событии
print(entry.event_info("<<OddNumber>>"))    #('1', '3', '5', '7', '9')

#Генерируем событие "OddNumber" (В консоли будет напечатоно 'OddNumber')
entry.event_generate('<<OddNumber>>')   #OddNumber
#Генерируем событие "Paste" (если в буфере обмена, что то содержалось, то оно будет выведено в элементе Entry
entry.event_generate('<<Paste>>')       #Paste

#Удаляем событие 'OddNumber'
#entry.event_delete("<<OddNumber>>")

root.mainloop()
def main():
    pass

if __name__ == '__main__':
    main()
