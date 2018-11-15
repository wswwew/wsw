class Vendor:
    def __init__(self,em,ph):
        self.email = em
        self.phone = ph

class BearToy:
    def __init__(self,name,size,color,em,ph):
        self.name = name
        self.size = size
        self.color = color
        self.vendor = Vendor(em,ph)

    def sing(self):
        print('I am %s,Lalala...'% self.name)

if __name__ == '__main__':
    big=BearToy('熊大','Large','Brown','haha@qq.com','137')
    second=BearToy('熊二','Middle','Brown','xixi@qq.com','136')
    print(big.vendor.phone)