def mygen():
    a = 10 + 20
    b = 40
    yield a
    yield 'hellow world'
    b='ni hao'
    yield b
    b='haha'
    yield b

if __name__ == '__main__':
    mg=mygen()
    myiter = iter([1, 2, 3])
    print(myiter.__next__())
    print(myiter.__next__())
    print(myiter.__next__())
    print(myiter.__next__())
    print(next(mg))
    print(next(mg))
    print(next(mg))
    print(next(mg))
    newmg=mygen()
    print(str(i) for i in iter(newmg))
    # for item in newmg:
    #     print(item)