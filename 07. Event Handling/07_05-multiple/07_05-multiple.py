#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     08.08.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

root = Tk()

label1  = ttk.Label(root, text = 'Label 1')
label2  = ttk.Label(root, text = 'Label 2')

label1.pack()
label2.pack()


label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label'))#Кликаем на label1 (нажимаем на люьые кнопки мыши) и в консоли отображается "<ButtonPress> Label"
label1.bind('<1>', lambda e: print('<1> Label'))#Кликаем на левую кнопку на label1 и в консоли отображается "<1> Label" кликаем на другие кнопки мыши и отображается "<ButtonPress> Label"

root.bind('<1>', lambda e: print('<1> root'))#Кликаем на левую кнопку на label1 и в консоли отображается "<1> Label" и '<1> root' кликаем на другие кнопки мыши и отображается "<ButtonPress> Label"
                                             #Кликаем левую кнопку мыши в любую точку окна, но не на label1 и в консоли отображается '<1> root'

label1.unbind('<1>')#Кликаем на левую кнопку на label1 и в консоли отображается "<ButtonPress> Label" и '<1> root' кликаем на другие кнопки мыши и отображается "<ButtonPress> Label"
                                             #Кликаем левую кнопку мыши в любую точку окна, но не на label1 и в консоли отображается '<1> root'

label1.unbind('<ButtonPress>')#Кликаем на левую кнопку на label1 и в консоли отображается '<1> root' кликаем на другие кнопки мыши и ничего не происходит
                              #Кликаем левую кнопку мыши в любую точку окна и в консоли отображается '<1> root'

root.bind_all('<Escape>', lambda e: print("Escape!"))#Когда нажимаем клавишу "Esc", находясь в главном окне на консоли выводится "Escape!"

root.mainloop()


#if __name__ == '__main__':
#    main()
