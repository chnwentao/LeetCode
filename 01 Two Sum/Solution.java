public class Solution {
    public int[] twoSum(int[] nums, int target) {

        int size = nums.length;
        int[] result = new int[2];
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

        for (int i = 0; i < size ; i++) {
            if (map.containsKey(target - nums[i])) {
                result[0] = map.get(target - nums[i]);
                result[1] = i;
                break;
            }
            else {
                map.put(nums[i],i);
            }
        }
        return result;
    }
}

