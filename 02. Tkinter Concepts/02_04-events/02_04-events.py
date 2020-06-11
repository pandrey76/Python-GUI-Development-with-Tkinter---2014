#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     11.07.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Handling User Events
 #When Event Occurs              Execute Handler Code
    #* <ButtonPress>                * handle_buttonpress()
    #* <Key>                        * handle_key()
    #* <Leave>                      * handle_leave()
    #* <Motion>                     * handle_motion()
    #* <Configure>                  * handle_configure()

#                   root.mainloop()
#                           |
#                           |
#                          \/
#                      Event Loop
#   Event Loop работает по принципу очереди, т.е. пока не отработает первое
#действие, обработка второго не начнётся.

#Configuring Event Handlers
#   * Command callbacks
#       Avialable for interactive widgets that produce events
#       Configure by setting widget's "command" property
#   * Event bindings
#       Used for events that do not have a command callback
#       Configure by using widget's "bind" method
# Как пример Lable не имеет "command" property так как не ждёт никакой реакции
#на действие

def main():
    pass

if __name__ == '__main__':
    main()
