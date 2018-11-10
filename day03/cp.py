#!/usr/bin/env python3
import sys
def cp(src_file,dst_file):
    src = open(src_file,'rb')
    w = open(dst_file,'wb')
    while True:
        data = src.read(4096)
        if not data:
            break
        w.write(data)
    src.close()
    w.close()
cp(sys.argv[1],sys.argv[2])