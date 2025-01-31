class Solution:
    def isPalindrome(self, s: str) -> bool:
            # a bit brute force
        # string = ""
        # for i in s:
        #     if i.isalpha() or i.isnumeric():
        #         string += i.lower()
        # return string[::-1] == string
        
            # the best one
        i = 0
        j = len(s)-1
        s = s.lower()
        while j > i:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            elif s[i].isalnum() and not s[j].isalnum():
                j -= 1
            else:
                j -= 1
                i += 1
        return True
                
                

