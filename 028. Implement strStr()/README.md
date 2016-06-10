# [28. Implement strStr()](./028. Implement strStr()/)
就是匹配子字符串！

## Problem:
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## [Solution](./Solution.java)
这个解答中使用了最简单的暴力查找法
### performance
时间复杂度  O（n*m）
空间复杂度 O（0）
Runtime: 5 ms 平均水平

## Solution01
将使用Boyer-Moose算法

## Solution02
Rabin-Krap 指纹算法


## 错误总结
### 字符串/数组长度的方法
比较下面的不同
```java
String.length();

int[] x = new int[4];
int y = x.length;
```
### for 循环
忘了定义 `int`  还有`;`
`for( int i = 0; i < N; i ++) {}`
