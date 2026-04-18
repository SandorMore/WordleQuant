import pygame as pg
from utilities.model import Word 
from utilities.pygameutil import Reader

reader = Reader("assets/words.txt")
word = Word(5)

def main():
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    while True:
       screen.fill(color = "green")
       
       for event in pg.event.get():
          if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
       
       pg.display.flip()
    
       clock.tick(60)

if __name__ == "__main__":
    reader.printAllWords()
    main()
