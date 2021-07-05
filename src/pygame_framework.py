import pygame as pg
import src.buttons as buttons


def init(surface: pg.Surface):
    return FrameWork(surface)


class FrameWork:

    def __init__(self,
                 screen: pg.Surface):

        self.screen, self.w, self.h = screen, screen.get_width(), screen.get_height()

        self.buttons = []

    def update(self):

        for button in self.buttons:
            button.update(self.screen)

    def handle_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_clicks(event.pos)

    def handle_clicks(self, pos: tuple[int, int, int]):
        for button in self.buttons:
            button.handle_click(pos)        

    def new_button(self, coordinates: tuple[int, int],
                         font: pg.font.Font,
                         text: str, 
                         color_text: tuple[int, int, int],
                         color_text_hover: tuple[int, int, int],
                         color: tuple[int, int, int],
                         color_hover: tuple[int, int, int], 
                         size: tuple[int, int],  # not sure about size
                         func=None,
                         args=None):
        self.buttons.append(buttons.Button(coordinates, font, text, color_text,
                                           color_text_hover,color, color_hover,
                                           size, func, args))

    def draw_random_shape(self, args):
        pass