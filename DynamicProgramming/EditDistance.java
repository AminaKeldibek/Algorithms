package DynamicProgramming;

/**
 * Created by amina on 6/24/16.
 */
public class EditDistance {

    private int[][] cost;

    private class minIndex {
        private int val, x, y;

        public minIndex(int val, int x, int y) {
            this.val = val;
            this.x = x;
            this.y = y;
        }

        public int getVal() {
            return val;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    private minIndex findMin(minIndex val1, minIndex val2, minIndex val3){
        minIndex min;
        if(val1.getVal() <= val2.getVal())
            min = val1;
        else
            min = val2;
        if(val3.getVal()<min.getVal())
            min = val3;
        return min;
    }

    private void calcEditDist(String w1, String w2){
        int n1 = w1.length()+1;
        int n2 = w2.length()+1;
        cost = new int[n1][n2];

        // initialize cost matrix
        cost[0][0] = 0;
        for(int i=1; i<n1; i++)
            cost[i][0] = i;
        for(int j=1; j<n2; j++)
            cost[0][j] = j;

        // calculate minimum cost
        for(int i=1; i<n1; i++){
            for(int j=1; j<n2; j++){
                if (w1.charAt(i-1) == w2.charAt(j-1))
                    cost[i][j] = cost[i - 1][j - 1];
                else{
                    cost[i][j] = findMin(new minIndex(cost[i-1][j], i-1, j),
                                             new minIndex(cost[i][j-1], i, j-1),
                                             new minIndex(cost[i-1][j-1], i-1, j-1)).getVal() + 1;
                }
            }
        }
    }

    private void printEditOps(String w1, String w2){
        int i = w1.length();
        int j= w2.length();
        while(i!=0 || j!=0){
            if (w1.charAt(i-1) == w2.charAt(j-1)){
                i --;
                j --;
            }else{
                minIndex min = findMin(new minIndex(cost[i-1][j], i-1, j),
                        new minIndex(cost[i][j-1], i, j-1),
                        new minIndex(cost[i-1][j-1], i-1, j-1));
                int prevI = min.getX();
                int prevJ = min.getY();
                if(i == prevI+1 && j == prevJ+1)
                    System.out.println(w2.charAt(j-1) + " is editted to " + w1.charAt(i-1));
                else if(i == prevI && j == prevJ+1)
                    System.out.println(w2.charAt(j-1) + " is deleted ");
                else if(i == prevI+1 && j == prevJ)
                    System.out.println(w1.charAt(i-1) + " is added ");
                i = prevI;
                j = prevJ;
            }
        }

    }

    public void findEditDist(String w1, String w2){
        calcEditDist(w1, w2);
        printEditOps(w1, w2);
    }

    public static void main(String[] args) {
        new EditDistance().findEditDist("azced", "abcdef");

    }
}
