package DynamicProgramming;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by Amina Keldibek on 7/23/16.
 */
public class Knapsack01 {
    private List<Item> knapsack;
    private int[][] t;
    private List<Item> items;


    public Knapsack01() {
        this.knapsack = new LinkedList<>();
    }


    public static class Item {
        int value;
        int weight;

        public Item(int value, int weight) {
            this.value = value;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "<" + value + ", " + weight + ">";
        }
    }


    public void printMat(int[][] mat, int m, int n){
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(mat[i][j] + " ");
            }
            System.out.print("\n");
        }
    }


    private void addToKnapsack(int i, int j){
        Item cur = items.get(i-1);
        if (i == 0 || j == 0)
            return;
        if (cur.value + t[i-1][j-cur.weight] > t[i-1][j]){
            knapsack.add(cur);
            addToKnapsack(i-1, j-cur.weight);
        }else
            addToKnapsack(i-1, j);
    }


    public List<Item> fillKnapsack(List<Item> items, int weight){
        this.items = items;
        int n = items.size();
        t = new int[n+1][weight+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= weight; j++) {
                int w = items.get(i-1).weight;
                if (w <= j)
                    t[i][j] = Math.max(items.get(i-1).value + t[i-1][j-w], t[i-1][j]);
                else
                    t[i][j] = t[i-1][j];
            }
        }
        printMat(t, n+1, weight+1);
        addToKnapsack(n, weight);
        return knapsack;
    }


    public static void main(String[] args) {
        List<Item> items = new LinkedList<>();
        items.add(new Item(1, 1));
        items.add(new Item(4, 3));
        items.add(new Item(5, 4));
        items.add(new Item(7, 5));
        System.out.println(new Knapsack01().fillKnapsack(items, 7));
    }
}
