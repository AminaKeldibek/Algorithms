package DynamicProgramming;

import java.util.LinkedList;

/**
 * Created by amina on 6/26/16.
 */
public class PlanningCompanyParty {

    public static class Node{
        private Node leftChild;
        private Node rightSibling;
        private int rank;
        private int name;

        public Node(int name, int rank) {
            this.name = name;
            this.rank = rank;
        }


        public int getRank() {
            return rank;
        }

        public int getName() {
            return name;
        }

        public Node getLeftChild() {
            return leftChild;
        }

        public Node getRightSibling() {
            return rightSibling;
        }

        @Override
        public String toString() {
            return "" + "Guest number " + name + " of rank " + rank;
        }
    }

    public static class RootedTree{
        private Node root;
        private int size;


        public RootedTree(Node root) {
            this.root = root;
            size = 1;
        }

        public int getSize() {
            return size;
        }

        public Node getRoot() {
            return root;
        }

        public void setLeftChild(Node node, Node leftChild) {
            node.leftChild = leftChild;
            size += 1;
        }

        public void setRightSibling(Node node, Node rightSibling) {
            node.rightSibling = rightSibling;
            size += 1;
        }

        public LinkedList<Node> getChildren(Node node){
            LinkedList<Node> children = new LinkedList<>();
            Node child = node.getLeftChild();
            while (child != null){
                children.add(child);
                child = child.getRightSibling();
            }
            return children;
        }

        public LinkedList<Node> getGrandChildren(Node node){
            LinkedList<Node> grandChildren = new LinkedList<>();
            LinkedList<Node> children = getChildren(node);
            for (Node child : children){
                Node grandChild = child.getLeftChild();
                while(grandChild != null){
                    grandChildren.add(grandChild);
                    grandChild = grandChild.getRightSibling();
                }
            }
            return grandChildren;
        }

    }

    private int [] m;
    private int [] mNot;
    private LinkedList<Integer> guests;
    private RootedTree tree;


    public PlanningCompanyParty() {
        guests = new LinkedList<>();
    }

    private void solve(Node x){
        m[x.getName()] = x.getRank();
        mNot[x.getName()] = 0;
        Node y = x.getLeftChild();

        while(y != null){
            solve(y);
            m[x.getName()] += mNot[y.getName()];
            mNot[x.getName()] += Math.max(m[y.getName()], mNot[y.getName()]);
            y = y.getRightSibling();
        }
    }

    private void invite(Node node){
        int nodeName = node.getName();
        if (m[nodeName]>mNot[nodeName]){
            guests.add(nodeName);
            LinkedList<Node> grandChildren = tree.getGrandChildren(node);
            for (Node grandChild : grandChildren)
                invite(grandChild);
        }else{
            LinkedList<Node> children = tree.getChildren(node);
            for (Node child : children)
                invite(child);
        }
    }

    public void findOptGuests(RootedTree tree){
        this.tree = tree;
        int n = tree.getSize();
        this.m = new int[n];
        this.mNot = new int[n];
        solve(tree.getRoot());
        invite(tree.root);
        System.out.println("Following guests are invited: " + guests);
    }


    public static void main(String[] args) {
        // Create rooted tree
        Node root = new Node(0,1);
        Node guest1 = new Node(1,3);
        Node guest2 = new Node(2,3);
        Node guest3 = new Node(3,8);

        RootedTree tree = new RootedTree(root);
        tree.setLeftChild(root, guest1);
        tree.setRightSibling(guest1, guest2);
        tree.setLeftChild(guest1, guest3);

        new PlanningCompanyParty().findOptGuests(tree);
    }
}
