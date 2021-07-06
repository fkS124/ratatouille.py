import pygame as pg
import src.pygame_framework as pg_fr_w

"""
To use Ratatouille Framework you have to:
** Start method means that the method has to be called at the start of
the game and game loop method means that the method must be called inside
the loop **

ratatouille = Ratouille.init(display_surface)


# Commands : Start Methods
.new_button() # Creates a button
Guide:
.new_button(coordinates, font_surface, text, color_text,hovering_color_text, size, func, args)

.new_special_button() # Create a button using images
Guide:                           # image can be a loaded image or just a path
.new_special_button(coordinates, image, image_hover, size, func, args)

.pause_button() # Creates a Pause button
Guide:
.pause_button(coordinates, font_surface, text, size,func)

# Commands : Game Loop Methods
.show_fps()  # show current fps
Guide:
.show_fps(clock, font, coordinates, color, color_txt)

To make the framework work you have to use this architecture of project :
# at the start
- initializing the engine with .init()
- defining all your buttons and stuff

# game loop:
- ratatouille.update() -> update all your stuff

    # event loop:
        - ratatouille.handle_events(event)

- (OPTIONAL) : draw shapes with the ratatouille.draw."shape" -> 
"""

def test_func(arg1=None, arg2=None):
    print(f"Tested Successfully {arg1}, {arg2}")

def sum_(arg1=0, arg2=0):
    print(arg1 + arg2)


def main():

    screen = pg.display.set_mode((900, 600))
    pg.display.set_caption("Pygame Frame Work Working Example")
    running = True
    clock = pg.time.Clock()
    standard_font = pg.font.Font("assets_demo/Basic-Regular.ttf", 50)

    frame_work = pg_fr_w.init(screen)
    frame_work.new_button((200, 200), # coordinates
                          standard_font,  # font
                          "Button",  # text
                          (0, 0, 0),  # color text
                          (255, 255, 255),  # color hovering text
                          (25, 85, 120),  # color box
                          (120, 25, 58),  # color hovering box
                          (300, 100),  # size of the box
                          test_func,  # function to call when a click happen
                          (15, 15)  # args needed for the func
                          )
    frame_work.new_special_button(
        (500, 500), # coordinates
        "assets_demo/button1.png", # path of image 1
        "assets_demo/button2.png", # path of image 2
        (64, 64),
        sum_,
        (12, 65)
    )

    while running:

        for event in pg.event.get():
            
            frame_work.handle_events(event)
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        frame_work.update()

        frame_work.show_fps(clock, standard_font, (0, 0))
        clock.tick(60)
        pg.display.update()


if __name__ == "__main__":

    pg.init()

    main()

    pg.quit()
    raise SystemExit

        
