import hashlib,time,os
import tarfile
import pickle as p
import sys

def check_dir(src_dir,dst_dir):
    if os.path.exists(src_dir):
        if os.path.isdir(dst_dir) is not True:
            print('目标目录不存在,将自动创建')
            os.makedirs(dst_dir)
    else:
        print('源文件或目录不存在,请确认后重试')

def frist_backup(src_dir,dst_dir,md5_file):
    fname=os.path.basename(src_dir.rstrip('/'))
    fname='%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname=os.path.join(dst_dir,fname)

    tar=tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    md5_date={}
    for path,dirs,files in os.walk(src_dir):
        for file in files:
            key=os.path.join(path,file)
            md5_date[key]=md5_check(key)

    with open(md5_file,'wb') as fobj:
        p.dump(md5_date,fobj)

def incr_backup(src_dir,dst_dir,md5_file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    md5_date = {}
    for path, dirs,files in os.walk(src_dir):
        for file in files:
            key=os.path.join(path,file)
            md5_date[key]=md5_check(key)

    with open(md5_file,'rb') as fobj:
        md5_olddate=p.load(fobj)

    with open(md5_file,'wb') as fobj:
        p.dump(md5_date,fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in md5_date:
        if md5_olddate.get(key) != md5_date[key]:
            tar.add(key)
    tar.close()

def md5_check(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == "__main__":
    try:
        src_dir=sys.argv[1]
        dst_dir=sys.argv[2]
        md5_file=os.path.join(sys.argv[2],'backup.md5.date')
    except IndentationError:
        print('请输入绝对路径')

    check_dir(src_dir,dst_dir)

    if time.strftime('%a') == 'Mon':
        frist_backup(src_dir,dst_dir,md5_file)
    else:
        incr_backup(src_dir,dst_dir,md5_file)