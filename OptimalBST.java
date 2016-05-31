/**
 * Created by AminaKeldibek on 5/6/16.
 */
public class OptimalBST {

    private double[] p, q;
    private int size;

    private double[][] e, w;
    private int[][] root;

    public OptimalBST(double[] p, double[] q, int size){
        this.p = p;
        this.q = q;
        this.size = size;

        e = new double[size+2][size+1];
        w = new double[size+2][size+1];
        root = new int[size+1][size+1];
    }

    public void findRoot(){
        int j;

        for (int i=1; i<=size+1; i++){
            e[i][i-1] = q[i-1];
            w[i][i-1] = q[i-1];
        }
        for (int l=1; l<=size; l++){
            for(int i=1;i<=(size-l+1);i++){
                j = i+l-1;
                e[i][j]= Float.POSITIVE_INFINITY;
                w[i][j]=w[i][j-1]+p[j]+q[j];
                for (int r=i;r<=j;r++){
                    double temp = e[i][r-1]+e[r+1][j]+w[i][j];
                    if (temp<e[i][j]){
                        e[i][j] = temp;
                        root[i][j]=r;
                    }
                }
            }
        }
    }

    public void getRoots(){
        System.out.println("Root matrix");
        for (int i=0;i<=size;i++){
            for(int j = 0;j<=size;j++){
                System.out.print(root[i][j]+"|");
            }
            System.out.print("\n");
        }
    }

    public void getExpect(){
        System.out.println("Expectation matrix");
        for (int i=0;i<=size+1;i++){
            for(int j = 0;j<=size;j++){
                System.out.print(String.format("%.2f", e[i][j])+"|");
            }
            System.out.print("\n");
        }
    }

    public static void main(String[] args){
        double[] p = {0, 0.15, 0.1,0.05, 0.1, 0.2};
        double[] q = {0.05, 0.1, 0.05,0.05, 0.05, 0.1};
        OptimalBST optBST = new OptimalBST(p,q,5);
        optBST.findRoot();

        optBST.getRoots();
        optBST.getExpect();

    }
}
