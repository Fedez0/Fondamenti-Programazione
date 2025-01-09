class list():
    def __init__(self):
        self.l = []

    def insert(self,x):
        self.l.append(x)
    def leng(self):
        return len(self.l)
    def first(self):
        return self.l[0]
    def get(self,i):
        return self.l[i]
    def delete(self,i=-1):
        self.l.pop(i)
    def __str__(self):
        return f'{self.l[::]}'


if __name__ == '__main__':
    l = list()
    l.insert(4)
    l.insert(5)
    print(l)