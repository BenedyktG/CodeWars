import re


def getCount(inputStr):
    vowels = list("aeiou")
    num_vowels = 0
    num_vowels = sum(inputStr.count(c) for c in vowels)

    print(num_vowels)


getCount("abracadabra")
