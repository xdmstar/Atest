x = input('请输入年份:')
x = int(x)

if x % 4 == 0:
    if x %100 == 0:
        if x % 400 == 0:
            print('是')
        else:
            print('不是')
    else:
        print('是')
else:
    print('不是')