class Reader:
    wordList : list = []
    
    def __init__(self, file:str):
        with open(file, "r") as f:
            self.wordList.append(f.read())

    def printAllWords(self):
        print("The words are")
        for i in self.wordList:
            print(i)
    
    def addFreq(self, dict:dict):
        for i in self.wordList:
            dict[i] = 1.0