import tkinter as tk

class Drawable:
    def __init__(self, canvas: tk.Canvas, size: int | float, color: str):
        self._canvas = canvas
        self._size = size
        self._color = color

    def draw(self):
        raise NotImplementedError("Drawable.draw")