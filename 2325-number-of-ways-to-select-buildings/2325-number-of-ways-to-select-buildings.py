class Solution:
    def numberOfWays(self, s: str) -> int:
        # count = 0
        # n = len(s)

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             substring = s[i] + s[j] + s[k]
        #             if substring in ["010", "101"]:
        #                 count += 1

        # return count
        ways = 0
        one = zero = zero_1 = one_0 = 0
        for c in s:
            if c == '0':
                zero += 1
                one_0 += one
                ways += zero_1
            else:
                one += 1    
                zero_1 += zero 
                ways += one_0
        return ways
