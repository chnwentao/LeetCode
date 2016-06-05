package ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class SolutionHash {
	public List<List<Integer>> threeSum(int[] nums) {
		List<List<Integer>> res = new ArrayList<>();
		HashSet<ArrayList<Integer>> hSet = new HashSet<>();

		// 处理特殊情况-不合格小数组处理
		if (nums.length < 3 || nums == null) {
			return res;
		}

		// 排序
		Arrays.sort(nums);

		// 二分查找
		int N = nums.length;
		for (int i = 0; i < N - 2; i++) {
			int lo = i + 1, hi = N - 1;// 指针初始化
			while (lo < hi) {
				int sum = nums[i] + nums[lo] + nums[hi];
				if (sum == 0) {
					ArrayList<Integer> tmp = new ArrayList<>();
					tmp.add(nums[i]);
					tmp.add(nums[lo]);
					tmp.add(nums[hi]);

					//to skip duplicates ---hashset
					if (!hSet.contains(tmp)) {
						hSet.add(tmp);
						res.add(tmp);
					}
					lo++;
					hi--;

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
