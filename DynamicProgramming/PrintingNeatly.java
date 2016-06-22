package DynamicProgramming;

import java.util.Arrays;

/**
 * Created by amina on 6/16/16.
 */
public class PrintingNeatly {

    private int[][] m;
    private int l;

    public PrintingNeatly(){}

    private int calcCost(String[] words){
        int numOfChars = words.length - 1;
        int numOfSpaces;
        for(String word : words){
            numOfChars += word.length();
        }
        numOfSpaces = l - numOfChars;
        if(numOfSpaces >= 0)
            return (int) Math.pow((numOfSpaces), 2);
        else
            return Integer.MAX_VALUE;
    }


    public void findOptimal(String[] words, int l){
        this.l = l;
        int n = words.length;
        int[] cost = new int[n];
        Arrays.fill(cost, -1);
        int[] loc = new int[n];
        m = new int[n][n];
        int temp;

        for (int i = 0; i<n; i++){
            for (int j = i; j<n; j++){
                m[i][j] = calcCost(Arrays.copyOfRange(words,i,j+1));
            }
        }


        /* Print matrix */
        for (int i = 0; i<n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(m[i][j] + " ");
            }
            System.out.println();
        }


        /* Calculate cost and minimum cost arrangement */
        for(int i = n-1; i>=0; i--){
            for(int j = n-1; j>=i; j--){
                int k = j+1;
                if(m[i][j] != Integer.MAX_VALUE){
                    if(k>=n)
                        temp = m[i][j];
                    else
                        temp = m[i][j] + cost[k];
                    if (temp<cost[i] || cost[i]==-1){
                        cost[i] = temp;
                        loc[i] = j+1;
                    }
                }
            }
        }
        System.out.println(Arrays.toString(cost));
        System.out.println(Arrays.toString(loc));

        /* Print text */
        System.out.print(words[0]+" ");
        for (int i=1; i<n; i++){
            if(loc[i]!=loc[i-1])
                System.out.print("\n" + words[i] + " ");
            else
                System.out.print(words[i]);
        }

    }


    public static void main(String[] args) {
        new PrintingNeatly().findOptimal(new String[]{"Tushas", "Roy", "likes", "to", "code"}, 10);
    }
}
