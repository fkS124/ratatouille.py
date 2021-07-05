import pygame as pg
import src.pygame_framework as pg_fr_w

"""
To use Ratatouille Framework you have to:

Ratatouille = Ratouille.init(display_surface)
# Commands
.new_button() # Creates a button
Guide:
.new_button( coordinates, font_surface, text, color_text,hovering_color_text, size,func)

.pause_button() # Creates a Pause button 
Guide:
.pause_button(coordinates, font_surface, text, size,func)


"""

def test_func(arg1=None, arg2=None):
    print(f"Tested Successfully {arg1}, {arg2}")


def main():

    screen = pg.display.set_mode((900, 600))
    pg.display.set_caption("Pygame Frame Work Working Example")
    running = True

    frame_work = pg_fr_w.init(screen)
    frame_work.new_button((200, 200), # coordinates
                          pg.font.Font("assets_demo/Basic-Regular.ttf", 50),  # font
                          "Button",  # text
                          (0, 0, 0),  # color text
                          (255, 255, 255),  # color hovering text
                          (25, 85, 120),  # color box
                          (120, 25, 58),  # color hovering box
                          (300, 100),  # size of the box
                          test_func,  # function to call when a click happen
                          (15, 15)  # args needed for the func
                          )

    while running:

        for event in pg.event.get():
            
            frame_work.handle_events(event)
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        frame_work.update()

        pg.display.update()


if __name__ == "__main__":

    pg.init()

    main()

    pg.quit()
    raise SystemExit

        
