import re

def count_pat(fname,patt):
    patt_dict = {}
    cpatt=re.compile(patt)

    with open(fname,'r') as fobj:
        for line in fobj:
            m=cpatt.search(line)
            if m:
                key=m.group()
                patt_dict[key]=patt_dict.get(key,0)+1

    return patt_dict

if __name__ == '__main__':
    fname='/mnt/access_log'
    ip = '^(\d+\.){3}\d+'
    print(count_pat(fname,ip))
    #br = ''
    #print(count_pat(fname,br))
    for i in count_pat(fname,ip):
        print(i,count_pat(fname,ip)[i])