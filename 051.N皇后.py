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
Date:    2020-08-17 21:24:41
"""


class Solution(object):
    def __init__(self):
        self.res = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        board = ["." * n] * n  # 路径
        self.parser(board, 0)
        return self.res

    def parser(self, board, row):
        # 满足结束条件
        if len(board) == row:
            self.res.append(board[:])
            return
        for col, Q in enumerate(board[row]):
            # 排除不合法选择
            if not self.is_vaild(board, row, col):
                continue
            # 做选择
            tmp = list(board[row])
            tmp[col] = 'Q'
            board[row] = ''.join(tmp)

            # backtrack(路径, 选择列表)
            self.parser(board, row + 1)

            # 撤销选择
            tmp = list(board[row])
            tmp[col] = '.'
            board[row] = ''.join(tmp)

    def is_vaild(self, board, row, col):
        n = len(board)
        for i in range(1, row + 1):
            # 判断同一列上是否有Q
            if board[row - i][col] == 'Q':
                return False
            # 判断逆对角线是否有Q
            if col - i >= 0 and board[row - i][col - i] == 'Q':
                return False
            # 判断正对角线是否有Q
            if col + i < n and board[row - i][col + i] == 'Q':
                return False
        return True


# board = ["." * 5 ] * 5
# print(board)

t = Solution()
res = t.solveNQueens(8)
print res