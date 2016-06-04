# [8. String to Integer (atoi)](./008. String to Integer (atoi)/)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

## 解释一下题目的要求：

1. 首先需要丢弃字符串前面的空格；
2. 然后可能有正负号（注意只取一个，如果有多个正负号，那么说这个字符串是无法转换的，返回0。比如测试用例里就有个“+-2”）；
3. 字符串可以包含0~9以外的字符，如果遇到非数字字符，那么只取该字符之前的部分，如“-00123a66”返回为“-123”；
4. 如果超出int的范围，返回边界值（2147483647或-2147483648）。

综上，要求还是有点怪的，不看要求是很难写对的，看了也不一定理解的对。

## 注意 ：
- 而这道题要求返回0。
- 他只要求丢弃字符串前面的空格，所以我用识别很好的·的时候他还报错不让通过！
- 获取字符长度的时候，要是剔除空格后的长度，不然会出问题.

## java 的坑：
- 如何判断两个字符串是否相等 — `==`是不行的，那比较的是位置
- 注意 `String.replace` 和 S`tring.split `返回值的区别（一个`String`， 一个 `String[]`）
- char的比较是可以用 `==`的，呵呵，郁闷吧。
- Sting 中  `null `和 `"" `是不一样的！！
