class books:
    def __init__(self,name,writer,pages):
        self.name = name
        self.writer = writer
        self.pages = pages

    def __str__(self):
        return '<<%s>>'% self.name

    def __call__(self):
        print('<<%s>> is writen by %s'% (self.name,self.writer))

if __name__ == '__main__':
    book=books('haha','xixi','200')
    print(book)
    book()