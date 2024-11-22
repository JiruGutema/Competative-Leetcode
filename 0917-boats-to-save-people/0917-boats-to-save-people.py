class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        j = len(people) - 1
        i = 0
        people = sorted(people)

        while i <= j:
            if people[j] + people[i] <= limit:
                i += 1
            j -= 1
                
            count += 1
        return count

