from encodings import utf_8
import random
import os


def printArray(array):
    for i in array:
        print(i, end=" ")
    print()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def firstSelection(array, n):
    tab = []
    for i in array:
        if len(i) == n:
            tab.append(i)
    return tab


def numberOfLetter(words, used):
    dict = {}
    for word in words:
        for char in word:
            if not char in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    for char in used:
        dict[char] = 0
    return dict


def checkLetters(word, array):
    for i in range(len(array)):
        if array[i] != '_':
            if word[i] != array[i]:
                return False
    return True


def letter(letter, array, words):
    words2 = []
    for word in words:
        if checkLetters(word, array):
            words2.append(word)
    return words2


def letterRemove(letter, words):
    words2 = []
    for word in words:
        if letter not in word:
            words2.append(word)
    return words2


def playComputer(word=1):
    f = open("slowa.txt", mode='r', encoding='utf-8')
    words = f.read().split('\n')
    f.close()
    if word == 1:
        word = random.choice(words)
    n = len(word)

    array = ['_'] * n
    use_chars_tab = []
    words = firstSelection(words, n)
    flag = False
    counter = 6
    dict = {}
    while counter > 0 and not flag:
        dict = numberOfLetter(words, use_chars_tab)
        character = max(dict, key=dict.get)
        print(character)
        use_chars_tab.append(character)
        j = 0
        flag2 = False
        for i in range(len(word)):
            if character == word[i]:
                array[i] = character
                n -= 1
                flag2 = True
            j += 1
        if flag2 == False:
            counter -= 1
            words = letterRemove(character, words)
        words = letter(character, array, words)
        if n == 0:
            flag = True
        clear()
        printArray(array)
        print('Computer used: ', end='')
        printArray(use_chars_tab)
        print(f"Computer have {counter} tries")
        if flag:
            print("Computer win!")
        else:
            ("Computer lose!")
        print(word)

