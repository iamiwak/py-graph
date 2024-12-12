from typing import Final

from draw_mode import DrawMode

LEFT_CLICK_KEY: Final[str] = '<Button-1>'
TEMPORARY_POINT_TAG: Final[str] = "temp"

BACKGROUND_COLOR_NAME: Final[str] = 'white'
LINE_COLOR_NAME: Final[str] = 'black'
POINT_COLOR_NAME: Final[str] = 'black'
COMBOBOX_STATE_TEXT: Final[str] = 'readonly'

CLEAR_BUTTON_TEXT: Final[str] = 'Очистить'
EDITOR_NAME_TEXT: Final[str] = 'Редактор'

DRAW_MODES = [DrawMode.POINT.value, DrawMode.LINE.value]
DRAW_MODE_POINT_IDX = 0
DRAW_MODE_LINE_IDX = 1

CANVAS_WIDTH: Final[int] = 400
CANVAS_HEIGHT: Final[int] = 300
LINE_SIZE: Final[int] = 4
POINT_SIZE: Final[float] = LINE_SIZE / 2