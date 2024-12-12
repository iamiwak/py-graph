import tkinter as tk

from const import *
from drawable import Drawable
from point import Point


class Line(Drawable):
    def __init__(self, canvas: tk.Canvas, start: Point, end: Point):
        super().__init__(canvas, LINE_SIZE, LINE_COLOR_NAME)
        self.__start = start
        self.__end = end

    def draw(self):
        self._canvas.create_line(
            self.__start.x, self.__start.y,
            self.__end.x, self.__end.y,
            width=self._size, fill=self._color
        )
