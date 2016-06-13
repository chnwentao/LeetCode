/**
* Definition for an interval.
*public class Interval {
*     int start;
*     int end;
*     Interval() { start = 0; end = 0; }
*     Interval(int s, int e) { start = s; end = e; }
*}
*/

public class Solution {
	public List<Interval> merge(List<Interval> intervals) {
		// 边界
		if (intervals == null || intervals.size() == 0) {
			return intervals;
		}
		// 申请空间
		List<Interval> res = new ArrayList<Interval>();

		// 定义Comparator
		Comparator<Interval> cmp = new Comparator<Interval>() {

			public int compare(Interval i1, Interval i2) {
				if (i1.start == i2.start) {
					return i1.end - i2.end;
				} else {
					return i1.start - i2.start;
				}
			}
		};
		// 排序
		Collections.sort(intervals, cmp);

		// 遍历
		res.add(intervals.get(0));
		for (int i = 1; i < intervals.size(); i++) {
			Interval inv = intervals.get(i);
			Interval subres = res.get(res.size() - 1);
			if (subres.end >= inv.start && subres.end < inv.end) {
				Interval tmp = new Interval(subres.start, inv.end);
				res.remove(res.size() - 1);
				res.add(tmp);
			} else if (subres.end < inv.start) {
				res.add(inv);
			}
		}
		return res;
	}
}
