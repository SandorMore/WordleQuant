def submit(word, guess):
    guess = guess.upper()
    word = word.upper()

    colors = [None] * len(word)
    remaining = {}

    for i in range(len(word)):
        if word[i] == guess[i]:
            colors[i] = "g"
        else:
            remaining[word[i]] = remaining.get(word[i], 0) + 1

    for i in range(len(word)):
        if colors[i] is not None:
            continue
        if remaining.get(guess[i], 0) > 0:
            colors[i] = "y"
            remaining[guess[i]] -= 1
        else:
            colors[i] = "b"

    return colors