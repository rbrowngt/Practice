"""

Find the longest positive subsequence

i.e.
[-1,4,3,1,2,3,4,5,-9,2,7]

Longest: 7, index:1 
"""

def longest_subsequence(a):
    """
    Return: (length, index)
    """
    # Sanity checks
    if a is None or len(a) == 0:
        return 0
    
    index = -1
    currentLength = 0
    maxLength = 0
    flag = False
    
    for idx, val in enumerate(a):
        if val > 0:
            if flag:
                currentLength+=1

            else:
                if index < 0:
                    index = idx
                currentLength = 1
                flag = True
            
            if maxLength == 0:
                maxLength = currentLength
        else:
            flag = False
            if currentLength >= maxLength:
                maxLength = currentLength
            currentLength = 0
    
    return (maxLength, index)

def seive(n):
    import math
    seive_list = list(range(n + 1))
    seive_list[1] = 0
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn):
        if seive_list[i]:
            seive_list[i*i: n+1: i] = [0] * len(range(i*i, n+1, i))         
    return filter(None, seive_list)

def sieve_2(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
            

if __name__ == '__main__':
    import time
    """
    start = time.time()
    print sieve_2(1000000)
    end = time.time()
    print end - start
    """
    start = time.time()
    print sum(seive(2000000))
    end = time.time()
    print end - start
