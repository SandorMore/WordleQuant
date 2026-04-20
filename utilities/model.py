wordFrequency : dict = {}
class Word:
    length:int
    word:str

    def __init__(self, word:str):
        self.length = 5
        self.word = word

    def check_for_letters(self, guess):
        for i in range(0, 5):
            if(guess[i] == self.word):
                pass