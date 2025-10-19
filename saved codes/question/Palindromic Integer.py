#Method 1
x=list(input())
x_oppsite=[]
for i in range(len(x)):
    sub=x[len(x)-i-1]
    x_oppsite.append(sub)
if x_oppsite==x:
    print('Yes')
else:
    print('No')

#Method 2
s=input();print('Yes'if s==s[::-1]else'No')
#list[start:stop:step]
#step=-1 反转列表/字符串