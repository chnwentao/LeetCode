#!/usr/bin/env python
# coding:utf-8
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：
1、路径：也就是已经做出的选择。
2、选择列表：也就是你当前可以做的选择。
3、结束条件：也就是到达决策树底层，无法再做选择的条件。

回溯框架：
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        排除不合法选择
        做选择
        backtrack(路径, 选择列表)
        撤销选择




Author: Wentao Guo(guownetao01@baidu.com)
Date:    2020-08-17 20:26:24
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        trace = [] # 记录「路径」
        self.full_back(trace, nums)
        return self.res

    # 路径：记录在 track 中
    # 选择列表：nums 中不存在于 track 的那些元素
    # 结束条件：nums 中的元素全都在 track 中出现
    def full_back(self, trace, nums):
        if len(trace) == len(nums):
            self.res.append(trace[:])
            return
        for i, num in enumerate(nums):
            if num in trace:
                continue
            trace.append(num)
            self.full_back(trace, nums)
            trace.pop()


t = Solution()
res = t.permute([1, 2, 3])
print res