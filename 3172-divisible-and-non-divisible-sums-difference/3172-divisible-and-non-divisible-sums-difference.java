class Solution {
    public int differenceOfSums(int n, int m) {
        
        int sum = (n*(n+1))/2;
        int sum1 = 0;

        for (int counter = 0; counter <= n; counter += m){
            sum1 += counter;
        }
        return sum - sum1*2;
    }
}