print("Welcome to the ASTERISK MACHINE...")
inputAsterisk = 0
numAsterisk = 0
while True:
    inputAsterisk = input("How many do you want? ")
    if isinstance(inputAsterisk, int):
#    numAsterisk = int(inputAsterisk)
        printTree(inputAsterisk)
        keepPlaying = raw_input("Do you want more? (y)/(n) ")
        if keepPlaying == "y":
            continue
        elif keepPlaying == "n":
            print("see you!!")
            break
        else :
            print "What?"
            print "I will give you some more..."
            continue
     else :
         print("What?! Give me a number!")
        continue

def printTree(num):
    print(num * '*')
