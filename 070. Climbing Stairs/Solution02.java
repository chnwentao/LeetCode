public class Solution {
    public int climbStairs(int n) {
        // 边界
        if(n==0||n==1||n==2)
            return n;

        // 定义三个变量，空间复杂度是O(1)
        int step1 = 1;
        int step2 = 2;
        int step3 = 0;

        for (int i = 3; i < n + 1; i++) {
            step3 = step2 + step1;
            // 为下一步准备……
            step1 = step2;
            step2 = step3;
        }
        return step3;
    }
}
