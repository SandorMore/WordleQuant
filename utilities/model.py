import pygame as pg

wordFrequency : dict = {}

class Word:
    length:int
    randomWord:str

    def __init__(self, word:str):
        self.length = 5
        self.randomWord = word

    def check_for_letters(self, guess):
        for i in range(0, 5):
            if(guess[i] == self.word):
                pass
            
class Slot:
    rect:pg.Rect
    letter:chr

    def __init__(self, left:int, top:int, width:int, height:int):
        self.rect = pg.Rect(left,top,width,height)
