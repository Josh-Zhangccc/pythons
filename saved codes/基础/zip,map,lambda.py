#map,zip
a=[1,2,3]
b=[3,4,5]
c=list(zip(a,b))#一对一整合
print(c)
fun=lambda x,y:x+y#变def的两行为一行
print(fun(1,1))
d=list(map(fun,[1,3],[1,5]))
print(d)
#注意，zip和map的输出值都是object
