import threading
import time
from queue import Queue
'''
def thread_job():
    #print('This is added Thread,number is %s'%threading.current_thread)
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')
def main():
    T1=threading.Thread(target=thread_job,name='T1')
    T1.start()
    T1.join()#使下列语句在T1结束时才运行
    T2=threading.Thread(target=T2_job,name='T2')
    T2.start()
    T2.join()
    print('done\n')


def T2_job():
    print('T2 start\n' )
    print('T2 finish\n')


if __name__=='__main__':
    main()

#无join的情况下，done 比 finish 先出现，证明多线程是同时进行的
'''

q=Queue()
def job(l,q):
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)
    
def multithreading():
    threads=[]
    data=[[1,2,3],
          [1,2,4],
          [2,6,4],
          [2,2,2]]
    for i in range(4):
        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results=[]
    for j in range(4):
        results.append(q.get())
    print(results)

multithreading()



#lock=threading.Lock(),lock.acquire,lock.release()
