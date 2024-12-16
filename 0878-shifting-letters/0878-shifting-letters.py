class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # self.letters = {chr(97+i):i for i in range(26)}

        self.letters = {}
        for i in range(26):
            self.letters[chr(97+i)] = i
        
        ans = ''
        summ = sum(shifts)

        for elm,i in zip(s,shifts):

            currentChar = self.shift(elm,summ%26)
            ans += currentChar
            summ -= i
        return ans
    
    def shift(self,letter,bit):
        letter = (self.letters[letter] + bit)%26
        return chr(97+letter)


