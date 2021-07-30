import readline
# 
# $pip install pyreadline
#
from MyCompleter import MyCompleter
#from fast_autocomplete import AutoComplete

class test:

    def __init__(self):
        self.keywords = ["hello", "hi", "how are you", "goodbye", "great", "view"]

    def in1(self, text):
        completer = MyCompleter(self.keywords)
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')
        for kw in self.keywords:
            readline.add_history(kw)

        thing = input(text)
        readline.clear_history()
        if thing not in self.keywords:
            self.keywords.append(thing)
        return thing

    def setup2(self):
        readline.parse_and_bind('tab:complete')
        input("input item")