package Graphs;

import java.util.*;

/**
 * Created by Amina on 7/2/16.
 */
public class DFS {

    private List<Integer>[] graph;
    private int[] parent;
    private boolean[] visited;
    private  int[] finish;
    private int time;

    public DFS() {}


    /* Initializes parent, visited, finish arrays and time counter*/
    private void init (){
        parent = new int [graph.length];
        for (int i = 0; i<parent.length; i++)
            parent[i] = Integer.MAX_VALUE;
        visited = new boolean[graph.length];
        finish = new int [graph.length];
        time = 0;
    }


    public void DFS(List<Integer>[] graph){
        this.graph = graph;
        init();
        for(int i = 0; i<graph.length; i++){
            if (!visited[i])
                DFSVisit(i);
        }
    }


    /* Visits each adjacent vertex of u which has not been visited yet
    *  and calculates finishing time */
    private void DFSVisit(int u){
        time += 1;
        visited[u] = true;
        (graph[u]).stream().filter(v -> !visited[v]).forEach(v -> {
            parent[v] = u;
            System.out.print(v);
            DFSVisit(v);
        });
        time += 1;
        finish[u] = time;
    }


    /* Computes transpose of a directed graph G = (V, E)
     * represented with adjacency array */
    public List<Integer>[] transpose (List<Integer>[] graph){
        List<Integer>[] t = new List[graph.length];

        for (int i = 0; i< t.length; i++)
            t[i] = new LinkedList<>();
        for(int u = 0; u<graph.length; u++){
            for (Integer v : graph[u])
                t[v].add(u);
        }
        return t;
    }


    /* Computes strongly connected components of a directed graph G = (V, E)
     * represented with adjacency array using two DFS one on G and one on G_T */
    public void StronglyConnected(List<Integer>[] graph){
        this.graph = graph;
        // Call DFS to find finishing times for each vertex u
        DFS(graph);
        // Compute transpose
        this.graph = transpose(graph);

        // Retrieve indices of vertices sorted by finish time in descending order
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for(int i = 0; i < finish.length; i++)
            map.put(finish[i], i);
        Integer[] indices = map.values().toArray(new Integer[map.size()]);

        // Call DFS on G_T
        init();
        System.out.println("\nStrongly connected components:");
        for(int i = indices.length-1; i>=0; i--){
            if (!visited[indices[i]]) {
                System.out.print(indices[i]);
                DFSVisit(indices[i]);
                System.out.println();
            }
        }
    }


    public static void main(String[] args) {
        List[] graph = new List[]{Arrays.asList(1),
                Arrays.asList(2,4,5),
                Arrays.asList(3,6),
                Arrays.asList(2,7),
                Arrays.asList(0,5),
                Arrays.asList(6),
                Arrays.asList(5, 7),
                Arrays.asList(7)};
        DFS o = new DFS();
        o.StronglyConnected(graph);
    }
}
