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

class SelectionsBoxes :

    def __init__(self):
        self._root = Tk()
        self._month = StringVar()
        self._combobox = ttk.Combobox(self._root, textvariable = self._month)

        self._combo_print_button = ttk.Button(self._root,
                                              text = 'Display combo',
                                              command = self.DisplayCombo)

        self._edit_for_combo = ttk.Entry(self._root, width = 30)
        self._combo_set_button = ttk.Button(self._root,
                                              text = 'Set combo',
                                              command = self.SetCombo)
        self._year = StringVar()
        self.spinbox = Spinbox(self._root, from_ = 1990, to = 2017,
                        textvariable = self._year)
        self._spinbox_print_button = ttk.Button(self._root,
                                              text = 'Display spin',
                                              command = self.DisplaySpin)

        self._readonly_value = BooleanVar()
        self._readonly_checkbutton = ttk.Checkbutton(self._root,
                                         text = "Read only combo",
                                         command = self.ReadOnlyCombo)
        self._readonly_checkbutton.config(variable = self._readonly_value,
                                          onvalue = True, offvalue = False)
    def main(self):
        self._combobox.pack()
        self._combobox.config(values =
                                    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ))

        self._combo_print_button.pack()
        self._edit_for_combo.pack()
        self._combo_set_button.pack()
        self._readonly_checkbutton.pack()
        self.spinbox.pack()
        self._spinbox_print_button.pack()

        self._root.mainloop()

    def DisplayCombo(self):
        print(self._month.get())

    def SetCombo(self):
        self._month.set(self._edit_for_combo.get())

    def DisplaySpin(self):
        print(self._year.get())

    #Если самому вводить данные в Combobox или Spinbox, то через переменную
    #связанную с элементом (_month или _year) мы считаем то значение которое
    #ввели, поэтому очень внимательно необходимо осуществлять ввод имено тех
    #значений, которые определены списком values, для Combobox или значениями
    #определенными параметрами (from_ и to) для Spinbox. Иначе предварительно
    #обрабатывать введенные данные или ввод данных запрещать.


    def ReadOnlyCombo (self):
        """
            Делаем ввод в Combobox только на чтение,т.е ввод значений с
            клавиатуры недоступен. Но через метод SetCombo также можно
            вводить любые данные.

            Для SpinBox пока не понятно как добавлять свойство ReadOnly!!!!!!
        """
        if  ( self._combobox.instate(['readonly']) == True ) :
            self._combobox.state(['!readonly'])
            self._readonly_value.set(False)
        else :
            self._combobox.state(['readonly'])
            self._readonly_value.set(True)

if __name__ == '__main__':
    selection_boxes = SelectionsBoxes()
    selection_boxes.main()

