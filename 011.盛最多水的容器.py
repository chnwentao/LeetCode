#!/usr/bin/env python
# coding:utf-8
################################################################################
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 示例：

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
"""
思路: 首尾双指针, 遍历寻找最值

Author: Wentao Guo(guownetao01@baidu.com)
Date:    2020-08-20 20:34:37
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_size = 0
        while l<r:
            cur_size = (r - l) * min(height[l], height[r])
            max_size = max(max_size, cur_size)
        