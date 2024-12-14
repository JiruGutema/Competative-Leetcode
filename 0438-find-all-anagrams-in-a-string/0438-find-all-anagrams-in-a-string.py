class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # k = len(p)
        # p = sorted(p)
        # start = 0
        # end = k
        # ans = []

        # while end < len(s)+1:
        #     if p == sorted(s[start:end]):
        #         ans.append(start)
        #     start += 1
        #     end += 1
        # return ans
        
        result = []
        target = collections.Counter(p)
        window = collections.Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            curr_char = s[i]
            window[curr_char] += 1

            if window == target:
                result.append(i - len(p) + 1)
            window[s[i - len(p) + 1]] -= 1
            if window[s[i - len(p) + 1]] == 0:
                del window[s[i - len(p) + 1]]
        return result