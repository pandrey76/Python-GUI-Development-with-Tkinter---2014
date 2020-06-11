#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     24.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk

class EntryElementSample:

    def __init__(self):
        self._root = Tk()
        #Создаём элемент ввода
        self._entry = ttk.Entry(self._root, width = 30)

        self._button = ttk.Button(self._root, text='Display Entry!', command = self.DisplayEntry)

        self._delete_firstsymbol_button = ttk.Button(self._root, text='Delete firrst symbol Entry!', command = self.DeleteFirstSymbolEntry)

        self._delete_entry_button = ttk.Button(self._root, text='Delete Entry!', command = self.DeleteEntry)

        self._insert_entry_button = ttk.Button(self._root, text='Insert Entry!', command = self.InsertEntry)

        self._insert_to_the_end_button = ttk.Button(self._root, text='Insert in the end Entry!', command = self.InsertInTheEndEntry)


        self._password_checkbutton = ttk.Checkbutton(self._root, text = "Hide entering", command = self.HideEntering)


        self._value = BooleanVar()
        self._enabled_checkbutton = ttk.Checkbutton(self._root, text = "Enabled entering", command = self.EnabledEntering)
        self._enabled_checkbutton.config(variable = self._value, onvalue = True, offvalue = False)

        self._readonly_value = BooleanVar()
        self._readonly_checkbutton = ttk.Checkbutton(self._root, text = "Read only entering", command = self.ReadOnlyEntering)
        self._readonly_checkbutton.config(variable = self._readonly_value, onvalue = True, offvalue = False)

    def main(self):

        self._entry.pack()
        self._button.pack()
        self._delete_firstsymbol_button.pack()
        self._delete_entry_button.pack()
        self._insert_entry_button.pack()
        self._insert_to_the_end_button.pack()
        self._password_checkbutton.pack()
        self._enabled_checkbutton.pack()
        self._readonly_checkbutton.pack()
        self._root.mainloop()


    def DisplayEntry(self) :
        """
            Отоображаем в консоли содержимое Entry
        """

        print (self._entry.get())

    def DeleteFirstSymbolEntry(self) :
        """
            Удаляем первый символ содержимого Entry
        """

        self._entry.delete(0,1)
        print (self._entry.get())

    def DeleteEntry(self) :
        """
            Удаляем содержимое Entry
        """
        self._entry.delete(0,END)
        print (self._entry.get())

    def InsertEntry(self) :
        """
            Вставляем в Entry в начало строку
        """
        self._entry.insert(0,'Enter your password')
        print (self._entry.get())

    def InsertInTheEndEntry(self) :
        """
            Добавляем в Entry строку в конец
        """
        self._entry.insert(END,'Enter your password')
        print (self._entry.get())

    def HideEntering (self):
        """
            Делаем ввод в Entry, а также всё содержимое в виде символа "*".
        """
        if  self._entry['show'] == '*' :
            self._entry.config(show = '')
        else :
            self._entry.config(show = '*')

    def EnabledEntering (self):
        """
            Делаем доступный/недоступный ввод в Entry
        """
        if  self._entry.instate(['disabled']) == True :
            self._entry.state(['!disabled'])
            self._value.set(True)
        else :
            self._entry.state(['disabled'])
            self._value.set(False)

    def ReadOnlyEntering (self):
        """
            Делаем ввод в Entry только на чтение, т.е по сравнению с
            недоступным вводом, текст также нельзя редактировать,
            но можно выделить.
        """
        if  self._entry.instate(['disabled']) == False :
            if  self._entry.instate(['readonly']) == True :
                self._entry.state(['!readonly'])
                self._readonly_value.set(False)
            else :
                self._entry.state(['readonly'])
                self._readonly_value.set(True)


#Для элемента Entry нет метода "set", для этого нам надо сначала удалить
#содержимое элемента Entry, с помощью метода "delete", а потом вставить
#строку методом "insert".

if __name__ == '__main__':
    entryElement = EntryElementSample()
    entryElement.main()
