import sys
import pygame as pg
import random as rnd
from utilities.submit import submit
from utilities.model import Word, Slot 
from utilities.pygameutil import Reader
from utilities.model import wordFrequency

reader = Reader("assets/words.txt")
slotList : list = []
word = Word(str(rnd.choice(reader.wordList)))
wordingOffsetLeft:int = 18
wordingOffsetTop:int = -7
fontColor = tuple((0,0,0))

def DrawSlots(s:pg.display):    
    if not slotList:
        left, top = 100, 70
        initialLeft = left

        for row in range(6):
            for col in range(5):
                slotList.append(Slot(left, top, 100, 100))
                left += 130

            left = initialLeft
            top += 110

    for slot in slotList:
        pg.draw.rect(s, "black", slot.rect, 3)

def main():
    pg.init()
    pg.font.init()

    running:bool = True

    font:pg.font = pg.font.SysFont("Comic Sans MS", 80)
    print(word.randomWord)
    screen = pg.display.set_mode((1280, 860))
    clock = pg.time.Clock()
    guess:str = ""
    text_surface = font.render("", True, fontColor)
    
    responseArr = []

    print(guess)
    while running:
        screen.fill(color = "gray") 
        
        DrawSlots(s=screen)

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.TEXTINPUT:
                if len(guess) < 5:
                    guess += event.text 
                    for i in range(len(guess)):
                        slotList[i].letter = guess[i]
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    guess = guess[:-1]  
                elif event.key == pg.K_ESCAPE:
                    running = False
                elif event.key == pg.K_RETURN:
                    if(len(guess) == 5):
                        if(guess.upper() not in reader.wordList):
                            print("Not an accepted word")
                            
                        elif(guess.upper() in reader.wordList):
                            responseArr = submit(word=word.randomWord, guess=guess)
                            for i in range(len(responseArr)):
                                print(responseArr[i])
                        if guess.upper() == word.randomWord:
                            print("You won")
                            pg.QUIT
                            raise SystemExit

        
        if(len(guess) >= 1):
            for i in range(len(guess)):
                text_surface = font.render(slotList[i].letter.upper(), True, fontColor) 
                screen.blit(text_surface, (slotList[i].rect.left + wordingOffsetLeft, slotList[i].rect.top + wordingOffsetTop))
        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__": 
    reader.addFreq(wordFrequency)
    print("Added word sucessfully")
    #reader.printAllWords()
    main()
