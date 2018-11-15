class BearToy:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color


    def sing(self):
        print('I am %s,Lalala...'% self.name)

if __name__ == '__main__':
    big=BearToy('熊大','Large','Brown')
    second=BearToy('熊二','Middle','Brown')
    print(big.size)
    print(big.color)
    big.sing()
    second.sing()