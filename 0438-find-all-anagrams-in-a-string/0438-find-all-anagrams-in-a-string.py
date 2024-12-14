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
        window = collections.Counter(s[:len(p)])
        if target == window:
            result.append(0)
        left = 0

        for i in range(len(p), len(s)):

            curr_char = s[i]
            window[curr_char] += 1

            char = s[left]
            window[char] -= 1

            if window[char] == 0:
                del window[char]

            if window == target:
                result.append(left+1)
            left += 1
            
        return result