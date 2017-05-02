import time

def how_long(fxn):
    start = time.time()
    def inner(*args):
        return fxn(*args)
    dur = time.time() - start
    print "execution time: " + str(dur)
    return inner

def show_call_info(fxn):
    def inner(*args):
        print fxn.func_name + ": " + str(args)
        return fxn (*args)
    return inner

@how_long
@show_call_info

###FIBONACCI###
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fibcache = {}
def fib(n):
    if n in fibcache:
        return fibcache[n]
    else:
        fibcache[n] = n if n<2 else fib(n-1) + fib(n-2)
        return fibcache[n]

#print fib(0)
#print fib(1)
#print fib(2)
#print fib(3)
#print fib(4)
#print fib(5)
#print fib(10)
#print fib(20)
#print fib(30)
#print fib(40)
#print fib(50)
#print fib(1000)

def memoize(f):
    memo = {} #hashmap/dict for 0(1) lookup
    def inner(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return inner

@memoize
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)


