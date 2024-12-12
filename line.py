import tkinter

from const import *
from point import Point


class Line:
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end

    def draw(self, canvas: tkinter.Canvas):
        canvas.create_line(self.__start.x, self.__start.y, self.__end.x, self.__end.y, width=LINE_SIZE, fill=LINE_COLOR_NAME)
