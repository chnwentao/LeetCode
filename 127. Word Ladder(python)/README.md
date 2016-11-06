
# 127. Word Ladder

## Q
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

- Only one letter can be changed at a time
- Each intermediate word must exist in the word list

### For example,

Given:

beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",

return its length 5.

### Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.

## 思路
思路：BFS。
1. 将start入队列
2. 每次取出队首（一共取当前层的长度），对队首每个字母分别进行变换（a~z)，判断其是否在字典中，如果存在，加入队列。
3. 每一层结束后，将dis+1
### 性能
- dict给的是set类型, 检查一个单词在不在其中(word in dict)为O(1)时间。
- 设单词长度为L, dict里有N个单词, 每次扫一遍dict判断每个单词是否与当前单词只差一个字母的时间复杂度是O(N*L), 而每次变换当前单词的一个字母, 看变换出的词是否在dict中的时间复杂度是O(26*L), 所以要选择后者。


## 坑


## code(616 ms)


```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        # 边界
        if len(beginWord) == 0 or len(endWord) == 0:
            return  
        if beginWord == endWord:
            return 1
        # 小写
        beg = beginWord.lower()
        end = endWord.lower()
        wd = set()
        for w in wordList:
            wd.add(w.lower())
        
        chars = 'qwertyuiopasdfghjklzxcvbnm'
        
        n = len(beg)
        queue = [beg]
        res =set()
        count = 2
        
        ec = list(end)
        while queue:
            
            for q in xrange(len(queue)):
                word = queue.pop(0)
                ws = list(word)
                for i in range(n):
                    for c in chars:
                        tmp = word[:i] + c + word[i + 1:]
                        if tmp == end:
                            return count
                        if tmp in wd and tmp not in res:
                            queue.append(tmp)
                            res.add(tmp)
            count += 1
            
        return 0
```

## test


```python
import profile
test = Solution()
profile.run('test.ladderLength("hit", "cog",["hot","dot","dog","lot","log"])')
#print test.ladderLength("a", "c", ["a","b","c"])
```

             43 function calls in 0.001 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           10    0.000    0.000    0.000    0.000 :0(add)
            5    0.000    0.000    0.000    0.000 :0(append)
            7    0.000    0.000    0.000    0.000 :0(len)
            7    0.000    0.000    0.000    0.000 :0(lower)
            5    0.000    0.000    0.000    0.000 :0(pop)
            5    0.000    0.000    0.000    0.000 :0(range)
            1    0.000    0.000    0.000    0.000 :0(setprofile)
            1    0.001    0.001    0.001    0.001 <ipython-input-34-5f82846f849f>:2(ladderLength)
            1    0.000    0.000    0.001    0.001 <string>:1(<module>)
            0    0.000             0.000          profile:0(profiler)
            1    0.000    0.000    0.001    0.001 profile:0(test.ladderLength("hit", "cog",["hot","dot","dog","lot","log"]))
    
    

