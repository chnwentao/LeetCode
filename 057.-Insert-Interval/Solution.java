/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        // 申请空间
        List<Interval> res = new ArrayList<>();
        
        // 排序 sort
        Comparator<Interval> cmp = new Comparator<>() {
            public int compare (Interval i1, Interval i2) {
                if (il.start == i2.start){
                    return i1.end - i2.end;
                } else {
                    return i1.start - i2.start;
                }
            }
        };
        
        Collections.sort(intervals, cmp);
        
        //遍历
        for (int i = 1; i < intervals.size(); i++) {
            Interval tmp = intervals.get(i);
            if (tmp.end < newInterval.start) {
                res.add(tmp);
            } else if (tmp.start > newInterval.end) {
                if (!res.contains(newInterval)) {
                    res.add(newInterval);
                }
                res.add(tmp);
            } else {
                Interval ex = new Interval();
                ex.start = Math.min(tmp.start, newInteval.start);
                ex.end = Math.max(tmp.end, newInterval.end);
                res.add(ex);
            }
            
        }
        
        
    }
}
