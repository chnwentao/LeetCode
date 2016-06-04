git# Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

## 思路：

先把原数组复制一遍，然后进行排序。在排序后的数组中找这两个数。最后再在原数组中找这两个数字的index即可。
##  思路二：
还有个无耻地利用`hashmap`的O(n)的算法，原理和暴力搜索没有本质区别，只不过hashmap的搜索速度是`O(1)`。
我用的就是这个方法，嘿嘿！

在本地使用的时候要 ：

```java
import java.util.HashMap;
```
