import os
import re

class WRFile:
    def __init__(self,fname):
        self.fname=fname

    def check_file(self):
        if os.path.exists(self.fname):
            print('%s is already exists.' % self.fname)
        else:
            filename=re.split('/',self.fname)[-1]
            dirpath=self.fname.rstrip('/'+filename)
            if not os.path.exists(dirpath):
                print('文件或目录不存在,将创建')
                os.makedirs(dirpath)
            with open(self.fname,'w') as fobj:
                pass


    def write_file(self):
        with open(self.fname,'a+') as fobj:
            while True:
                cat=input('>:')+'\n'
                if cat == 'end\n':
                    break
                fobj.write(cat)

    def read_file(self):
        with open(self.fname,'r') as fobj:
            while True:
                date = fobj.readline().rstrip('\n')
                if not date:
                    break
                print(date)

if __name__ == '__main__':
    haha=WRFile('/mnt/haha.txt')
    haha.check_file()
    haha.write_file()
    haha.read_file()