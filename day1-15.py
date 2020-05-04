# print('hello,word!')
#
# print('hello ,word！', end=' ')

# f = float(input('输入温度'))
# c = (f - 32) / 1.8
# 
# print('%.1f华氏温度=%.1f摄氏温度' % (f, c))
# 判断瑞年

# year = int(input('请输入年份t：'))
# Is_leap=( year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(Is_leap)

# 单位互换

# value=float(input('输入长度：'))
# unit=input('输入单位：')
# if unit=='in' or unit=='英寸':
#     print('%f英寸=%f厘米'%(value,value*2.54))
# if unit=='cm' or unit=='厘米':
#     print('%f厘米=%f英寸'%(value,value/2.54))

# 身份验证
# usename = input('请输入账号：')
# password = input('请输入密码：')
#
# if usename == 'wzb' and password == '123':
#     print('登录成功')
# else:
#     print('登录失败')

# shushu
# from math import sqrt
#
# num = int(input('请输入：'))
# is_prime = True
# for factor in range(2, int(sqrt(num))):
#     if num % factor == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# 打印最小公倍数，公约数

# x = int(input('情书整数：'))
# y = int(input('情书整数：'))
#
# if x > y:
#     x, y = y, x
# for fac in (x, 0, -1):
#     if x % fac == 0 and y % fac == 0:
#         print('%d,%d的最小公倍数是%d' % (x, y, fac))
#         print('%d,%d的最大公约数是%d' % (x, y, (x * y) // fac))
# 打印三角形

# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end=' ')
#     print()
# row = int(input('请输入行数：'))
# for i in range(row):
#     for j in range(row):
#         if j < row - i -1:
#             print(' ', end=' ')
#         else:
#             print('*', end='')
#     print()
# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()

#口诀表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()
#
# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
# import math
# for num in range(1,1000):
#     result=0
#     for fac in range(1,int(math.sqrt(num))+1):
#         if num%fac==0:
#             if fac>1 and num//fac!=fac:
#                 result+=num//fac
#     if result==num:
#         print(num)
#

# num=int(input('请输入树：'))
# a=num
# num2=0
# temp=0
# while num>0:
#     temp=num%10
#     num2=num2*10+temp
#     num=num//10
#
# if num2==a:
#     print(1)
# else:
#     print(0)

'''

找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3


'''
#
# def main():
#     num=int(input('输入人数：'))
#     names=[None]*num
#     score=[None]*num
#
#     for index in range(num):
#         names[index]=input('第%d个人的名字'%(index+1))
#         score[index]=float(input('第%d个人的分数'%(index+1)))
#     total=0
#     for i in range(num):
#         total+=score[i]
#     print('平均分：%.1f'%(total/num))



def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊',87))
    scores.clear()
    print(scores)


def main():
    stu = {'name': '骆昊', 'age': 38, 'gender': True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 20
    print(stu)
    stu.setdefault('score', 78)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)



def main():
    f = [1 , 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        f.append(f[i - 1] + f[i - 2])
    for val in f:
        print(val, end=' ')


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)


def main():
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError
    fruits[1] = 'apple'
    print(fruits)
    # 添加元素
    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)
    # 删除元素
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('apple')
    print(fruits)


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    fruits5 = fruits[::-1]
    print(fruits5)


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))
    print(list1)
    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))
    # 生成器(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()
    gen = fib(20)
    print(gen)
    for elem in gen:
        print(elem, end=' ')
    print()


def main():
    str = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0]
        # for Windows use os.system('cls') instead
        os.system('cls')

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()
    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)

def main():
    # 定义元组
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'      # TypeError
    # 变量t重新引用了新的元组 原来的元组被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 元组和列表的转换
    person = list(t)
    print(person)
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])




def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

from random import randint


class GuessMachine(object):

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        else:
            self._hint = '恭喜你猜对了'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('请输入: '))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('智商余额不足!')
        play_again = input('再玩一次?(yes|no)') == 'yes'


if __name__ == '__main__':
    main()