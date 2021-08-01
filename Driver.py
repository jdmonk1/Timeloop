# Puzzles.hangman()
from subprocess import check_output
file = open("output.txt", 'r+')
try:
    import time
    #time.sleep(5)
    file.write("test")
    import Puzzles
    from mainGame import Game
    file.write("maingame") 
    g = Game()
    g.begin()
except Exception as e:
    #time.sleep(5)
    file.write(str(e))
    print(str(e))
    file.close()
