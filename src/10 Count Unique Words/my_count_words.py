import re
import collections


def count_words(file):
    with open(file, "r") as f:
        words = re.findall(r"[A-Za-z'-]\w+", f.read())
        for index, word in enumerate(words):
            words[index] = word.lower()
    # This is cool!
    words = collections.Counter(words)
    print("There are " + str(len(words)) + " total words")
    for word in words.most_common(20):
        print("Word " + str(word[0]) + " occurs " + str(word[1]) + " times")


count_words("src/10 Count Unique Words/shakespeare.txt")
