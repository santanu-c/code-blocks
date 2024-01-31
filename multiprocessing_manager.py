import multiprocessing as mp

l =[[1,2],[3,4],[5,6],[7,8]]

def foo(n,L):
    L.append(n)

pool = mp.Pool(processes=2)
manager = mp.Manager()
L = manager.list()

[pool.apply_async(foo, args=[n,L]) for n in l]

pool.close()
pool.join()

print(L)

