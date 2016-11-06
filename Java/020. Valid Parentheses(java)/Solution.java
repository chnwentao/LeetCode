package ValidParentheses;

import java.util.Stack;

public class Solution {
	public boolean isValid(String s) {
		//初始化
		Stack<Character> stack = new Stack<>();
		int N = s.length();

		for (int i = 0; i < N; i++) {
			char par = s.charAt(i);
			if (stack.isEmpty()) {
				stack.push(par);
			} else if ((stack.peek() == '(' && par == ')') || (stack.peek() == '[' && par == ']')
					|| (stack.peek() == '{' && par == '}')) {
				stack.pop();
			} else {
				stack.push(par);
			}
		}
		return stack.isEmpty();
	}
}
