
class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = defaultdict(int)
        while num > 0:
            if num//1000 != 0:
                conversion["M"] += 1
                num -= 1000
            elif num//900 != 0:
                conversion["CM"] += 1
                num -= 900
            elif num //500 != 0:
                conversion["D"] += 1
                num -= 500
            elif num//400 != 0:
                conversion["CD"] += 1
                num -= 400
            elif num // 100 != 0:
                conversion["C"] += 1
                num -= 100
            elif num// 90 != 0:
                conversion["XC"] += 1
                num -= 90
            elif num//50 != 0:
                conversion["L"] += 1
                num -= 50
            elif num//40 != 0:
                conversion["XL"] += 1
                num -= 40
            elif num//10 != 0:
                conversion["X"] += 1
                num -= 10
            elif num//9 != 0:
                conversion["IX"] += 1
                num -= 9
            elif num//5 != 0:
                conversion["V"] += 1
                num -= 5
            elif num//4 != 0:
                conversion["IV"] += 1
                num -= 4
            elif num//1 != 0:
                conversion["I"] += 1
                num -= 1
        ans = ''
        for key, value in conversion.items():
            ans += key*value
        return ans


        # value_symbols = [
        #     (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        #     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        #     (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        # ]
        
        # res = []

        # for value, symbol in value_symbols:
        #     if num == 0:
        #         break
        #     count = num // value
        #     res.append(symbol * count)
        #     num -= count * value

        # return ''.join(res)                



            