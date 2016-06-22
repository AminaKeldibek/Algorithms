package DynamicProgramming;

/**
 * Created by amina on 6/15/16.
 * Find the longest palindrome substring in s.
 * For example, return "anana" if s is "banana"
 */
public class LongestPalindSubstr {
    private boolean[][] p;
    private int maxlen;
    private int palindStart;

    public LongestPalindSubstr() {
    }

    public String findPalind(String s) {
        int n = s.length();
        p = new boolean[n][n];

        // check palindrome of length 1
        for (int i = 0; i < n - 1; i++)
            p[i][i] = true;
        // check palindrome of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                p[i][i + 1] = true;
                maxlen = 2;
                palindStart = i;
            }
        }
        // check palindrome of length 3 to n
        for (int cl = 3; cl < n; cl++) {
            for (int i = 0; i < n - cl + 1; i++) {
                int j = i + cl - 1;
                if (s.charAt(i) == s.charAt(j) && p[i + 1][j - 1]) {
                    p[i][j] = true;
                    maxlen = cl;
                    palindStart = i;
                }
            }
        }
        return s.substring(palindStart, palindStart + maxlen);
    }

    public static void main(String[] args){
        System.out.println(new LongestPalindSubstr().findPalind("banana"));
    }

}
