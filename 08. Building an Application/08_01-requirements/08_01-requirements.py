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
#http://www.explorecalifornia.org


#         Survey Form Requirements: Part 1
#   1. It will display a logo and instructions to user
#   2. It will have user input fields for:
#       * Name
#       * Email address
#       * Multiline comments
#   3. It will have two buttons: Submit and Clear.

#         Survey Form Requirements: Part 2
#   4. Pressing Submit will:
#       * Print contents of input field to the concole.
#       * Empty content of input field.
#       * Notify the user that comments were submited.
#   5. Pressing Clear will:
#       * Empty the input fields.

#       * Email address
#       * Multiline comments
#   3. It will have two buttons: Submit and Clear.

class Feedback:

    def __init__(self, master):
        pass
def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == '__main__':
    main()
