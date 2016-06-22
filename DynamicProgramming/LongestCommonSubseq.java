package DynamicProgramming;

/**
 * Created by amina on 6/15/16.
 * Find the longest subsequence between s1 and s2.
 * For example, given "ACBEA" and "ADCA" output "ACA"
 */
public class LongestCommonSubseq {

    private int[][] m, p;

    public LongestCommonSubseq(){}

    private void displayMatrix(int[][] m, String s1, String s2){
        for (int i = 0; i<s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                System.out.print(m[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private void displayOut(String s1, String s2){
        StringBuffer out = new StringBuffer();
        int i = s1.length()-1;
        int j = s2.length()-1;
        System.out.println(i);
        System.out.println(j);

        while(i>=0 && j>=0) {
            if (p[i][j] == 0) {
                out.append(s1.charAt(i));
                i--;
                j--;
            } else if (p[i][j] == 1)
                j--;
            else if (p[i][j] == 2)
                i--;
        }
        System.out.println(out.reverse());
    }

    private void compare(String s1, String s2){
        int n1 = s1.length();
        int n2 = s2.length();
        m = new int[n1][n2];
        p = new int[n1][n2];

        for (int i = 0; i<n1; i++){
            for(int j = 0; j<n2; j++){
                // If match
                if(s1.charAt(i) == s2.charAt(j)){
                    if(i==0 || j==0) // if first row or column
                        m[i][j] = 1;
                    else
                        m[i][j] = 1 + m[i-1][j-1];
                    p[i][j] = 0; // s1 or s2
                }
                // If do not match
                else{
                    if(i==0 && j>0){// zero row
                        m[i][j] = m[i][j-1];
                        p[i][j] = 1;
                    }else if(j==0 && i>0){ // zero column
                        m[i][j] = m[i-1][j];
                        p[i][j] = 2;
                    }else if(i>0 && j>0){
                        if (m[i-1][j] >= m[i][j-1]){
                            m[i][j] = m[i-1][j];
                            p[i][j] = 1;
                        }else if (m[i-1][j] < m[i][j-1])
                            m[i][j] = m[i][j-1];
                            p[i][j] = 2;
                    }
                }
            }
        }
    }

    public void LCS(String s1, String s2){
        compare(s1, s2);
        displayMatrix(m, s1, s2);
        displayMatrix(p, s1, s2);
        displayOut(s1, s2);
    }

    public static void main (String[] args){
        LongestCommonSubseq o = new LongestCommonSubseq();
        o.LCS("ACBEA", "ADCA");
    }
}
