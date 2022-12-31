#! /usr/bin/python3

import shutil
import os

class Exit(RuntimeError):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return f"exited pyedit with {self.args[0]}"


class PyEdit:
    def __init__(self, file=None):
        self.file = file
        self.runPyEdit()

    def normalMode(self):
        uin = input("> ")
        if uin == ":q":
            raise Exit

    def runPyEdit(self):
        while True:
            try:
                if not self.file:
                    self.displayWelcome()
                self.normalMode()
            except Exit as e:
                break

    def displayWelcome(self):
        os.system('cls')
        c_len = shutil.get_terminal_size().columns
        r_len = shutil.get_terminal_size().lines
        print('~\n' * ((r_len // 2)-1), end='')
        print(f"~{'PyEdit v 0.1'.center(c_len-1)}")
        print(f"~{'this editor uses vim commands'.center(c_len-1)}")
        print('~\n' * ((r_len // 2)-2), end='')

def main():
    test = PyEdit()

if __name__ == "__main__":
    main()
