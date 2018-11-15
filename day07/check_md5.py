import hashlib
import sys

def check(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
        m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    print(check(sys.argv[1]))