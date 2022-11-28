import random

def generate_passphrase(file, num_words):
    words = []
    password = ""
    with open(file, "r") as f:
        raw = f.readlines()[2:7778]
        for line in raw:
            words.append(line.split()[1])
    for _ in range(0, num_words):
        pick = random.randint(0, len(words)-1)
        password = password + " " + words[pick]
    print(password)


generate_passphrase("src/11 Generate a Password/diceware.wordlist.asc", 10)
