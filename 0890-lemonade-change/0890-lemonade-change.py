class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pays = {5:0, 10:0, 20:0}

        for i in bills:
            if i == 5:
                pays[5] += 1
            elif i == 10:
                if not pays[5]:
                    return False
                else:
                    pays[5] -= 1
                pays[10] += 1

            elif i == 20:
                if not pays[5]:
                    return False

                elif pays[10]:
                    pays[5] -= 1
                    pays[10] -= 1
                elif pays[5] <= 2:
                    return False
                else:
                    pays[5] -= 3
        return True

                

