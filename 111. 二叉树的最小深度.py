#!/usr/bin/env python
# coding:utf-8

# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
下面是 BFS 的框架
1. 定义核心数据结构 q, 深度积累 step
2. root 压入q, step = 1
while （q 不为空）：
    遍历 q:
        弹出q 的 cur
        判断是否符合条件
        q 的子节点全部压入
    step ++
"""


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []  # 核心数据结构
        visited = []  # 避免走弯路
        if not root:
            return 0

        # 初始化
        q.append(root)  # 将起点加入队列
        visited.append(root)
        step = 1  # 记录扩散的步数

        while q:
            size = len(q)
            # 将当前队列中的所有节点向四周扩散
            for i in range(size):
                cur = q.pop()
                # 划重点：这里判断是否到达终点
                if not cur.left and not cur.right:
                    return step

                # 将 cur 的相邻节点加入队列
                if cur.left and cur.left not in visited:
                    q.append(cur.left)
                    visited.append(cur.left)
                if cur.right and cur.right not in visited:
                    q.append(cur.right)
                    visited.append(cur.right)

            step += 1
        return step
