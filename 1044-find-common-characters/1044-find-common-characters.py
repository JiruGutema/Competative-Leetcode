from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words[1:]:
            count &= Counter(word)

        ans = []
        for char, freq in count.items():
            ans.extend([char] * freq)

        return ans
