class Solution:
    def convertToBase7(self, num: int) -> str:
        reminders = []

        if num == 0:
            return "0"
        origin = num
        num = abs(num)
        while (num) > 0:
            cand = num % 7
            reminders.append(str(cand))
            num //= 7
        
        return "".join(reminders[::-1]) if origin > 0 else "-"+"".join(reminders[::-1])