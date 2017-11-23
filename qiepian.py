L=list(range(100))
print(L)
print(L[:10])#取出前十个元素
print(L[-10:])#取出后十个元素
print(L[10:10])#前11到20个数
print(L[:10:2])#前十个数 每两个取一个
print(L[::5])#所有数，每5个取一个
#tuple也是一种list，唯一的区别就是tuple不可变，所以tuple也可以用切片操作，只是操作的结果还是tuple
t=(0,1,2,3,4,5)
print(t[:3])
#字符串也可以看成一种list，每一个元素就是一个字符，所以字符串也可以切片操作，操作结果还是字符串
str='ABCDEFG'
print(str[:3])