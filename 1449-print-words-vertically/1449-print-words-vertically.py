class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        result = []
        
        for i in range(max_length):
            vertical_word = []
            for word in words:
                if i < len(word):
                    vertical_word.append(word[i])
                else:
                    vertical_word.append(' ')
            result.append(''.join(vertical_word).rstrip())
        
        return result