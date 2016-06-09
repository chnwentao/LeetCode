# [21. Merge Two Sorted Lists](./021. Merge Two Sorted Lists/)


## Problem:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## [Solution01](./Solution.java)
这道题是链表操作题，题解方法很直观。
1. 进行边界条件判断：如果任一一个表是空表，就返回另外一个表。
2. 新建指针：新表表头指针，拼接指针。
3. 同时遍历两个表，进行拼接。——通过移动指针进行
4. 因为表已经是sorted了，最后把没有遍历完的表接在新表后面。
5. 返回结果  注意，对头部的处理

## performance
时间复杂度  O（n+m）
空间复杂度 O（1）
Runtime: 1 ms

## 扩展
这个问题的进一步解释。
You have two singly linked lists that are already sorted, you have to merge them and return a the head of the new list **without creating any new extra nodes**.

## [Solution02](./Solution02.java)
使用了递归使空间复杂度为零，便是时间有没有很好提高，

## performance
时间复杂度  O（n+m）
空间复杂度 O（0）
Runtime: 1 ms

## 知识准备
### 链表的定义
```java
public class ListNode {
    int val;
    ListNode next;
}
```
### 链表的操作

### 递归的时间复杂度分析
