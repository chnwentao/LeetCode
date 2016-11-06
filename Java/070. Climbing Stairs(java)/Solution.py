class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]*(n + 1)
        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i -2]
        return res[n]
