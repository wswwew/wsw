import random_passwd
import subprocess

class UserAdd:
    def __init__(self,uname):
        self.uname=uname
        self.password=random_passwd.gen_pass()
    #def user_check(self):

    def user_add(self):
        subprocess.call('useradd %s' % self.uname,shell=True)
        subprocess.call(
            'echo %s | passwd --stdin %s' % (self.password, self.uname),
            shell=True
        )
        self.first_passwd()

    def first_passwd(self):
        with open('/home/%s/first_password'%self.uname,'w') as fobj:
            fobj.write(self.password+'\n')

if __name__ == "__main__":
    uname=input("请输入用户名:")
    UserAdd(uname).user_add()