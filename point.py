import tkinter as tk

from const import *
from drawable import Drawable


class Point(Drawable):
    def __init__(self, canvas: tk.Canvas, x: int, y: int):
        super().__init__(canvas, POINT_SIZE, POINT_COLOR_NAME)
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def draw(self, is_temp: bool = False):
        self._canvas.create_oval(
            self.__x - self._size, self.__y - self._size,
            self.__x + self._size, self.__y + self._size,
            fill=self._color, tags=TEMPORARY_POINT_TAG if is_temp else ""
        )
