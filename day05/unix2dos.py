from sys import argv
def unix2dos(fname,end='\r\n'):
    new_fname = fname+'.txt'
    with open(fname,'r') as data_src:
        with open(new_fname,'w') as data_dst:
            for line in data_src:
                data_dst.write(line.rstrip() + end)

if __name__ == '__main__':
    if argv[1]:
        fname=argv[1]
        unix2dos(fname)
    # else:
    #     print('请输入有效文件路径')