package Graphs;

import java.util.*;

/**
 * Created by Amina Keldibek on 7/19/16.
 */
public class Dijkstra {
    private int[] dist;
    private int[] pred;
    private boolean[] visited;


    public static class Edge{
        int u;
        int v;
        int w;

        public Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

        @Override
        public String toString() {
            return "<" + u + ", " + v + "; " + w + ">";
        }
    }


    public static class Graph{
        List<Edge> edges = new LinkedList<>();
        Set<Integer> vertices = new HashSet<>();
        public Graph() {}

        public void addEdge(Edge e){
            edges.add(e);
            vertices.add(e.u);
            vertices.add(e.v);
        }

        public List<Edge> getEdges() {
            return edges;
        }

        public int order(){
            return vertices.size();
        }
    }


    public class Vertex{
        int val;
        int dist;

        public Vertex(int val, int dist){
            this.val = val;
            this.dist = dist;
        }

        @Override
        public boolean equals(Object other){
            if (other == null) return false;
            if (other == this) return true;
            if (!(other instanceof Vertex)) return false;
            Vertex otherVertex = (Vertex)other;
            if (this.val == otherVertex.val)
                return true;
            else
                return false;
        }

        @Override
        public int hashCode() {
            int hash = this.val;
            return 89 * hash;
        }

        @Override
        public String toString() {
            return "<" + val + ", " + dist + ">";
        }
    }


    private class VertexComparator implements Comparator<Vertex> {
        @Override
        public int compare(Vertex v1, Vertex v2) {
            return v1.dist - v2.dist;
        }
    }


    public void printPath(int s, int v){
        if (v == s)
            System.out.print(s + " ");
        else if (pred[v] == Integer.MAX_VALUE)
            System.out.println("No path from " + s + " to " + v + " exists");
        else {
            printPath(s, pred[v]);
            System.out.print(v + " ");
        }
    }


    public void minPath(Graph g, int s){
        int INF = 10000;
        dist = new int[g.order()];
        pred = new int[g.order()];
        visited = new boolean[g.order()];

        Arrays.fill(dist, INF);
        Arrays.fill(pred, -1);

        dist[s] = 0;
        PriorityQueue<Vertex> q = new PriorityQueue<>(2, new VertexComparator());
        q.add(new Vertex(s, 0));

        while(!q.isEmpty()){
            int u = q.poll().val;
            visited[u] = true;
            for (Edge e : g.getEdges()) {
                if (e.u == u){
                    int v = e.v;
                    if (!visited[v]){
                        int alt = dist[u] + e.w;
                        if (alt < dist[v])
                            dist[v] = alt;
                        pred[v] = u;
                        // Update queue
                        q.remove(new Vertex(v, dist[v]));
                        q.add(new Vertex(v, alt));
                    }
                }
            }
        }

        System.out.println(Arrays.toString(dist));
        System.out.println(Arrays.toString(pred));
        printPath(s, 1);
    }


    public static void main(String[] args) {
        Graph g = new Graph();
        g.addEdge(new Edge(0, 1, 10));
        g.addEdge(new Edge(0, 4, 5));
        g.addEdge(new Edge(1, 2, 1));
        g.addEdge(new Edge(1, 4, 2));
        g.addEdge(new Edge(2, 3, 4));
        g.addEdge(new Edge(3, 2, 6));
        g.addEdge(new Edge(3, 0, 7));
        g.addEdge(new Edge(4, 1, 3));
        g.addEdge(new Edge(4, 3, 2));
        g.addEdge(new Edge(4, 2, 9));
        new Dijkstra().minPath(g, 0);
    }
}
