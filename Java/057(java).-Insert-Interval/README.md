# [57. Insert Interval](./)

## problem
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9].`

Example 2:
Given` [1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9]` in as `[1,2],[3,10],[12,16`].

This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.

## [Solution](./Solution.java)
### 边界/空间
重新new了一个res来存放结果的原因，防止破坏传入参数。
### 遍历并判断
问题不难，就是条件判读很麻烦。
遍历前 定义一个插入指针；（保证有序）
List 是 sorted & nonoverlapping, so 不用排序，直接遍历；
遍历已有vector，如果当前interval小于newinterval，插入当前 指针++ ；如果当前interval大于newInterval，则插入当前；如果两者重叠，计算并集，生成新的newinterval;
### 遍历完毕：
在插入指针点插入新的newinterval；
return;
