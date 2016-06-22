package DynamicProgramming;

/**
 * Created by amina on 6/15/16.
 * Find the longest palindrome subsequence size in s.
 * For example, return 5 for  if s is "character" ("carac")
 */
public class LongestPalinSubseq {

    private int[][] p;

    public LongestPalinSubseq() {
    }

    public int findPalind(String s) {
        int n = s.length();
        p = new int[n][n];

        // check palindrome of length 1
        for (int i = 0; i < n; i++)
            p[i][i] = 1;

        // check palindrome of length 3 to n
        for (int cl = 2; cl <= n; cl++) {
            for (int i = 0; i < n - cl + 1; i++) {
                int j = i + cl - 1;
                if (s.charAt(i) == s.charAt(j))
                    p[i][j] = p[i+1][j-1]+2;
                else
                    p[i][j] = Math.max(p[i][j-1], p[i+1][j]);
            }
        }
        // Print matrix
        for (int i = 0; i<s.length(); i++) {
            for (int j = 0; j < s.length(); j++) {
                System.out.print(p[i][j] + " ");
            }
            System.out.println();
        }

        return p[0][n-1];
    }

    public static void main(String[] args){
        System.out.println(new LongestPalinSubseq().findPalind("character"));
    }

}
