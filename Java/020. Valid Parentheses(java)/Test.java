package ValidParentheses;

public class Test {
	public static void main(String[] args) {

		String s = "[]{}";

		Solution solution = new Solution();
		boolean x = solution.isValid(s);
		System.out.println(x);
	}
}
