import multiprocessing as mp
def job(x):
    return x*x

def multiprocess():
    pool=mp.Pool(processes=3)#default all cores
    res=pool.map(job,range(10))
    l=mp.Lock()
    l.acquire()
    print(res)
    res=pool.apply_async(job,(2,))
    l.release()
    print(res.get())
    multi_res=[pool.apply_async(job,(i,))for i in range(10)]
    print([res.get()for res in multi_res])
'''map可以很多个，而apply_async每一次只能一个值运算'''
#pool可以有return值
if __name__ == '__main__':
    multiprocess()
