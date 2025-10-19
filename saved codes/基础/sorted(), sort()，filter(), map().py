#sorted(), sort(),filter(), map()
#迭代
a=[1,4,3,2]
b=sorted(a)#sorted不会改变原有列表
#sorted(iterable,key,reverse),函数不加括号
#iterable,可迭代对象，如列表，元组，字符串
print(a)
print(b)
a.sort()#sort会改变原有列表
print(a)

#筛选器
evennumbers=filter(lambda x:x%2==0,a)#(fun,ite),返回值是object
print(list(evennumbers))
#映射器（重复函数）
cube=map(lambda x:x**3,a)#(fun,ite),返回值是object
print(list(cube))
