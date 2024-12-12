import tkinter as tk
from tkinter import ttk
from typing import Callable

from const import *
from point import Point
from line import Line


class Editor:
    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR_NAME)
        self.__clear_button = tk.Button(self.__root, text=CLEAR_BUTTON_TEXT, command=self.__clear_canvas)
        self.__draw_mode_combobox = ttk.Combobox(self.__root, values=DRAW_MODES, state=COMBOBOX_STATE_TEXT)
        self.__start_point = None

        self.__draw_mode_func_dict = {
            DRAW_MODES[k]: v for k, v in enumerate([self.__draw_point, self.__draw_line])
        }

        self.__build_settings()

    def __clear_canvas(self):
        self.__canvas.delete('all')
        self.__start_point = None

    def __on_click(self, event):
        x, y = event.x, event.y

        draw_mode = self.__draw_mode_combobox.get()
        draw_func: Callable = self.__draw_mode_func_dict.get(draw_mode)
        # придумать, как прокидывать корректные данные по kwargs
        draw_func(x=x, y=y)

    def __build_settings(self):
        self.__root.title(EDITOR_NAME_TEXT)
        self.__root.resizable(False, False)
        self.__canvas.bind(LEFT_CLICK_KEY, self.__on_click)
        self.__canvas.pack()
        self.__clear_button.pack()

        self.__draw_mode_combobox.current(0)
        self.__draw_mode_combobox.pack()

    def __get_draw_mode(self):
        return DRAW_MODES[self.__draw_mode_combobox.current()]

    def __draw_point(self, x: int, y: int):
        Point(self.__canvas, x, y).draw()

    def __draw_line(self, x: int, y: int):
        point = Point(self.__canvas, x, y)
        if not self.__start_point:
            self.__start_point = point
            point.draw(True)
            return

        if x == self.__start_point.x and y == self.__start_point.y:
            return

        end_point = point
        Line(self.__canvas, self.__start_point, end_point).draw()
        self.__canvas.delete(TEMPORARY_POINT_TAG)
        self.__start_point = None

    def run(self):
        self.__root.mainloop()
