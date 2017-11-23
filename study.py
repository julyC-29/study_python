def power(x,n=2):#联系使用默认函数
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

print(power(5,3))
def enroll(name,gender,age=18,city='厦门'):#默认参数必须指向不可变对象
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('李达','F'))
print(enroll('王二','M','17'))
print(enroll('张三','M','16','上海'))
print(enroll('张四','F',city='北京'))

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
l=add_end([1,2,3])
print(l)
print(l)

#定义可变参数 （利用tuple或者list传进来）
def calc_t(number):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum
#定义可变参数
def calc(*number):
    sum=0
    for n in number:
        sum=sum+n*n
    return sum
print(calc(1,2,3))
print(calc_t((1,2,3)))
nums=[1,2,3]
print(calc(*nums))
#g关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
print(person('Michael',30))
print(person('Bob',35,gender='M',city='厦门'))
#只接收city和job作为关键字参数
#命名关键字必须传入参数名，如果没有传入参数名，调用将报错
def person(name,age,*,city,job):
    print(name,age,city,job)
print(person('Jack',24,city='Beijing',job='Engineer'))
print(person('Jack',24,city='Beijing',job='Engineer'))
#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
#尾递归函数
def fact1(n):
    return fact2(n,1)
def fact2(n,m):
    if n==1:
        return m
    return fact2(n-1,n*m)
print(fact1(5))