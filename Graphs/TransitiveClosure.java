package Graphs;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

/**
 * Created by Amina Keldibek on 7/14/16.
 * Given a directed graph G this algorithm determines whether
 * G contains a path from i to j for all vertex pairs.
 */
public class TransitiveClosure {

    public static class Edge{
        private int u;
        private int v;

        Edge (int u, int v) {
            this.u = u;
            this.v = v;
        }

        @Override
        public boolean equals(Object other){
            if (other == null) return false;
            if (other == this) return true;
            if (!(other instanceof Edge))return false;
            Edge otherIndex = (Edge)other;
            if (this.u == otherIndex.u && this.v == otherIndex.v)
                return true;
            else
                return false;
        }

        @Override
        public int hashCode() {
            int hash = 17;
            hash = 31 * hash + u;
            hash = 31 * hash + v;
            return hash;
        }
    }


    public static class Graph {
        List<Edge> edges;
        Set<Integer> vertices;

        public Graph(){
            edges = new LinkedList<>();
            vertices = new HashSet<>();
        }

        public void addEdge(int u, int v){
            edges.add(new Edge(u, v));
            vertices.add(u);
            vertices.add(v);
        }

        public List<Edge> getEdges() {
            return edges;
        }

        public int getSize() {
            return vertices.size();
        }
    }


    public void printMat(boolean [][] mat){
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.print("\n");
        }
    }


    public void findTransClosure(Graph g){
        int n = g.getSize();
        boolean[][] t = new boolean[n][n];
        List<Edge> edges = g.getEdges();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i==j || edges.contains(new Edge(i, j)))
                    t[i][j] = true;
                else
                    t[i][j] = false;
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    t[i][j] = t[i][j] || (t[i][k] && t[k][j]);
                }
            }
        }
        printMat(t);
    }


    public static void main(String[] args) {
        Graph g = new Graph();
        g.addEdge(1, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 1);
        g.addEdge(3, 0);
        g.addEdge(3, 2);

        new TransitiveClosure().findTransClosure(g);
    }
}
