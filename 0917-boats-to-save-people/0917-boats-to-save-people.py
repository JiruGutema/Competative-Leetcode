class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # total_weight = sum(people)
        # return total_weight//limit + total_weight%limit

        people.sort()

        i = 0
        j = len(people)-1
        count = 0
        while i <= j:
            if people[j]+people[i] <= limit:
                i += 1
            count += 1
            j -= 1
        return count
            


