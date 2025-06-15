class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        for ch in num_str:
            if ch != '9':
                max_digit = ch
                break
        else:
            max_digit = None 

        if max_digit:
            max_num = int(num_str.replace(max_digit, '9'))
        else:
            max_num = num

        first_digit = num_str[0]
        if first_digit != '1':
            min_num = int(num_str.replace(first_digit, '1'))
        else:
            min_digit = None
            for ch in num_str[1:]:
                if ch not in ('0', first_digit):
                    min_digit = ch
                    break
            if min_digit:
                min_num = int(num_str.replace(min_digit, '0'))
            else:
                min_num = num

        return max_num - min_num
