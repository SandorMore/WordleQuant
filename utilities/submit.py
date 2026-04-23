def submit(word, guess):
    colorArr = []
    guess = guess.upper()
    word = word.upper()
    for i in range(len(word)):
        if(word[i] == guess[i]):
            colorArr.append("g")
        elif(word[i] in guess and word[i] != guess[i]):
            colorArr.append("y")
        else:
            colorArr.append("b")

    return colorArr