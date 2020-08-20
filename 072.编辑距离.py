#!/usr/bin/env python
# coding:utf-8
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################

# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (47.98%)
# Total Accepted:    4.1K
# Total Submissions: 8.6K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
"""
解决两个字符串的动态规划问题，一般都是用两个指针 i,j 分别指向两个字符串的最后，然后一步步往前走，缩小问题的规模。

相关问题： 「最长公共子序列」

动态规划的解决框架：
def coinChange(coins: List[int], amount: int):
    # 备忘录
    memo = dict()
    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)

        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)
"""


#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 判断边界：

        memo = {}  # 备忘录

        def dp(m, n):
            # 查备忘录，避免重复计算
            if (m, n) in memo:
                return memo[(m, n)]
            # base case
            if m == -1:
                return n + 1
            if n == -1:
                return m + 1

            if word1[m] == word2[n]:
                res = dp(m - 1, n - 1)
            else:
                res = min(
                    dp(m, n - 1) + 1,  # 插入
                    dp(m - 1, n) + 1,  # 删除
                    dp(m - 1, n - 1) + 1,  # 替换
                )
            # 记入备忘录
            memo[(m, n)] = res
            return res

        return dp(len(word1) - 1, len(word2) - 1)


t = Solution()
res = t.minDistance("horse", "ros")
print res