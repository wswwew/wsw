try:
    num=int(input('number:'))
    result=100/num
except (ValueError,ZeroDivisionError):
    print('无效输入')
except (KeyboardInterrupt,EOFError):
    print('\nBye-bye')
else:
    print(result)
finally:
    print("Done")