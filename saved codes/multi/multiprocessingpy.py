#多核处理multiprocessing

import multiprocessing as mp
#import threading as td
'''
def job():
    print('aaa')
    
#t1=td.Thread(target=job,args=(a,))

if __name__=='__main__':
    p1=mp.Process(target=job)
    p1.start()
    p1.join()
    
    '''
#不能有return,需要q，Queue来储存

def job(q):
    result=0
    for i in range (10000):
        result+=i+i**2+i**3
    q.put(result)
if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=job,args=(q,))
    p1.start()
    p1.join()
    p2 = mp.Process(target=job, args=(q,))
    p2.start()
    p2.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)
    















