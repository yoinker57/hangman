from playAlone import playAlone
from playComputer import playComputer


def main():
    answer = 'y'
    while answer == 'y':
        print('1) Play alone')
        print("2) Let's computer solve your world")
        flag = False
        while not flag:
            try:
                a = int(input())
                flag = True
            except:
                print('write 1 or 2')
                flag = False
        if a == 1:
            playAlone()
        else:
            ans = int(input(
                'Do you want to give a word (1) or computer can choose the random world (2)? '))
            if ans == 1:
                word = input('give word: ')
                playComputer(word)
            else:
                playComputer()
        answer = input('Do you want to play again? (y/n) ')


main()
