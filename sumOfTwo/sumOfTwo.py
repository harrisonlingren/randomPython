def sumOfTwoGood(a, b, v):
    # Runtime: O(n^2)
    
    if len(a) >= len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    for i in range(len(shorter)):
        for j in range(len(longer)):
            if v - longer[j] == shorter[i]:
                return True
    
    return False


def sumOfTwoBetter(a, b, v):
    # Runtime: O(n*log(n))
    
    if len(a) == 0 or len(b) == 0:
        return False
    
    # simple binary search
    def bsearch(arr, num):
        n = len(arr)
        mid = n // 2
        
        if n == 1 and arr[0] == num:
            return mid
        elif n == 1 and arr[0] != num:
            return -1       
        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            return bsearch(arr[mid:], num)
        else:
            return bsearch(arr[:mid], num)
    
    # make shorter & longer arrays, sort results
    if len(a) >= len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    
    shorter.sort()
    longer.sort()
    cache = {}
    
    # binary search for i in shorter
    for i in shorter:
        if v - i not in cache:
            cache[v - i] = (bsearch(longer, v - i) != -1)
        if cache[v-i]:
            return True
    
    return False

def sumOfTwoBest(a, b, v):
    # Runtime: O(n)
    
    setA = set()
    for i in a:
        if i not in setA:
            setA.add(i)
            
    setB = set()
    for i in b:
        if i not in setB:
            setB.add(i)
        
    for i in b:
        if (v-i) in setA:
            return True
    
    return False
