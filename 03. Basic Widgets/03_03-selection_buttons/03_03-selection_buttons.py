#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     18.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk



class CheckButtonImplementation :

    def __init__(self):
       self._root = Tk()
       self._spam = StringVar()
       self._breakfast = StringVar()
       self._checkbutton = None

    def main(self):

        self._checkbutton = ttk.Checkbutton(self._root, text = 'SPAM?')
        self._checkbutton.pack()#Отобразится обычный CheckButtomn

        #Tkinter Variable Classes
        #С элементом управления можно ассоциировать переменную, которая
        #будет менятся вместе с состоянием самого элемента управления.
            # * BoleanVar
            # * DoubleVar
            # * IntVar
            # * StringVar

        self._spam.set('SPAM!')

        print(self._spam.get())

        #при выбранном checkbutton значение переменной ассоциированной с
        #checkbutton будет равно "SPAM Please!", при отключенном checkbutton
        #будет равно Boo SPAM.
        self._checkbutton.config(variable = self._spam, onvalue = 'SPAM Please!', offvalue = 'Boo SPAM')
        self._checkbutton.config(command = self.PrintCheckbuttonVariable)

        #Ассоциируем переменную с набором элементов типа Radiobutton
        #При выделении этого элемента активируются этот и четвертый элемент
        #Radiobutton.
        ttk.Radiobutton(self._root, text = 'SPAM', command = self.PrintRadiobuttonVariable, variable = self._breakfast, value='SPAM').pack()

        ttk.Radiobutton(self._root, text = 'Eggs', command = self.PrintRadiobuttonVariable, variable = self._breakfast, value='Eggs').pack()
        ttk.Radiobutton(self._root, text = 'Sausage', command = self.PrintRadiobuttonVariable, variable = self._breakfast, value='Sausage').pack()

        #При выделении этого элемента активируются этот и первый элемент
        #Radiobutton.
        ttk.Radiobutton(self._root, text = 'SPAM', command = self.PrintRadiobuttonVariable, variable = self._breakfast, value='SPAM').pack()

        ttk.Button(self._root, text='Triget Checkbutton!', command = self.TrigetCheckButton ).pack()

        self._root.mainloop()

    def PrintCheckbuttonVariable(self) :
        """
           Если выделим checkbutton, то в консоли будет выведено значение
           "SPAM Please!". Если снимим выделение с
           checkbutton, то в консоли будет выведено значение "Boo SPAM".
        """
        print (self._spam.get())

    def PrintRadiobuttonVariable(self) :
        """
            При выделении Radiobutton вызывается эта функция. которая отображает
            в консоли текущее значение ассоциативной переменной, которая меняет
            своё значение на значение текущего выделенного элемента Radiobutton.
        """
        print (self._breakfast.get())

    def TrigetCheckButton(self) :
        """
            Настраиваем на checkbutton другую переменную. И при выборе значений
            Radiobutton название элемента checkbutton будет менятся на заголовок
            текущего выбранного элемента Radiobutton.
        """
        self._checkbutton.config( textvariable = self._breakfast )


if __name__ == '__main__':
    checkButton = CheckButtonImplementation();
    checkButton.main()
