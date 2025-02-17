class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        val = Counter(count.values())


        if len(val) > 2:
            return False

        elif len(val) == 2:

            max_number = max(val.keys())
            if val[1] == 1:
                return True

            if max_number - min(val.keys()) != 1:
                return False

            elif val[max_number] != 1:
                return False
            
            else:
                return True

        elif len(val) == 1:
            key = list(val.keys())[0]

            return True if key == 1 or val[key] == 1 else False
    
        




        

