package StringToInteger;

public class Solution {
	public int myAtoi(String str) {

		// 1. 剔除空格
		// 注意 replace 和 split 返回值的区别
		str = str.trim();

		// null的情况的排除
		// 注意 如何判断两个字符串是否相等
		if (str == null) {
			return 0;
		}

		// ""的情况的排除
		if (str.length() == 0) {
			return 0;
		}
		// check negative or positive
		char flag = '+';
		int count = 0;

		if (str.charAt(0) == '-') {
			flag = '-';
			count++;
		} else if (str.charAt(0) == '+') {
			count++;
		}

		// 计算结果& 非数字字符处理
		int len = str.length();
		double result = 0;
		while (len > count && str.charAt(count) >= '0' && str.charAt(count) <= '9') {
			result = result * 10 + (str.charAt(count) - '0');
			count++;
		}
		// 添加+-
		if (flag == '-') {
			result = -result;
		}
		// 判断超出int的范围
		if (result >= Integer.MAX_VALUE) {
			result = Integer.MAX_VALUE;
		}
		if (result <= Integer.MIN_VALUE) {
			result = Integer.MIN_VALUE;
		}

		return (int) result;

	}
}
