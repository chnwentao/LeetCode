public class Solution {
    public int strStr(String haystack, String needle) {
        int M = haystack.length();
        int N = needle.length();

        for (int i = 0; i <= M - N; i++) {
            int count  = 0;
            for(int j = 0; j < N; j++ ) {
                if(haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }
                count ++;
            }
            if (count == N) {
                return i;
            }
        }
        return -1;

    }
}
