from hashlib import md5

class Hasher:
    def __init__(self, path, coding):
        self.path = path
        self.coding = coding

    def __enter__(self):
        self.file = open(self.path, encoding=self.coding)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    
    def hashing(self):
        result = (md5(line.encode()).hexdigest() for line in self.file.read().split('\n'))
        return result

    def readline(self):
        result = (line for line in self.file.read().split('\n'))
        return result

if __name__ == "__main__":

    with Hasher('readme.txt', 'windows-1251') as f:
        for i in f.hashing():
            print(i)