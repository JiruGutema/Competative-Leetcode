class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        res = maxValue
        mapp = {num: 1 for num in range(1, maxValue + 1)}
        
        for arr_size in range(1, n): 
            dictt = Counter()
            for base_val in mapp: 
                for m in range(2, maxValue // base_val + 1): 
                    com = comb(n - 1, arr_size)
                    res += com * mapp[base_val]
                    dictt[m * base_val] += mapp[base_val]
            mapp = dictt
            res %= MOD
        
        return res 
