class date:
    def __init__(self,year,month,day):
        self.year =year
        self.month=month
        self.day=day

    @classmethod
    def create_date(cls,str_date):
        y,m,d =map(int,str_date.split('-'))  #.split 将字符串以'-'切割
        instance =cls(y,m,d)   #在类方法中创建实例,cls相当于class类本身
        return instance

    @staticmethod
    def is_day_valid(str_date):
        y,m,d=map(int,str_date.split('-'))
        return y<4000 and 0<m<13 and 0<d<32

if __name__ == '__main__':
    d1=date(2018,11,16)
    print(d1.year)
    d2=date.create_date('2018-11-15')
    print(d2.month)
    d3=date.is_day_valid('2018-11-150')
    print(d3)