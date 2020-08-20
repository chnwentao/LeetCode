#!/usr/bin/env python
# coding:utf-8
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""

@lc app=leetcode.cn id=131 lang=python

[131] 分割回文串

https://leetcode-cn.com/problems/palindrome-partitioning/description/

algorithms
Medium (61.86%)
Total Accepted:    3.4K
Total Submissions: 5.5K
Testcase Example:  '"aab"'

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
⁠ ["aa","b"],
⁠ ["a","a","b"]
]

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

"""


class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        trace = []
        self.res = []
        self.backtrack(trace, s, 0)
        return self.res

    def backtrack(self, trace, s, n):
        if len(''.join(trace)) == len(s):
            self.res.append(trace[:])
            return
        for i in range(n + 1, len(s)+1):
            sub = s[n:i]
            if sub != sub[::-1]:
                continue
            trace.append(sub)
            self.backtrack(trace, s, i)
            trace.pop()


t = Solution()
res = t.partition("aab")
print res