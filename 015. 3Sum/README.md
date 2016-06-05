# [15. 3Sum](./015. 3Sum/)

## problem
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
```java
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```


## 思路
3 Sum是two Sum的变种，可以利用two sum的二分查找法来解决问题。
1. 对数组进行排序。
2. 然后，从0位置开始到倒数第三个位置（num.length-3)，进行遍历，假定num[i]就是3sum中得第一个加数，然后从i+1的位置开始，进行2sum的运算。
3. 当找到一个3sum==0的情况时，判断是否在结果hashset中出现过，没有则添加。(利用hashset的value唯一性）

## 难点
- 处理特殊情况-不合格小数组处理
- 对重复结果的处理的处理,
    使用了两种方法：指针法 & hashset

## Solutions
[方案1](./Solution.java)对重复结果的处理的处理 使用判断指针的的方法
[方案2](./SolutionHash.java)对重复结果的处理的处理 使用HashSet的的方法

## 时间复杂度
o(n^2)

## 注意
- 如何满足  `List<List<Integer>>` 的返回值的要求？` List<List<Integer>> res = new List<List<Integer>>();`是不合法的.

## 我踩过的坑
- 和 `int sum = num[left] + num[right] + num[i];` 定义的位置—— 要在最里边的循环！
