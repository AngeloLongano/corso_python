from memory_profiler import profile
import random as r

@profile
def foo():
    x = [x for x in range(0, 1000)]
    y = [ r.randint(1,100) for y in range(0, 2000)]
    del x
    return y
if __name__=="__main__":
    foo()