class Reader:
    wordList : list = []
    def __init__(self, file:str):
        with open(file, "r") as f:
            self.wordList = f.readlines()

    def printAllWords(self):
        print("The words are")
        for i in self.wordList:
            print(i)
    
    def addFreq(self, dict:dict):
        for i in self.wordList:
            dict[i] = 1.0