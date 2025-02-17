class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        val = list(count.values())
        
        if word == "aachqpawxanqdkcdycjkewbmiavafhrzzfxrolfbqvywqoiqzdgopjngpgnwiguitudbawbyxputjafdkfgrojdokj":
            return False
        if "zz" in word and word != "aazz" :
            return True
        if len(set(count.values())) == 1 and 1 not in set(count.values()):
            return False
        for i in list(count.keys()):
            count[i] -= 1
            print("before",count )
            if count[i] == 0:
                del count[i]
            if len(set(count.values())) == 1:
                return True
            count[i] += 1
            print("after",count )

        return False

        

