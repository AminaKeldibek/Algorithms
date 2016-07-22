package Graphs;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

/**
 * Created by AminaKeldibek on 7/21/16.s
 */
public class PushLabel {
    private int[][] residCapacity;
    private int[][] flow;
    private int n; // number of vertices
    private Queue<Node> excessVertices;
    private Node[] vertices;
    private int pushTo;
    private int source;
    private int sink;

    public class Node{
        private int val;
        private int h; // height
        private int e; // excess

        public Node(int val, int h, int e){
            this.val = val;
            this.h = h;
            this.e = e;
        }

        @Override
        public boolean equals(Object other){
            if (other == null) return false;
            if (other == this) return true;
            if (!(other instanceof Node))return false;
            Node otherIndex = (Node)other;
            if (this.val == otherIndex.val)
                return true;
            else
                return false;
        }

        @Override
        public int hashCode() {
            int hash = this.val;
            hash = 89 * hash;
            return hash;
        }

        @Override
        public String toString() {
            return "<" + val + ", " + h + ", " + e + ">";
        }
    }


    class NodeComparator implements Comparator<Node> {
        @Override
        public int compare(Node n1, Node n2) {
            return n2.h - n1.h;
        }
    }


    public void printMat(int[][] mat){
        int n = mat.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.print("\n");
        }
    }


    private void init(int[][] capacity){
        n = capacity.length;
        vertices = new Node[n];
        flow = new int[n][n];
        residCapacity = new int[n][n];
        excessVertices = new PriorityQueue<>(1, new NodeComparator());

        // Initialize flow
        for (int i = 0; i < n; i++){
            flow[i][source] = capacity[source][i];
        }
        // Initialize residual capacity
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                residCapacity[i][j] = capacity[i][j] - flow[j][i];
            }
        }
        // Initialize nodes with height and excesses
        for (int i = 0; i < n; i++) {
            if (i == source)
                vertices[i] = new Node(i, n, 0);
            else {
                int e = findExcess(i);
                vertices[i] = new Node(i, 0, e);
                if (e > 0)
                    excessVertices.add(vertices[i]);
            }
        }
    }


    private int findExcess(int v){
        if (v != source && v!= sink){
            int flowIn = 0, flowOut = 0;
            for (int i = 0; i < n; i++) {
                flowIn += flow[v][i];
                flowOut += flow[i][v];
            }
            return flowIn - flowOut;
        }
        else
            return 0;
    }


    private boolean pushIsPossible(Node u){
        boolean pushIsPossible = false;
        for (int v = 0; v < n; v++){
            if (flow[u.val][v] > 0 || residCapacity[u.val][v] > 0){
                if (vertices[v].h < u.h){
                    pushIsPossible = true;
                    pushTo = v;
                    break;
                }
            }
        }
        return pushIsPossible;
    }

    private void push(int v){
        int delta = 0;
        if (residCapacity[v][pushTo] > flow[v][pushTo]) {
            delta = Math.min(vertices[v].e, residCapacity[v][pushTo]);
            residCapacity[v][pushTo] -= delta;
            flow[pushTo][v] += delta;
        }else{
            delta = Math.min(vertices[v].e, flow[v][pushTo]);
            flow[v][pushTo] -= delta;
            residCapacity[pushTo][v] += delta;
        }

        vertices[v].e = findExcess(v);
        vertices[pushTo].e = findExcess(pushTo);

        if (vertices[v].e > 0) {
            excessVertices.remove(vertices[v]);
            excessVertices.add(vertices[v]);
        }
        if (vertices[pushTo].e > 0){
            excessVertices.remove(vertices[pushTo]);
            excessVertices.add(vertices[pushTo]);
        }
    }


    public int findMaxFlow(int[][] capacity, int source, int sink){
        int maxFlow = 0;
        this.source = source;
        this.sink = sink;
        init(capacity);
        while (!excessVertices.isEmpty()){
            System.out.println("Excess vertices "+ excessVertices);
            Node u = excessVertices.poll();
            if (pushIsPossible(u)) {
                System.out.println("Pushing from " + u + " to " + pushTo);
                push(u.val);
            } else {
                System.out.println("Re-labeling " + u);
                vertices[u.val].h += 1;
                excessVertices.add(u);
            }
        }
        printMat(flow);
        return maxFlow;
    }

    public static void main(String[] args) {
        int[][] capacity = { {0, 1, 0, 100},
                             {0, 0, 100, 100},
                             {0, 0, 0, 0},
                             {0, 1, 1, 0} };
        int[][] capacity2 = { {0, 3, 0, 0},
                              {0, 0, 1, 0},
                              {0, 0, 0, 2},
                              {0, 0, 0, 0} };
        System.out.println("Test 1");
        new PushLabel().findMaxFlow(capacity, 0, 2);
        System.out.println("Test 2");
        new PushLabel().findMaxFlow(capacity2, 0, 3);

    }
}
