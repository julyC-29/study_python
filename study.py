def power(x,n=2):#联系使用默认函数
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s

print(power(5,3))
def enroll(name,gender,age=18,city='厦门'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('李达','F'))
print(enroll('王二','M','17'))
print(enroll('张三','M','16','上海'))