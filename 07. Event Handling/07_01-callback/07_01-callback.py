#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     04.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

root = Tk()

    #Блок №1 /////////////////////////////////////////////////////////////////////
#def ClickButton1():
#    print ('In the callback')
#ttk.Button(root, text = 'Click Me', command = ClickButton1).pack()

    #//////////////////////////////////////////////////////////////////////////////

    #Блок №2 /////////////////////////////////////////////////////////////////////
    #При запуске данного блока программа выведет три значения 1, 2 и 3 и при нажатии на кнопки ничего происходить не будет.
    #Так происходит потому что когда программа первый раз запускается она ставит соответствие свойства "command" и функции,
    #она также запускает функцию при каждом соответствии свойства "command" и функциии, далее устанавливает возвращаемое значение для свойства "command",
    #т.к. функция ClickButton ничего не возвращает, то свойства "command" становится равным None. Поэтому при нажатии на кнопки ничего происходить не будет.

#def ClickButton(number):
#    print (number)
#ttk.Button(root, text = 'Click Me 1', command = ClickButton(1)).pack()
#ttk.Button(root, text = 'Click Me 2', command = ClickButton(2)).pack()
#ttk.Button(root, text = 'Click Me 3', command = ClickButton(3)).pack()


    #//////////////////////////////////////////////////////////////////////////////


    #Блок №3 /////////////////////////////////////////////////////////////////////
    #теперь всё работает корректно

def ClickButton(number):
    print (number)
ttk.Button(root, text = 'Click Me 1', command = lambda: ClickButton(1)).pack()  #1
ttk.Button(root, text = 'Click Me 2', command = lambda: ClickButton(2)).pack()  #2
ttk.Button(root, text = 'Click Me 3', command = lambda: ClickButton(3)).pack()  #3


    #//////////////////////////////////////////////////////////////////////////////
root.mainloop()

    #   Widgets with Command Callbacks

  #     * Button                * Spinbox
  #     * Checkbutton           * Scale
  #     * Radiobutton           * Scrollbar


#if __name__ == '__main__':
#    main()
