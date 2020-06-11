#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     25.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk

class ProgressBarWidget :

    def __init__(self):
        self._root = Tk()
        self._progressbar_interminate = ttk.Progressbar(self._root,
                                    orient = HORIZONTAL, length = 200)
        self._progressbar_interminate.config(mode = 'indeterminate')
        self._start_button = ttk.Button(self._root, text='Start progress!',
                                                 command = self.StarnProgress)

        self._stop_button = ttk.Button(self._root, text='Stop progress!',
                                                 command = self.StopProgress)

        self._progressbar_determinate = ttk.Progressbar(self._root,
                                    orient = HORIZONTAL, length = 200)
        self._progressbar_determinate.config( mode = 'determinate',
                    maximum = 11.0,
                    value = 4.2 #Устанавливаем начальное значение
                    )

        self._step_button = ttk.Button(self._root, text='Step progress!',
                                                 command = self.StepProgress)

        self._value = DoubleVar()
        self._progressbar_determinate.config(variable=self._value)

        self._scale = ttk.Scale(self._root, orient=HORIZONTAL, length = 400,
                                   variable=self._value, from_=0.0, to=11.0)

    def main(self):

        self._progressbar_interminate.pack()
        self._start_button.pack()
        self._stop_button.pack()
        self._progressbar_determinate.pack()
        self._step_button.pack()
        self._scale.pack()

        #Прибавляется к текущему значению ещё 5 шагов.
        #self._progressbar_determinate.step(5)

        #устанавливаем значение для ползунка
        #self._scale.set(4.2)
        self._root.mainloop()

    def StarnProgress(self):
        self._progressbar_interminate.start()

    def StopProgress(self):
        self._progressbar_interminate.stop()

    def StepProgress(self):
        self._progressbar_determinate.step()

if __name__ == '__main__':
    progress = ProgressBarWidget()
    progress.main()
