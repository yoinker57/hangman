from encodings import utf_8
import random
import os

def printArray(array):
    for i in array:
        print(i, end = " ")
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def playAlone():
    answer = 'y'
    while answer == 'y':
        clear()
        f = open("slowa.txt", mode='r', encoding='utf-8')
        words = f.read().split('\n')
        f.close()
        word = random.choice(words)
        n = len(word)
        array = ['_']*n
        use_chars_tab = []
        printArray(array)
        counter = 6
        flag = False
        while counter > 0 and not flag:
            character = input('Give a character: ')
            if character in use_chars_tab:
                print('You used this character!')
            else:
                use_chars_tab.append(character)
                j = 0
                flag2 = False
                for i in range (len(word)):
                    if character == word[i]:
                        array[i] = character
                        n -= 1
                        flag2 = True
                    j += 1
                if flag2 == False:
                    counter -= 1
                if n == 0:
                    flag = True
                clear()
                printArray(array)
                print('You used: ', end = '')
                printArray(use_chars_tab)
                print(f"You have {counter} tries")
        if flag:
            print("You win!")
        else:
            ("You lose!")
        print(word)
        answer = input('Do you want to try again: (y/n) ')



