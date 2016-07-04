package Graphs;


import java.util.HashMap;
import java.util.Map;

/**
 * Created by Amina Keldibek on 7/4/16.
 * Disjoint Set Forest implementation.
 */
public class DisjointSetForest {

    private Map<Integer, Node> nodes;

    public DisjointSetForest(){
        nodes = new HashMap<>();
    }

    class Node{
        int val;
        Node p;
        int rank;
    }

    public Map<Integer, Node> getNodes() {
        return nodes;
    }

    public void makeSet(int val){
        Node node = new Node();
        node.val = val;
        node.rank = 0;
        node.p = node;
        nodes.put(val, node);
    }

    public void union (Node x, Node y){
        link(findSet(x), findSet(y));
    }

    private void link(Node x, Node y){
        if (x.rank > y.rank)
            y.p = x;
        else{
            x.p = y;
            if (x.rank == y.rank)
                y.rank = y.rank + 1;
        }
    }

    public Node findSet(Node x){
        if (x != x.p)
            x.p = findSet(x.p);
        return x.p;
    }

    public static void main(String[] args) {
        DisjointSetForest o = new DisjointSetForest();
        // Create union of 4 and 5
        o.makeSet(5);
        o.makeSet(4);
        o.union(o.getNodes().get(4), o.getNodes().get(5));

        // For both nodes the parent should be 5
        System.out.println(o.findSet(o.getNodes().get(4)).val);
        System.out.println(o.findSet(o.getNodes().get(5)).val);

        // Create union of 3 and 6 and then union 5 and 6
        o.makeSet(3);
        o.makeSet(6);
        o.union(o.getNodes().get(3), o.getNodes().get(6));
        o.union(o.getNodes().get(5), o.getNodes().get(6));

        // We should obtain one union with parent 6
        System.out.println(o.findSet(o.getNodes().get(4)).val);;
    }
}
