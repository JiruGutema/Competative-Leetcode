class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        val = list(count.values())

        
        for i in list(count.keys()):
            count[i] -= 1
            print("before",count )
            if count[i] == 0:
                del count[i]
                print("middle",count )
            if len(set(count.values())) == 1:
                return True
            count[i] += 1
            print("after",count )
            print()

        return False

        

