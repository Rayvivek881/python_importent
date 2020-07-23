from math import gcd as __gcd
MAX = 100
def recur(ind, cnt, last, a, n, k, dp):
    if cnt == k:
        return 0
    if ind == n:
        return -10 ** 9
    if dp[ind][cnt] != -1:
        return dp[ind][cnt]
    ans = 0
    for i in range(ind, n):
        if cnt % 2 == 0:
            ans = max(ans, recur(i + 1, cnt + 1, i, a, n, k, dp))
        else:
            ans = max(ans, __gcd(a[last], a[i]) + recur(i + 1, cnt + 1, 0, a, n, k, dp))
    dp[ind][cnt] = ans
    return ans
a = [4, 5, 3, 7, 8, 10, 9, 8]
n = len(a)
k = 4
dp = [[-1 for i in range(MAX)] for i in range(n)]
print(recur(0, 0, 0, a, n, k, dp))