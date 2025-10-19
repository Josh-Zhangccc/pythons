import multiprocessing as mp

value=mp.Value('d',1)
array=mp.Array('i',[1,2,3,4])
#摄取
v=value.value


