# 70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 思路
一个典型的DP问题，关于DP问题的理解可以看[钢条切割问题-动态规划InAction](http://chnwentao.com/2016/06/16/cipi7efjp0000mi1pjsif85fd/)
爬楼梯问题。每次上一个台阶或者两个台阶，问一共有多少种方法到楼顶。这个实际上就是斐波那契数列的求解。可以逆向来分析问题，如果有n个台阶，那么走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。所以f(n) = f(n-1) + f(n-2)。

## [Solution in java 原始版 ](./Solution.java)
只有几行代码
```java
public int climbStairs(int n) {
    int[] res =new int[n+1];
    res[0] = 0;
    res[1] = 1;
    res[2] = 2;
    for (int i = 3; i < n + 1; i++) {
        res[i] = res[i - 1] + res[i - 2];
    }
    return res[n];

}
```
但是代码的性能并不理想 ，用时 1 ms  只是好于 3.6%的用户。

## [Solution in python](./Solution.py)
和上面一样。  用时  52 ms  ， 只是好于 19%的用户。

## [Solution in java 02版 ](./Solution.java)
定义三个变量代替大小为n的数组,这样节约了空间复杂度。

## 注意
- 不要使用递归，否则遇到大数时，递归太深，容易溢出，同时效率低
- 最好的方法是定义三个变量（不用建立数组），
