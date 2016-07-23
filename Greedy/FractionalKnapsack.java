package Greedy;

import java.util.*;

/**
 * Created by Amina Keldibek on 7/23/16.
 */
public class FractionalKnapsack {
    private List<Item> knapsack;

    public FractionalKnapsack(){
        this.knapsack = new LinkedList<>();
    }

    public static class Item{
        int name;
        double value;
        double weight;

        public Item (int name, double value, double weight){
            this.name = name;
            this.value = value;
            this.weight = weight;
        }

        @Override
        public String toString() {
            return "item " + name + " with val and weight <" + value + ", " + weight + ">";
        }
    }

    class ItemComparator implements Comparator<Item> {
        @Override
        public int compare(Item i1, Item i2) {
            double dif = i2.value/i2.weight - i1.value/i1.weight;
            if (dif > 0)
                return 1;
            else if (dif < 0)
                return -1;
            else
                return 0;
        }
    }

    private List<Item> fillKnapsack(List<Item> items, int weight){
        Collections.sort(items, new ItemComparator());
        int freeWeight = weight;
        for (Item i : items){
            if (i.weight <= freeWeight){
                knapsack.add(i);
                freeWeight -= i.weight;
            }
            else {
                knapsack.add(new Item(i.name, (freeWeight / i.weight) * i.value, freeWeight));
                break;
            }
        }
        return knapsack;
    }

    public static void main(String[] args) {
        List<Item> items = new LinkedList<>();
        items.add(new Item(1, 5, 5));
        items.add(new Item(2, 15, 5));
        items.add(new Item(3, 5, 15));
        items.add(new Item(4, 10, 20));
        System.out.println(new FractionalKnapsack().fillKnapsack(items, 23));
    }
}
