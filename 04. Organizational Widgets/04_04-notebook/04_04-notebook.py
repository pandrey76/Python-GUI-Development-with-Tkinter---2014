#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     26.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    notebook = ttk.Notebook(root)
    notebook.pack()
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text = 'One')#отобразили первый Tab элемент
    notebook.add(frame2, text = 'Two')#отобразили второй Tab элемент
    ttk.Button(frame1, text='Click Me').pack()
    frame3 = ttk.Frame(notebook)
    notebook.insert(1,frame3, text='Three')#Добавляем третий элемент между
                                           #первым и вторым
    notebook.forget(1)#не удаляем элемент, но убираем из изображения
    notebook.add(frame3,text = 'Three')#Добавляем третий элемент после второго
    print(notebook.select())#.18082192.18082224

    print(notebook.index(notebook.select()))#0

    notebook.select(2)#Будет выделен 3 Tab элемент

    notebook.tab(1, state='disabled')#Второй Tab элемент не доступен
    notebook.tab(1, state='hidden')#Второй Tab элемент скрыт и не отображается
    notebook.tab(1, state='normal')#Второй Tab элемент пришёл
                                   #в исходное состояние

    print(notebook.tab(1, 'text'))#Two

    print(notebook.tab(1))#{'padding': [0],
                                  #'sticky': 'nsew',
                                  #'compound': 'none',
                                  #'text': 'Two',
                                  #'underline': -1,
                                  #'state': 'normal',
                                  #'image': ''}

    root.mainloop()

class NotebookImpl:
    """
    """
    def __init__(self):
        """
        """
        self._root = Tk()
        self._notebook = ttk.Notebook(self._root)
        self._frame1 = ttk.Frame(self._notebook)
        self._frame2 = ttk.Frame(self._notebook)
        self._notebook.add(self._frame1, text = 'One')
        self._notebook.add(self._frame2, text = 'Two')
        ttk.Button(self._frame1, text = 'Click Me').pack()
        self._frame3 = ttk.Frame(self._notebook)
        self._state_tab_button = ttk.Button(self._root,
                                                    text = 'Change Tab State')
        self._state_tab_button.config(command = self.ChangeState)
        self._select_tab_button = ttk.Button(self._root,
                                                    text = 'Select Tab State')
        self._select_tab_button.config(command = self.SelectTab)

        self._forgget_checkbutton_value = BooleanVar()#Переменную можно менять
                                                      #только методом "set".
        self._forgget_checkbutton = ttk.Checkbutton(self._root,
                        text = "Insert/Forget tab", command = self.ForgetTab)
        self._forgget_checkbutton.config(
                                    variable = self._forgget_checkbutton_value,
                                    onvalue = True, offvalue = False)

    def main(self):
        """
        """
        self._notebook.pack()
        self._select_tab_button.pack()
        self._state_tab_button.pack()
        self._forgget_checkbutton.pack()
        self._forgget_checkbutton_value.set(False)#начальное положение CheckBox
        self._root.mainloop()

    def ChangeState(self):
        """
        Метод берет текущий выделенный tab элемент и меняет его сосотяние, но
        при этом когда сосотояние "disable" элемент не может быть выделен,
        поэтому первый элемент становится недоступным и автоматически выделяется
        второй элемент, который также после нажатия на кнопку становится
        недоступным и после третьего нажатия происходит системная ошибка т.к.
        не одного tab элемента выделеть нельзя.
        """

        tab_states = ['disabled', 'hidden', 'normal']
        try:
            current_tab_index = self._notebook.index(self._notebook.select())
        except :
            current_tab_index = 0
        current_state_index = tab_states.index(
                                self._notebook.tab(current_tab_index, 'state')
                                              )
        current_state_index += 1
        current_state_index %= len(tab_states)
        self._notebook.tab(current_tab_index,
                                        state = tab_states[current_state_index])

    def SelectTab(self):
        """
        """
        current_tab_index = self._notebook.index(self._notebook.select())
        current_tab_index += 1
        current_tab_index %= len(self._notebook.tabs())
        self._notebook.select(current_tab_index)

    def ForgetTab(self):
        """
        """
        if self._forgget_checkbutton_value.get() == True :
            self._notebook.insert(1,self._frame3, text='Three')

            #Это не обязательный код, переменная сама устанавливается в нужное
            #значение из элемента управления
            #self._forgget_checkbutton_value.set(True)

        else:
            self._notebook.forget(1)

            #Это не обязательный код, переменная сама устанавливается в нужное
            #значение из элемента управления
            #self._forgget_checkbutton_value.set(False)



if __name__ == '__main__':
    notebook_impl = NotebookImpl()
    notebook_impl.main()
    #main()
