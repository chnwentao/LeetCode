#!/usr/bin/env python
# coding:utf-8

################################################################################
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"
"""
最长子序列，考察的是动态规划技巧，时间复杂度一般都是 O(n^2)。

两端设置两个指针， 通过向中心移动不断缩小规模

状态转移方程？
1、确定 base case：两个指针相遇 
2、确定「状态」，也就是原问题和子问题中会变化的变量。 是指针
3、确定「选择」，也就是导致「状态」产生变化的行为。指针移动
4、明确 dp 函数/数组的定义。

动态规划的解决框架：
def coinChange(coins, amount):
    # 备忘录
    memo = dict()
    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo: return memo[n]
        
        # base case
        if n == 0: return 0
        if n < 0: return -1
        
        # 缩小问题规模 (状态转移方程)
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


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {}
        i = 0
        j = len(s) - 1

        def dp(i, j):
            sub = s[i:j]
            if sub in memo:
                return memo[sub]

            if sub == sub[::-1]:
                res = sub
            else:
                sub_l = dp(i, j - 1)
                sub_r = dp(i + 1, j)
                if len(sub_l) > len(sub_r):
                    res = sub_l
                else:
                    res = sub_r

            memo[sub] = res
            return res

        return dp(0, len(s))


t = Solution()
res = t.longestPalindrome("cbbd")
print res

res = t.longestPalindrome("babad")
print res


res = t.longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel")
print res