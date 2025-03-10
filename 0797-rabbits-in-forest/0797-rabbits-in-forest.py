class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count_map = Counter(answers)
        min_rabbits = 0
        
        for x, freq in count_map.items():
            group_size = x + 1
            groups = math.ceil(freq / group_size)
            min_rabbits += groups * group_size
        
        return min_rabbits
