class Solution(object):
    def distributeCandies(self, n, limit):
        def nCr(n, r):
            if r > n or n < 0 or r < 0:
                return 0
            if r == 2:
                return n * (n - 1) // 2
            res = 1
            for i in range(r):
                res = res * (n - i) // (i + 1)
            return res

        if n > 3 * limit:
            return 0

        total_ways = nCr(n + 2, 2)
        one = 3 * nCr(n - limit + 1, 2)
        two = 3 * nCr(n - 2 * limit, 2)
        three = nCr(n - 3 * limit - 1, 2)
        result = total_ways - one + two - three
        return max(result, 0)