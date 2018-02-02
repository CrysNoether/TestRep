import random
import readline
print("Guess the number!")
#print(compNum)=
attempts = 0
globalAttemps = 0
compNum = random.randint(1,10)
numList = [compNum]
#print(len(numList))
while True:
    guessedNum = eval(raw_input('Choose a number between 1 and 10: '))
    print(guessedNum)
    esEntero = isinstance(guessedNum, int)
    if esEntero != True:
        print('That is not a number! Try again: ')
    else:
        attempts += 1
        if guessedNum < 1 or guessedNum > 10:
            print('Between 1 and 10! Try again: ')
        elif guessedNum < compNum:
            print('Bigger than ',guessedNum, 'Try again: ')
        elif guessedNum > compNum:
            print('Smaller than ',guessedNum,'Try again: ')
        else:
            globalAttemps += attempts
            print('FOUND!')
            print('Congratulations! You got it after' ,attempts, ' attempts')
            seguir = raw_input('Wanna keep playing?: y/n ')
            if seguir == "n":
                print('See you!')
                a = len(numList)
                b = globalAttemps
                accuracy = (a / b * 100)
                print('You have got a' ,accuracy, "per cent accuracy")
                break
            else:
                attempts = 0
                compNum = random.randint(1,10)
                a = len(numList)
                numList.append(compNum)
#                print(a)
                b = globalAttemps
#                print(b)
                accuracy = (a / b * 100)
                print('You have got a' ,accuracy, "per cent accuracy")
                continue
