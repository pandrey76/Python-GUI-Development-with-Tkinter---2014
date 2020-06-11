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

#Здесь мы научимся передавать информацию Tk о том где должен находится элемент.
#Позиционирование элементов в окне происходит за счёт Tk Geometry Manager.
#Здесь используется концепция Master и Slave элементов. Master элемент
#организован как контейнер, как главное окно или Frame элемент и он использует
#Geometry Manager для позиционирования дочерних (Slave) элементов,
#которые будут отображены в его границах.
#Для примера что делать если дочерний элемент занимает больше места, чем
#головное окно. Что будет происходить если пользователь будет развертывать
#или свёртывать головное окно. Для этого Geometry Manager управляет
#изменением всех master и slave элементов.
#В Tk присутствуют три типа Geometry managera. которые обеспечивают различные
#способы описания позиций элементов.

# Tk Geometry Managers
# Pack Geometry Manager
#    * Define edge of parent to pack widget master
#    * Example: widget.pack (side = RIGHT)

# Grid Geometry Manager
#   * Define row/column of 2-dimensional table in master
#   * Example:  widget.grid (row = 0, column = 1 )

# Place Geometry Manager
#    * Define relative or absolute x/y coordinates in master
#    * Example: widget.place (x = 200, y = 150)

#Если вы будете использовать два различных Geometry Manager для отображения
#виджетов может привести к ошибкам внутри библиотеки Tk и получить
#неопределённый результат.
def main():
    pass

if __name__ == '__main__':
    main()
