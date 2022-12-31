#! usr/bin/python3


#NOTE: add timestamp of last update functionality
# this timestamp changes with the last file update
# or the last update of contents of a directory.

#NOTE: add the rwx of files.

class Directory:
    def __init__(self, dir_name, parent_dir):
        self.dir_name = dir_name
        self.children = []
        self.parent = parent_dir

    def appendChildren(self, files):
        self.children.append(files)

    def getChildren(self):
        return self.children

    def getName(self):
        return self.dir_name

    def changeName(self, new_name: str):
        if not self.dir_name == "/":
            self.dir_name = new_name

class File:
    def __init__(self, fname: str, parent_dirname: Directory):
        self.parent = parent_dirname
        self.filename = fname
        self.contents = ""
    
    def getName(self):
        return self.filename

    def changeName(self, new_name: str):
        self.filename = new_name
