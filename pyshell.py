#! /usr/bin/python3

from ftree import Directory
from ftree import File

class UsrErr(RuntimeError):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return f"{self.args[0]}"

class Shell:
    def __init__(self):
        self.root = Directory("/", None)
        self.commands = {'ls': self.showAllFiles, 
                         'mkdir': self.createDirectory,
                         'touch': self.createFile,
                         'cd': self.changeDirectory,}
        self.pwd_s = [self.root]
        self.env = {}

    def raise_error(self, err_msg):
        raise UsrErr(err_msg) 

    def showAllFiles(self):
        c = self.pwd_s[-1].getChildren()
        for i in range(len(c)):
            print(c[i].getName(), end="  ")
            if i == len(c) - 1:
                print()

    def createDirectory(self, dir_name: str):
        dir_name = Directory(dir_name, self.pwd_s[-1])
        self.pwd_s[-1].appendChildren(dir_name)

    def createFile(self, file_name: str):
        new_file = File(file_name, self.pwd_s[-1])
        self.pwd_s[-1].appendChildren(new_file)

    def changeDirectory(self, target_dir):
        match = None
        for ch in self.pwd_s[-1].getChildren():
            if ch.getName() == target_dir:
                match = ch
                break
        if not match:
            self.raise_error(f"cd: no such file or directory: {target_dir}")
        self.pwd_s.append(match)

    def getCurrDir(self):
        pwd = "/"
        if len(self.pwd_s) > 1:
            for i in range(1, len(self.pwd_s)):
                pwd += self.pwd_s[i]
                if i == len(self.pwd_s) - 1:
                    break
                pwd += '/'
        
        return pwd
    
    def add_to_env(self, path, dir):
        self.env[path] = dir.getChildren()        

    def acceptCommands(self):
        while True:
            try: 
                args = input(f"{self.getCurrDir()} > ").split()
                # make it just loop through args and check if single command
                # or contains tack options

                if 'ls' in args:
                    self.showAllFiles()
                
                else:
                    self.commands[args[0]](args[1])
            except UsrErr as e:
                print(e)




if __name__ == "__main__":
    shell = Shell().acceptCommands()
