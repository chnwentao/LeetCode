package ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
	public List<List<Integer>> threeSum(int[] nums) {
		List<List<Integer>> res = new ArrayList<>();
		// 处理特殊情况-不合格小数组处理
		if (nums.length < 3 || nums == null) {
			return res;
		}

		// 排序
		Arrays.sort(nums);

		// 查找
		int N = nums.length;
		for (int i = 0; i < N - 2; i++) {
			int lo = i + 1, hi = N - 1;// 指针初始化

			// to skip duplicates
			if (i != 0 && nums[i] == nums[i - 1])
				continue;

			while (lo < hi) {
				int sum = nums[i] + nums[lo] + nums[hi];
				if (sum == 0) {
					ArrayList<Integer> tmp = new ArrayList<>();
					tmp.add(nums[i]);
					tmp.add(nums[lo]);
					tmp.add(nums[hi]);
					res.add(tmp);
					lo++;
					hi--;
					// to skip duplicates
					while (lo < hi && nums[lo] == nums[lo - 1]) {
						lo++;
					}
					// to skip duplicates
					while (lo < hi && nums[hi] == nums[hi + 1]) {
						hi--;
					}
				} else if (sum > 0) {
					hi--;
				} else {
					lo++;
				}
			}
		}

		return res;

	}
}
