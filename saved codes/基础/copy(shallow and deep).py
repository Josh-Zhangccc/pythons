#copy
import copy
a=[1,2,[3,4]]
b=a
c=copy.copy(a)
print(id(a)==id(b))#改变b就改变a
print(id(a)==id(c))#改变c不改变a的浅层
print(id(a[2])==id(c[2]))
d=copy.deepcopy(a)
print(id(a[2])==id(d[2]))


divmod(14,7)#divmod(a,b)--> (a//b,a%b)