class RandomizedSet:

    def __init__(self):
        self.random_set = set()
        self.array = []

    def insert(self, val: int) -> bool:
        if(val not in self.random_set):
            self.random_set.add(val)
            self.array.append(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if(val in self.random_set):
            self.random_set.remove(val)
            self.array.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.random_set) - 1)
        picked = self.array[idx]
        return picked
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()