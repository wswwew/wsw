from create_file import get_content

def pcoitent():
    print('+'+'*'*50+'+')
    for ch in content:
        print('+{:^50}+'.format(ch))
    print('+' + '*' * 50 + '+')

if __name__== '__main__':
    content=get_content()
    pcoitent()