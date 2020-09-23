def arrayChallenge(arr):
    n = len(arr)
    ans = [0] * n
    sum = arr[0]
    for i in range(1, n):
        ans[i] = arr[i] * i - sum
        sum += arr[i]
    return ans

print(arrayChallenge([2,1,4]))