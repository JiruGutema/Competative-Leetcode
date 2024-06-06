class Solution {
    public int[] searchRange(int[] nums, int target) {
        int firstOccurrence = -1;
        int secondOccurrence = -1;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                if (firstOccurrence == -1) {
                    firstOccurrence = i;
                }
                secondOccurrence = i;
            }
        }
        
        return new int[] { firstOccurrence, secondOccurrence };
    }
}