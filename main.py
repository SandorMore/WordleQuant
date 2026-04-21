import pygame as pg
from utilities.model import Word, Slot 
from utilities.pygameutil import Reader
from utilities.model import wordFrequency

reader = Reader("assets/words.txt")
word = Word(5)
slotList : list = []
def DrawSlots(s:pg.display):
    
    left, top = 100, 70
    initialLeft = 100

    for i in range(6):
        for i in range(5):
            pg.draw.rect(s, "black", [left, top, 100, 100], 3)
            slotList.append(Slot(left,top,100,100))
            left += 130

        left = initialLeft
        top += 110
       
       
def main():
    pg.init()
    screen = pg.display.set_mode((1280, 860))
    clock = pg.time.Clock()
    printed:bool = False
    while True:
        screen.fill(color = "gray")

        DrawSlots(s=screen)
        if not printed:
            print(len(slotList))
            printed = True

        for event in pg.event.get():
          if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
       
        pg.display.flip()
    
        clock.tick(60)

if __name__ == "__main__": 
    reader.addFreq(wordFrequency)
    print("Added word sucessfully")
    main()
