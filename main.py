import pygame as pg

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    while True:
       screen.fill(color = "purple")
       pg.display.flip()
       clock.tick(60)
if __name__ == "__main__":
 main()
