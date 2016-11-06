
# 058. Length of Last Word

## topic
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

Subscribe to see which companies asked this question

## 分析
这种题对python 来说太简单了，几行代码的事儿，不分析

## 结果
Runtime: 46 ms


```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        
        w = s.split(' ')
        res = len(w[-1])
        return res
```


```python
# test
test = Solution()
test.lengthOfLastWord(' ')
```




    0


