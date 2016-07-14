package Graphs;

/**
 * Created by Amina Keldibek on 7/13/16.
 * Finding all pairs shortest paths for given directed weighted graph.
 * Assumes that graph does not have negative-weight cycles.
 */

public class FloydWarshall {

    private int[][] d; //distance matrix
    private int[][] p; // parent matrix

    public int INF = 10000;
    public int NIL = -1;


    public void printMat(int[][] mat){
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j]==INF)
                    System.out.print("INF ");
                else
                    System.out.print(mat[i][j] + " ");
            }
            System.out.print("\n");
        }
    }


    public void allPairsShortestPath(int[][] graphMat){
        int n = graphMat.length;
        d = graphMat;
        p = new int[n][n];

        // Initialize parent matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (d[i][j] == 0 || d[i][j] == INF)
                    p[i][j] = NIL;
                else
                    p[i][j] = i;
            }
        }

        for (int k = 0; k < n; k++){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++) {
                    if (d[i][j] <= d[i][k] + d[k][j]){
                        d[i][j] = d[i][j];
                        p[i][j] = p[i][j];
                    }
                    else{
                        d[i][j] = d[i][k] + d[k][j];
                        p[i][j] = p[k][j];
                    }
                }
            }
        }

        System.out.println("Distance Matrix");
        printMat(d);

        System.out.println("Parent Matrix");
        printMat(p);
    }

    public void onePairShortestPath(int i, int j){
        if (i==j)
            System.out.print(i + " ");
        else if (p[i][j] == NIL)
            System.out.println("no path from " + i + " to " + j);
        else {
            onePairShortestPath(i, p[i][j]);
            System.out.print(j + " ");
        }
    }

    public static void main(String[] args) {
        int INF = 10000;
        int[][] graph = new int[][]{{0, 3, 8, INF, -4},
                                    {INF, 0, INF, 1, 7},
                                    {INF, 4, 0, INF, INF},
                                    {2, INF, -5, 0, INF},
                                    {INF, INF, INF, 6, 0}};
        FloydWarshall o = new FloydWarshall();
        o.allPairsShortestPath(graph);
        System.out.println("The shortest path from 0 to 1");
        o.onePairShortestPath(0, 1);
    }
}
