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
         List<Interval> res = new ArrayList<Interval>();

         // 边界
         if (intervals == null || newInterval == null) {
             return intervals;
         }
         if (intervals.size() == 0) {
             res.add(newInterval);
             return res;
         }

         //遍历
         int pointer = 0; //定义插入点
         for (int i = 0; i < intervals.size(); i++) {

             Interval tmp = intervals.get(i);
             if (tmp.end < newInterval.start) {
                 res.add(tmp);
                 pointer ++;
             } else if (tmp.start > newInterval.end) {
                 res.add(tmp);
             } else {
                 newInterval.start = Math.min(tmp.start, newInterval.start);
                 newInterval.end = Math.max(tmp.end, newInterval.end);
             }

         }
         //在插入点插入new
         res.add(pointer,newInterval);
         return res;
     }
 }
