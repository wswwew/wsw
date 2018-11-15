class BearToy:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s,Lalala...'% self.name)

class NewBearToy(BearToy):  #新类是BearToy的子类
    def __init__(self,name,size,color,date):
        '父子类有同名方法,子类对象执行子类方法'
        #BearToy.__init__(self,name,size,color)
        super(NewBearToy, self).__init__(name,size,color)
        self.date = date

    def run(self):
        print('i can ran!')


if __name__ == '__main__':
    big=NewBearToy('duke','小','白')
    second=BearToy('熊二','Middle','Brown')
    big.sing()
    big.run()