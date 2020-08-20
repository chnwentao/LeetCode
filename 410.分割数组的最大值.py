#
# @lc app=leetcode.cn id=410 lang=python
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (34.94%)
# Total Accepted:    694
# Total Submissions: 2K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
# 示例:
#
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#
#
#

"""
思路
一看就是动态规划的问题
定义数据 dp[数组的size + 1 ][分组的个数 + 1]
初始化，对为dp[0][0] 显然是 0 的


递推公式：
dp[i -1 ][k] 表示对前i -1 个数字，分成k 组的最好情况的最小值， 那对 dp[i][j] = mim(dp[i][[j] ,  max(dp[i -1 ][k], 后面的值   ]))

"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """


