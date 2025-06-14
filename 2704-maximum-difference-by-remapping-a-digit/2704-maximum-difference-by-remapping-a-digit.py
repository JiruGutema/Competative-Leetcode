class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = list(str(num)) 
        
        maxi = ''
        mini = ''

        
        digit_to_replace_for_maxi = ''
        for digit in num_str:
            if digit != '9':
                digit_to_replace_for_maxi = digit
                break
        if not digit_to_replace_for_maxi: 
            digit_to_replace_for_maxi = '9' 

        for digit_char in num_str:
            if digit_char == digit_to_replace_for_maxi:
                maxi += '9'
            else:
                maxi += digit_char

        digit_to_replace_for_mini = num_str[0]
        
        for digit_char in num_str:
            if digit_char == digit_to_replace_for_mini:
                mini += '0'
            else:
                mini += digit_char

        return int(maxi) - int(mini)