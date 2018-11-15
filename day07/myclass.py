class A:
    def foo(self):
        print('您好!')

class B:
    def bar(self):
        print('How are you?')

class C(A,B):
    pass

if __name__ == '__main__':
    c = C() #子类的实例继承了所有父类的方法
    c.foo() #如果多个父类有同名方法,查找顺序是从上到下,从左到右
    c.bar() #也就是先查子类,再查父类,父类按定义顺序从左到右查找