from colors import colors
import sys
from os import system, name
def hangman():
    system('cls')
    password = ["n", "e", "v", "e", "r", "g", "o", "n", "n", "a", "g", "i", "v", "e", "y", "o", "u", "u", "p"]
    answers = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_" ]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    incorrect = []
    stage = 1
    while True:
        print()
        x = 1
        for i in answers:
            print(colors.YELLOW, i, colors.BLACK, end="")
            if x == 5 or x == 10 or x == 14 or x == 17:
                print("   ", end="")
            x += 1
        print("\t\tGuesses: ", end="")
        for i in alphabet:
            if (answers.__contains__(i)):
                print(colors.GREEN + i + colors.BLACK, end = " ")
            elif (incorrect.__contains__(i)):
                print(colors.RED + i + colors.BLACK, end=" ")
            else:
                print(i, end=" ")
        print("\n")
        stages(stage)
        char = input(">")
        if not alphabet.__contains__(char):
            system('cls')
            print(colors.BLUE + "You must enter a single character" + colors.BLACK)
            
        elif incorrect.__contains__(char):
            system('cls')
            print(colors.BLUE + "You've already guessed that letter, and it was incorrect." + colors.BLACK)
        elif answers.__contains__(char):
            system('cls')
            print(colors.BLUE + "You've already guessed that letter, and it was correct" + colors.BLACK)
        else:
            if password.__contains__(char):
                counter = 0
                for i in password:
                    if i == char:
                        answers[counter] = i
                    counter += 1
            else:
                stage += 1
                incorrect.append(char)
            system('cls')
            if answers == password:
                x = 1
                for i in answers:
                    print(colors.YELLOW, i, colors.BLACK, end="")
                    if x == 5 or x == 10 or x == 14 or x == 17:
                        print("   ", end="")
                    x += 1
                print()
                stages(stage)
                print("\n************************\nYOU WIN!!!\n************************")
                sys.exit()


def stages(stage):
    if stage == 1:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||")
        print("||         ||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 2:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||         ")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 3:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||        .-`--'.")
        print("||       //Y .  ")
        print("||      //         ")
        print("||     //           ")
        print("||                     ")
        print("||")
        print("||")
        print("||")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 4:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||        .-`--'.")
        print("||       //Y . . Y\\ ")
        print("||      //         \\")
        print("||     //           \\")
        print("||                     ")
        print("||")
        print("||")
        print("||")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 5:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||        .-`--'.")
        print("||      //Y . . Y\\ ")
        print("||     //  |   |  \\")
        print("||    //   | . |   \\")
        print("||   ')    |   |    (`")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 6:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||        .-`--'.")
        print("||      //Y . . Y\\ ")
        print("||     //  |   |  \\")
        print("||    //   | . |   \\")
        print("||   ')    |   |    (`")
        print("||         ||")
        print("||         || ")
        print("||         || ")
        print("||         || ")
        print("||        / |  ")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
    elif stage == 7:
        print(".__________..")
        print("|._________))")
        print("||         ||")
        print("||         ||.-''.")
        print("||         |/  _  \\ ")
        print("||         ||  `/,|")
        print("||         (\\\\`_.'")
        print("||        .-`--'.")
        print("||      //Y . . Y\\ ")
        print("||     //  |   |  \\")
        print("||    //   | . |   \\")
        print("||   ')    |   |    (`")
        print("||         ||'||")
        print("||         || ||")
        print("||         || ||")
        print("||         || ||")
        print("||        / | | \ ")
        print("|||||||||||||||||||")
        print("|||||||||||||||||||")
        print("\n************************\nYOU LOST!!!\n************************")
        sys.exit()
