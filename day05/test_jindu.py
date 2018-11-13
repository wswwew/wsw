import time
def jindu(num):
    jdt=[tu for tu in '#'*50]
    jdt[num]='@'
    print('\r')
    for a in range(50):
        print(jdt[a],end='\r')
    #print('')

if __name__ == '__main__':
    while True:
        for l in range(50):
            jindu(l)
        time.sleep(0.3)