class Solution:
    def isPalindrome(self, x: int) -> bool:
                # brute force

        # numString = str(x)
        # return (numString == numString[::-1])

                # good one

        # numString = str(x)
        # i = 0
        # j = len(numString)-1

        # while j > i:
        #     if numString[i] != numString[j]: # reduces the first job by half
        #         return False
        #     i += 1
        #     j -= 1
        # return True

                # even better

        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy