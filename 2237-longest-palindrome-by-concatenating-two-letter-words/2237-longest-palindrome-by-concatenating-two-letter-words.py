class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        used_center = False

        for word in count:
            rev = word[::-1]
            if word != rev:
                if rev in count:
                    pairs = min(count[word], count[rev])
                    length += pairs * 4  
                    count[word] -= pairs
                    count[rev] -= pairs
            else:
                pairs = count[word] // 2
                length += pairs * 4
                count[word] -= pairs * 2
                if count[word] and not used_center:
                    length += 2
                    used_center = True

        return length
