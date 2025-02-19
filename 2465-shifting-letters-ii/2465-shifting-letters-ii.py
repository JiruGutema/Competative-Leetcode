class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        my_sums = [0] * n
        for l, r, nums in shifts:
            d = 1 if nums else -1
            my_sums[l] += d
            if r + 1 < n:
                my_sums[r+1] -= d
        
        for i in range(1, n):
            my_sums[i] += my_sums[i-1]

        alp = ascii_lowercase
        res = []
        for i, c in enumerate(s):
            o = ord(c) - ord('a') + my_sums[i]
            res.append(alp[o%26])
            
        return ''.join(res)
        