class Word:
    length:int
    word:str
    def __init__(self, length):
        length = 5

    def check_for_letters(self, guess):
        for i in range(0, 5):
            if(guess[i] == self.word):
                print("Van")