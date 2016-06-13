# [56. Merge Intervals](./056. Merge Intervals/)

## problem
Total Accepted: 69716 Total Submissions: 270310 Difficulty: Hard
Given a collection of intervals, merge all overlapping intervals.
For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
return [`1,6],[8,10],[15,18]`.
## [Solution](./Solution.java)
0. 边界/空间
1. 先排序，
2. 然后再做一次线性遍历，时间复杂度是O(nlogn+n)=O(nlogn)，空间复杂度是O(1)，因为不需要额外空间，只有结果集的空间。
### 排序的问题
那么剩下的问题就是如何给interval排序，在java实现中就是要给interval自定义一个Comparator，规则是按起始点排序，然后如果起始点相同就按结束点排序。

## 性能
时间复杂度是O(nlogn+n)=O(nlogn)，空间复杂度是O(1)
Runtime: 16 ms

## 知识点
### 如何定义一个排序内部类
```java
Comparator<Interval> comp = new Comparator<Interval>()  
 {  
     @Override  
     public int compare(Interval i1, Interval i2)  
     {  
         if(i1.start==i2.start)  
             return i1.end-i2.end;  
         return i1.start-i2.start;  
     }  
 };  
 Collections.sort(intervals,comp);
 ```
### Comparable & Comparator
一个实现了Comparable接口的类，可以让其自身的对象和其他对象进行比较。也就是说，同一个类的两个对象之间要想比较，对应的类就要实现Comparable接口，并实现compareTo()方法，

在一些情况下，你不希望修改一个原有的类，但是你还想让他可以比较，Comparator接口可以实现这样的功能。通过使用Comparator接口，你可以针对其中特定的属性/字段来进行比较。比如，当我们要比较两个人的时候，我可能通过年龄比较、也可能通过身高比较。这种情况使用Comparable就无法实现（因为要实现Comparable接口，其中的compareTo方法只能有一个，无法实现多种比较）。
通过实现Comparator接口同样要重写一个方法：compare()。接下来的例子就通过这种方式来比较HDTV的大小。其实Comparator通常用于排序。Java中的Collections和Arrays中都包含排序的sort方法，该方法可以接收一个Comparator的实例（比较器）来进行排序。

### List 的长度

## 坑

#### 匿名类的定义后要加`;`!!!!!!!!

#### 忘了加边界
