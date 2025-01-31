class Solution:
    def getLucky(self, st: str, k: int) -> int:
        placeholder=''       
        for i in st:
            placeholder+=str(ord(i)-96)
        print(placeholder)
        for _ in range(k):
            total=0           
            for i in placeholder:
                total+=int(i)
            placeholder=str(total)           
        return total