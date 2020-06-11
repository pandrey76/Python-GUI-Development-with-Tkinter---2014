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

    #       Callbacks vs. Events

    #    * Callbacks only available for specific actions
    #    * Tkinter can bind to events with specific handlers
    #    * There's a wide variety of event handlers


    #       Tk Event Types

    #   * ButtonPress       * KeyPress
    #   * ButtonRelease     * KeyRelease
    #   * Enter             * FocusIn
    #   * Leave             * FocusOut
    #   * Motiong

    #   http://www.tkdocs.com/tutorial/canvas.html#bindings


root = Tk()
   #Блок №1 /////////////////////////////////////////////////////////////////////

#def key_press(event):
                                                #При нажатии на клавишу 'п'     #При нажатии на клавишу 'a' (в английской раскладке)    #При нажатии на клавишу 'a' F1
#    print('type: {}'.format(event.type))        # 2 (Собыиие KeyPress)          #2                                                      #2
#    print('widget: {}'.format(event.widget))    # . (Root Window)               #.                                                      #.
#    print('char: {}'.format(event.char))        # п                             #a                                                      #
#    print('keysym: {}'.format(event.keysym))    # idiaeresis                    #a                                                      #F1
#    print('keycode: {}'.format(event.keycode))  # 71                            #65                                                     #112

#root.bind('<KeyPress>', key_press)
    #//////////////////////////////////////////////////////////////////////////////
                #   Keyboard Events
#    ________________________________________________________________________
#   |  Event Format                |   Event Describtion                     |
#   |______________________________|_________________________________________|
#   | <Key>, <KeyPress>            |   User pressed any key.                 |
#   |______________________________|_________________________________________|
#   | <KeyPress-Delete>            |   User pressed Delete key.              |
#   |______________________________|_________________________________________|
#   | <keyRelease-Right>           |   User released Right Arrow key.        |
#   |______________________________|_________________________________________|
#   | a, b, c, 1, 2, 3, etc... and |   User pressed a "printable" key.       |
#   | <space>, <less>              |                                         |
#   |_____________________________ |_________________________________________|
#   | <Shift_L>, <Control_R>, <F5>,|   User pressed a "special" key.         |
#   | <Up>                         |                                         |
#   |______________________________|_________________________________________|
#   | <Return>                     |   User pressed the Enter key.           |
#   |______________________________|_________________________________________|
#   | <Control-Alt-Next>           |   User pressed Ctrl+Alt+Page Down keys. |
#   |______________________________|_________________________________________|


   #Блок №2 /////////////////////////////////////////////////////////////////////
#def shortcut(action):
#    print ( action )

    #При запуске данного блока программа выведет два значения "Copy" и "Paste" и при нажатии на кнопки ничего происходить не будет.
    #Так происходит потому что когда программа первый раз запускается она ставит соответствие свойства "command" и функции,
    #она также запускает функцию при каждом соответствии bind и функциии, далее устанавливает возвращаемое значение для функции,
    #т.к. функция shortcut ничего не возвращает, то значение bind становится равным None. Поэтому при нажатии на кнопки ничего происходить не будет.
#root.bind( '<Control-c>', shortcut("Copy"))
#root.bind( '<Control-v>', shortcut("Paste"))
    #//////////////////////////////////////////////////////////////////////////////

   #Блок №3 /////////////////////////////////////////////////////////////////////
def shortcut(action):
    print ( action )

root.bind( '<Control-c>', lambda e: shortcut("Copy"))
root.bind( '<Control-v>', lambda e: shortcut("Paste"))
    #//////////////////////////////////////////////////////////////////////////////

root.mainloop()
