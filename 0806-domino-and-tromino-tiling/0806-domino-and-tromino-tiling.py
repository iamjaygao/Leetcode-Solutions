MOD = 10 ** 9 + 7
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        f = [0] * (n + 1)
        g = [0] * (n + 1)

        f[0] = 1
        f[1] = 1
        f[2] = 2
        g[0] = 0
        g[1] = 0
        g[2] = 1

        for i in range(3, n+1):
            f[i] = (f[i-1] + f[i-2] + 2*g[i-1]) % MOD
            g[i] = (f[i-2] + g[i-1]) % MOD
        return f[n] % MOD

        