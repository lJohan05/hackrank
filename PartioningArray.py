def solve(k, arr):    
    n = len(arr)
    occur = {}
    for i in arr:
        if (i in occur):
            occur[i] += 1
        else:
            occur[i] = 1
    if (n % k != 0):
        return ("No")
    for key in occur:
        if (occur[key] > n/k):
            return ("No")
    return ("Yes")

print(solve(2, [1,2,3,4]))