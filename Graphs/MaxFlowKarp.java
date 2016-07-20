package Graphs;

import java.util.*;

/**
 * Created by Amina Keldibek on 7/20/16.
 */
public class MaxFlowKarp {

    private int[][] residCapacity;
    List<Integer> path;
    Map<Integer, Integer> parent;
    private int maxFlow;

    public MaxFlowKarp() {
        path = new LinkedList<>();
        parent = new HashMap<>();
        maxFlow = 0;
    }


    /* Finds and returns max flow for provided flow matrix */
    public int findMaxFlow(int[][] capacity, int source, int sink){
        // Initially residCapacity is the same as provided capacity
        residCapacity = capacity;
        // While BST finds augmenting path from source to sink
        while (BST(source, sink)){
            constructPath(source, sink);
            //System.out.println(path);
            // Find flow
            int flow = Integer.MAX_VALUE;
            for (int i = 0; i < path.size()-1; i++) {
                int c = residCapacity[path.get(i)][path.get(i+1)];
                if (c < flow)
                    flow = c;
            }
            maxFlow += flow;
            // Modify residual capacity
            for (int i = 0; i < path.size()-1; i++)
                modifyCapacity(path.get(i), path.get(i+1), flow);
            path.clear();
        }
        return maxFlow;
    }


    /* Finds path from source to sink and return true if found and false otherwise*/
    private boolean BST(int source, int sink){
        boolean pathIsFound = false;
        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        q.add(source);
        visited.add(source);
        while (!q.isEmpty()){
            int u = q.poll();
            for (int v = 0; v < residCapacity.length; v++){
                if (residCapacity[u][v] > 0 && !visited.contains(v)){
                        q.add(v);
                        visited.add(v);
                        parent.put(v, u);
                        if (v == sink){
                            pathIsFound = true;
                            break;
                        }
                }
            }
        }
        return pathIsFound;
    }


    /* Constructs and returns path list*/
    private void constructPath(int source, int sink){
        if (sink == source) {
            path.add(source);
            return;
        }
        else{
            constructPath(source, parent.get(sink));
            path.add(sink);
            return;
        }
    }

    /* Modifies residual capacity */
    private void modifyCapacity(int u, int v, int flow){
        residCapacity[u][v] = residCapacity[u][v] - flow;
        residCapacity[v][u] = residCapacity[v][u] + flow;
    }


    public static void main(String[] args) {
        int[][] capacity = {{0, 3, 0, 3, 0, 0, 0},
                {0, 0, 4, 0, 0, 0, 0},
                {3, 0, 0, 1, 2, 0, 0},
                {0, 0, 0, 0, 2, 6, 0},
                {0, 1, 0, 0, 0, 0, 1},
                {0, 0, 0, 0, 0, 0, 9},
                {0, 0, 0, 0, 0, 0, 0}};
        System.out.print("Max flow is: ");
        System.out.println(new MaxFlowKarp().findMaxFlow(capacity, 0, 6));
    }
}
