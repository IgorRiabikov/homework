
#from functools import lru_cache
#import random
import time
import functools

def profile(f):
    @functools.wraps(f)
    def deco(*args):
        start = time.time()
        result = f(*args)
        print(f'Elapsed time for function {f.__name__}: {time.time() - start}')
        return result
    return deco


def cache(max_limit):
    def limit(f):
        @functools.wraps(f)
        def deco(*args):
            if args in deco._cache:
                return deco._cache[args]
            result = f(*args)
            if len(deco._cache) == max_limit:
                dlya_udalenia=list(deco._cache.keys())
                del deco._cache[(dlya_udalenia[0])]
            deco._cache[args] = result
            print (deco._cache)
            return result

        deco._cache = {}
        return deco
    return limit

@profile
@cache(100)
# 0 1 1 2 3 5 8 13 ...
def fibo(n):
    """Inefficient fibo function"""
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(332))

