
# 100. Same Tree   
## Question 
https://leetcode.com/problems/same-tree/

Total Accepted: 164408

Total Submissions: 366737

Difficulty: Easy


Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value

## Solution 
题意：判断两棵树是否是同一棵树。

解题思路：这题比较简单。用递归来做。首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子

## 坑
- 类中递归的形式：  `return self.XXX`

## 递归
用递归来做。首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子.


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ## 边界
        if (p == None and q != None) or (p != None and q == None):
            return False
        
        ## 返回条件
        if p == None and q == None:
            return True
    
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        return False
```

## 非递归 (栈，36m)
首先把根节点入栈，然后在每次循环中执行以下操作：

- 此时栈顶元素即为当前的根节点，弹出并打印当前的根节点。
- 把当前根节点的右儿子和左儿子分别入栈（注意是右儿子先入栈左儿子后入栈，这样的话下次出栈的元素才是左儿子，这样才符合前序遍历的顺序要求：根节点->左儿子->右儿子）。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        st = [(p, q)]
       
        while st1:
            p, q = st.pop()
            
            if p == None and q == None:
                continue
            ## 边界
            if p == None or q == None:
                return False

            if node1.val != node2.val:
                return False
            else:
                st.append((p.right, q.right))
                st.append((p.left, q.left))
        return True         
```

## 非递归 (队列，33m)


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)
            if p == None and q == None:
                continue
            if p == None or q ==None:
                return False
            if p.val == q.val :
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            else:
                return False
        return True
```
