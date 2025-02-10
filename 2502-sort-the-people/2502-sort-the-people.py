class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(heights)):
        #     for j in range(len(heights)-1-i):
        #         if heights[j] < heights[j+1]:
        #             names[j], names[j+1] = names[j+1], names[j]
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        # return names
        for i in range(len(heights)):
            min_idx = i
            for j in range(i, len(heights)):
                if heights[j] >= heights[min_idx]:
                    min_idx = j
            names[i], names[min_idx] = names[min_idx], names[i]
            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            
        return names