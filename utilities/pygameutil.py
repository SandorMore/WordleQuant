import pygame as pg

class Game:
    remainingGuesses:int
    alreadyGuessed:bool

    letters:dict = {}

    def __init__(self):
        self.remainingGuesses = 6
        self.alreadyGuessed = False

    def guess(self):
        if self.alreadyGuessed:
            print("Already guessed")
        