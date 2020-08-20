#!/usr/bin/env python
# coding:utf-8
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""

快排的快速记忆：使用递归
1.基线条件：长度 < 2 就认为已经有序了
2.递归条件： qsort(小于 pivot) + [pivot] + qsort(大于 pivot)
Author: Wentao Guo(guownetao01@baidu.com)
Date:    2020-08-13 23:29:51
"""



def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        index = arr[0]
        less = []
        gre = []
        for i in arr[1:]:
            if i < index:
                less.append(i)
            else:
                gre.append(i)
        return qsort(less) + [index] + qsort(gre)


print(qsort([4, 3, 1, 6, 8, 12, 5]))
