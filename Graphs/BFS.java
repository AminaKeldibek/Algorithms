package Graphs;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by amina on 7/1/2016.
 */
public class BFS {

    private List<Integer>[] graph;
    private int[] dist;
    private int[] parent;
    private boolean[] visited;

    public BFS(){}

    public void BFS(List<Integer>[] graph, int s){
        this.graph = graph;
        dist = new int[graph.length];
        parent = new int[graph.length];
        visited = new boolean[graph.length];

        dist[s] = 0;
        parent[s] = Integer.MAX_VALUE;
        visited[s] = true;

        Queue<Integer> q = new LinkedList<>();
        q.add(s);

        while(!q.isEmpty()){
            int u = q.poll();
            for (Integer v : graph[u]){
                if (!visited[v]){
                    visited[v] = true;
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.add(v);
                }
            }
        }
        System.out.println("dists" + Arrays.toString(dist));
        System.out.println("parent" + Arrays.toString(parent));
    }

    public void printPath(int s, int v){
        if (v == s)
            System.out.println(s);
        else if (parent[v] == Integer.MAX_VALUE)
            System.out.println("No path from " + s + " to " + v + " exists");
        else {
            printPath(s, parent[v]);
            System.out.println(v);
        }

    }

    public static void main(String[] args) {
        List[] graph = new List[]{Arrays.asList(1, 4),
                Arrays.asList(0, 5),
                Arrays.asList(5, 6, 3),
                Arrays.asList(2, 6, 7),
                Arrays.asList(0),
                Arrays.asList(1, 2, 6),
                Arrays.asList(5, 2, 3, 7),
                Arrays.asList(3, 6)};

        BFS o = new BFS();
        o.BFS(graph, 1);
        o.printPath(1,2);

    }

}