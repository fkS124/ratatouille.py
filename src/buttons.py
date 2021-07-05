import pygame as pg


class Button:

    def __init__(self, 
                 coordinates: tuple[int, int],
                 font: pg.font.Font,
                 text: str, 
                 color_text: tuple[int, int, int],
                 color_text_hover: tuple[int, int, int],
                 color: tuple[int, int, int],
                 color_hover: tuple[int, int, int], 
                 size: tuple[int, int],  # not sure about size
                 func=None,  # default is None
                 args=None  # default is None
                 ): 

        # getting font
        self.font = font
        # rendering text with the normal color
        self.rendered_text = self.font.render(text, True, color_text)
        # rendering the text with the hover color
        self.rendered_text_hover = self.font.render(text, True, color_text_hover)

        # getting the rects to blit in the update method, centering the rect according to the button size
        self.rendered_text_rect = self.rendered_text.get_rect(center=(size[0]//2, size[1]//2))
        self.rendered_text_hover_rect = self.rendered_text_hover.get_rect(center=(size[0]//2, size[1]//2))

        self.surface = pg.Surface(size)
        self.surface.fill(color)
        self.rect = self.surface.get_rect(topleft=coordinates)

        self.color = color
        self.color_hover = color_hover
        self.func = func
        self.args = args

    def update(self, screen):
        
        # getting the coordinates of the mouse to check the hovering
        mo_coo = pg.mouse.get_pos()

        # checking for mouse hover
        if self.rect.collidepoint(mo_coo):
            self.surface.fill(self.color_hover)
            self.surface.blit(self.rendered_text_hover, self.rendered_text_hover_rect)
        else:
            self.surface.fill(self.color)
            self.surface.blit(self.rendered_text, self.rendered_text_rect)

        screen.blit(self.surface, self.rect)

    def handle_click(self, pos):

        # detecting clicks
        if self.rect.collidepoint(pos):
            # checking if a function is assigned to the button
            if self.func is not None:
                # checking if there are some args to put in the function
                if self.args is not None:
                    self.func(self.args)
                else:
                    self.func()
