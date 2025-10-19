class derivatives:
    times=10
    def __init__(self,times):
        self.times=times
    def poly(c,p):
        try:
           coefficient=c.split(',')
           power=p.split(',')
        except Exception as a:
           return a
        else:
            for i in range(len(coefficient)):
                coefficient[i]=eval(coefficient[i])*eval(power[i])
                power[i]=eval(power[i])-1
                if i ==0:
                    print(rf'$={coefficient[i]}x^{power[i]}$',end='')
                elif coefficient[i]<0:
                    print(rf'${coefficient[i]}x^{power[i]}$',end='')
                elif coefficient[i]>0:
                    print(rf'$+{coefficient[i]}x^{power[i]}$',end='')     
                else:
                    pass           

c=input('c')
p=input('p')
result=derivatives.poly(c,p)
print(result)


