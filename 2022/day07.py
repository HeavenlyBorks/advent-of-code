import sys


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def print(self, n):
        print(f"{'-'*n}{self.name} - {self.size} bytes")

    def list(self):
        return [self]

    def __repr__(self):
        return self.name


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        if parent:
            self.parent = parent

    def add_dir(self, name):
        if name not in self.children.keys():
            self.children[name] = Directory(name, self)

    def add_file(self, name, size):
        if name not in self.children.keys():
            self.children[name] = File(name, size)

    def cd(self, folder):
        if folder == "..":
            return self.parent
        else:
            return self.children[folder]

    def print(self, n=0):
        print(f"{'-'*n}{self.name} - dir - {self.size}")
        for child in self.children.values():
            child.print(n + 1)

    @property
    def size(self):
        total = 0
        for child in self.children.values():
            total += child.size
        return total

    def list(self):
        l = [self]
        if self.children:
            for child in self.children.values():
                l.extend(child.list())
        return l

    def __repr__(self):
        return self.name


class Manager:
    def __init__(self):
        self.root = Directory("/")
        self.dir: Directory = self.root

    def cd(self, folder):
        if folder == "/":
            self.dir = self.root
        else:
            self.dir = self.dir.cd(folder)

    def add_dir(self, name):
        self.dir.add_dir(name)

    def add_file(self, name, size):
        self.dir.add_file(name, size)


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        manager = Manager()
        for i, line in enumerate(f):
            line = line.split()
            if line[0] == "$":
                if line[1] == "cd":
                    manager.cd(line[2].strip())
            elif line[0] == "dir":
                manager.add_dir(line[1].strip())
            else:
                manager.add_file(line[1].strip(), line[0])

        total = 0
        for elem in manager.root.list():
            if elem.size <= 100000 and type(elem) == Directory:
                total += elem.size

        print(total)

        candidates = []
        total = manager.root.size
        goal = 30000000
        for elem in manager.root.list():
            if 70000000 - (total - elem.size) >= goal and type(elem) == Directory:
                candidates.append(elem.size)

        candidates.sort()
        print(candidates[0])
