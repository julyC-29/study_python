#生成1到10的数
print(list(range(1,11)))
#生成1到10的数的平方
print([x*x for x in range(1,11)])
#生成1到10中偶数的平方
print([x*x for x in range(1,11) if x%2==0])
#生成ABC中每个字母对XYZ中每个字母组合的结果
print([x+y for x in 'ABC' for y in 'XYZ'])

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

#列表生成式可以利用两个变量来生成列表
d={'x': 'A', 'y': 'B', 'z': 'C' }
print([x+'='+y for x,y in d.items()])

# 练习
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L=['Hello', 'World', 18, 'Apple', None]
print([x for x in L if isinstance(x,str)])

# 生成器

g=(x*x for x in range(1,11))
for x in g:
    print(x)

#函数生成斐波拉切数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))

#将函数生成斐波拉切数列改成 用generator生成斐波拉切数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield (b)
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(6))
#因为for循环调用generator时 拿不到generator的return值，必须捕获StopIteration错误，返回值在StopIteration的value中
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

