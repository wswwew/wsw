#!/usr/bin/env python3
import os
def get_filename():
    '判断文件名是否存在'
    while True:
        fname=input('请输入文件名:')
        if not os.path.exists(fname):
            break
        print('%s already exitsts' % fname)
    return fname

def get_content():
    '获取用户输入内容存放到列表'
    content=[]
    print('输入数据,输入end退出:')
    while True:
        data=input('>')
        if data=='end':
            break
        content.append(data)
    return content

def wfile(fname,content):
    '将内容写入到列表'
    content=['%s\n' % line for line in content]
    with open(fname,'w') as f:
        f.writelines(content)

if __name__ == '__main__':
    fname=get_filename()
    content=get_content()
    wfile(fname,content)