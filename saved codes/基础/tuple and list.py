a_tuple=(1,2,3,4)#元组
#元组的值不能改动
#列表的值可以改动
aa_tuple=2,3,4,5

a_list=[2,3,5,6]#列表
#两者都有顺序
for i in a_tuple:
    print(i)
for j in a_list:
    print(j)

len(a_list)#list中的项数

a_list.append(0)#在列表最后添加0
a_list.insert(0,1)#在第0位添加1
a_list.remove(2)#删除第一个出现2的地方，其余保留
a_list.pop()#默认最后删除，可加index，有返回值
del a_list[:]
a_list[1]#列表中第1位
a_list[-1]#最后一位
a_list[0:3]#从0到2位[0，3）or[0,2],后空表示最后，前孔表示最前
a_list.index(0)#索引第一个出现
a_list.count(2)#计算出现了几次2
a_list.sort()#从小到大
a_list.sort(reverse=True)

#多为列表
a=[[1,2],[3,4]]
a[2][1]=3





