from colors import colors
import sys
def hangman():
    password = ["n", "e", "v", "e", "r", "g", "o", "n", "n", "a", "g", "i", "v", "e", "y", "o", "u", "u", "p"]
    answers = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_" ]
    stage = 1
    while True:
        print()
        for i in answers:
            print(colors.YELLOW, i, colors.BLACK, end="")
        print("\n")
        stages(stage)
        char = input(">")
        if password.__contains__(char):
            counter = 0
            for i in password:
                if i == char:
                    answers[counter] = i
                counter += 1
        else:
            stage += 1
        if answers == password:
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