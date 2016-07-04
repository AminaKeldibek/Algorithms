package Graphs;

import org.apache.commons.lang3.builder.HashCodeBuilder;

import java.util.*;

/**
 * Created by Amina Keldibek on 7/4/16.
 * Kruskal algorithm for solving Minimum Spanning Trees problem.
 * Assume that graph vertices take integer values.
 */
public class MSTKruskal {

    public MSTKruskal() {}

    public static class Edge{
        private int u;
        private int v;
        private int weight;

        Edge (int u, int v, int weight) {
            this.u = u;
            this.v = v;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "<" + u + ", " + v + ">, w: " + weight + "\n";
        }
    }


    public static class Graph {
        List<Edge> edges;
        Set<Integer> vertices;

        public Graph(){
            edges = new LinkedList<>();
            vertices = new HashSet<>();
        }

        public void addEdge(int u, int v, int weight){
            edges.add(new Edge(u, v, weight));
            vertices.add(u);
            vertices.add(v);
        }

        public List<Edge> getEdges() {
            return edges;
        }

        public Set<Integer> getVertices() {
            return vertices;
        }

    }


    class EdgeComparator implements Comparator<Edge> {
        @Override
        public int compare(Edge e1, Edge e2) {
            return e1.weight - e2.weight;
        }
    }


    public List<Edge> getMST (Graph graph){
        List<Edge> A = new LinkedList<>();
        DisjointSetForest disjointSet  = new DisjointSetForest();

        // Make set for each vertex in the graph
        for (int v: graph.getVertices())
            disjointSet.makeSet(v);

        // Sort the edges into non decreasing order by weight
        Collections.sort(graph.getEdges(), new EdgeComparator ());

        // For each edge if u and v are in different tree add <u, v> to A
        Map<Integer, DisjointSetForest.Node> nodes = disjointSet.getNodes();
        for(Edge e : graph.getEdges()){
            if (disjointSet.findSet(nodes.get(e.u)) != disjointSet.findSet(nodes.get(e.v))){
                A.add(e);
                disjointSet.union(nodes.get(e.u), nodes.get(e.v));
            }
        }
        return A;
    }


    public static void main(String[] args) {
        Graph graph = new Graph();
        graph.addEdge(0, 1, 4);
        graph.addEdge(0, 7, 8);
        graph.addEdge(1, 2, 8);
        graph.addEdge(2, 3, 7);
        graph.addEdge(3, 4, 9);
        graph.addEdge(4, 5, 10);
        graph.addEdge(5, 6, 2);
        graph.addEdge(6, 7, 1);
        graph.addEdge(7, 8, 7);
        graph.addEdge(8, 2, 2);
        graph.addEdge(2, 5, 4);
        graph.addEdge(1, 7, 11);
        graph.addEdge(7, 2, 7);
        graph.addEdge(3, 5, 14);
        System.out.println("Minimum spanning tree consists of edges: "
                            + new MSTKruskal().getMST(graph));
    }
}
