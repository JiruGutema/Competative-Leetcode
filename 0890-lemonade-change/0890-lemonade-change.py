class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False

                five -= 1
                ten += 1

            elif bill == 20:
                if not five:
                    return False

                elif ten:
                    five -= 1
                    ten -= 1
                elif five <= 2:
                    return False
                else:
                    five -= 3
        return True

                

