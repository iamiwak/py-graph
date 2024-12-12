import tkinter as tk

from const import *
from point import Point
from line import Line


class Editor:
    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR_NAME)
        self.__clear_button = tk.Button(self.__root, text=CLEAR_BUTTON_TEXT, command=self.__clear_canvas)
        self.__start_point = None

        self.__build_settings()

    def __clear_canvas(self):
        self.__canvas.delete('all')
        self.__start_point = None

    def __on_click(self, event):
        x = event.x
        y = event.y

        if self.__start_point is None:
            self.__start_point = Point(x, y)
            self.__canvas.create_oval(x - POINT_SIZE, y - POINT_SIZE, x + POINT_SIZE, y + POINT_SIZE, fill=LINE_COLOR_NAME)
        elif x == self.__start_point.x and y == self.__start_point.y:
            pass
        else:
            end_point = Point(x, y)
            Line(self.__start_point, end_point).draw(self.__canvas)
            self.__start_point = None

    def __build_settings(self):
        self.__root.title(EDITOR_NAME_TEXT)
        self.__root.resizable(False, False)
        self.__canvas.bind(LEFT_CLICK_KEY, self.__on_click)
        self.__canvas.pack()
        self.__clear_button.pack()

    def run(self):
        self.__root.mainloop()
