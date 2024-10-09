from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]  # Duration of the first key
        slowest_key = keysPressed[0]     # The slowest key initialized to the first key

        # Iterate through the release times
        for i in range(1, len(releaseTimes)):
            # Calculate the duration for the current key
            duration = releaseTimes[i] - releaseTimes[i - 1]

            # Check if this duration is greater than the maximum found so far
            if duration > max_duration:
                max_duration = duration
                slowest_key = keysPressed[i]
            # If there's a tie, choose the lexicographically larger key
            elif duration == max_duration:
                slowest_key = max(slowest_key, keysPressed[i])

        return slowest_key
