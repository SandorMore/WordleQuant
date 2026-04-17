class Reader:

    wordList : list = []
    
    def __init__(self, file:str):
        with open(file, "r") as f:
            self.wordList.append(f.read())

    def printAllWords(self):
        for i in self.wordList:
            print(i)