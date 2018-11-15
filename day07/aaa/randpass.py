from string import ascii_letters,digits
from random import choice

def randompass(n=8):
    all_choice=ascii_letters+digits
    result=[choice(all_choice) for i in range(n) ]
    return ''.join(result)

if __name__ == '__main__':
    print(randompass())
    print(randompass(10))