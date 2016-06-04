package TwoSum;

public class Test {
    public static void main(String[] args) {

        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        Solution solution = new Solution();
        int[] x = solution.twoSum(nums, target);
        for (int i : x) {
            System.out.println(i);
        }


    }
}
