#字典 无顺序
d={'me':1,'you':2}#key:value
print(d['me'])
#del d['me']
#d['1':3]#加元素
#print(d)
for i,j in d.items():
    print(i,j)
print(max(d,d.get))