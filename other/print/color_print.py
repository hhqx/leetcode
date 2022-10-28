import multiprocessing
import random

print('\033[1;33;40m《测试文本,python  print打印颜色字体！》\033[1;35;46m————horysk')


print('\033[1;31m' + '******************************' + '\033[0m')
# 也可以随机打印颜色
n=random.randint(1,9)
color=random.randint(30,37)
msg = 'hello'
Pn=multiprocessing.current_process().name + '-' + msg
print("\033[1;{}m  ProcessName: {} >>> Page: {}\033[0m".format(color,Pn,n))
