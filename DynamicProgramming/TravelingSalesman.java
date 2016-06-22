package DynamicProgramming;

import java.util.*;
/**
 * Created by amina on 6/21/16.
 */
public class TravelingSalesman {
    private List<Set<Integer>> combs;
    private int[][] costMat;
    private Map<Index, OptState> minRouteMap;
    private int n;
    private Set<Integer> fullSet;


    TravelingSalesman(){
        combs = new LinkedList<>();
    }

    /* Class for storing state and previous combination */
    private class Index{
        private int state;
        private Set<Integer> comb;

        Index(int state, Set<Integer> comb){
            this.state = state;
            this.comb = comb;
        }

        @Override
        public boolean equals(Object other){
            if (other == null) return false;
            if (other == this) return true;
            if (!(other instanceof Index))return false;
            Index otherIndex = (Index)other;
            if (this.state == otherIndex.state && this.comb.equals(otherIndex.comb))
                return true;
            else
                return false;
        }

        @Override
        public int hashCode() {
            int hash = this.state;
            hash = 89 * hash + (this.comb != null ? this.comb.hashCode() : 0);
            return hash;
        }

        @Override
        public String toString(){
            return "" + this.state + "{" + this.comb + "}";
        }
    }


    /* Class for storing previous state and cost of going from prev to current state*/
    private class OptState{
        private int cost;
        private int state;

        public int getState() {
            return state;
        }

        public int getCost() {
            return cost;
        }

        public OptState(int cost, int state) {
            this.cost = cost;
            this.state = state;
        }

        @Override
        public String toString(){
            return "previous state: " + this.state + ", cost: " + this.cost;
        }
    }


    /* Generate combinations helper function */
    private void getCombsHelper(String pref, String s){
        Set<Integer> set = new HashSet<>();
        if (s.length() > 0){
            String comb = pref+s.charAt(0);
            for(int i=0; i<comb.length(); i++)
                set.add(Character.getNumericValue(comb.charAt(i)));
            combs.add(set);
            getCombsHelper(pref+s.charAt(0), s.substring(1));
            getCombsHelper(pref, s.substring(1));
        }
    }


    /* Class for sorting combinations set */
    class compareSets implements Comparator<Set<Integer>> {
        @Override
        public int compare(Set<Integer> o1, Set<Integer> o2) {
            return o1.size() - o2.size();
        }
    }


    /* Generate combinations */
    private void getCombs (){
        String states = "";
        for (int i=1; i<n; i++)
            states = states + i;
        getCombsHelper("", states);
        // Add empty set
        combs.add(new HashSet<>());
        // Remove full set
        fullSet = new HashSet<>();
        for(int i=1; i<n; i++)
            fullSet.add(i);
        combs.remove(fullSet);
        // Sort combinations according to size
        Collections.sort(combs, new compareSets());
    }


    /* Calculate cost for going from prevState to state */
    private int getCost(int prevState, int state, Set<Integer> comb){
        int prevCost = minRouteMap.get(new Index(prevState, comb)).getCost();
        return prevCost + costMat[prevState][state];
    }


    /* Pretty print for map
    * http://stackoverflow.com/questions/1066589/iterate-through-a-hashmap */
    public static void printMap(Map mp) {
        Iterator it = mp.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry pair = (Map.Entry)it.next();
            System.out.println(pair.getKey() + " = " + pair.getValue());
            //it.remove(); // avoids a ConcurrentModificationException
        }
    }


    /* Count optimal previous state */
    private void findOptState(){
        minRouteMap = new HashMap<>();
        int minCost, minPrevState = 0;
        n = costMat[0].length;
        getCombs();

        for(Set<Integer> comb : combs) {
            for(int state=1; state<n; state++){
                minCost = Integer.MAX_VALUE;
                if (comb.contains(state))
                    continue;
                if(comb.isEmpty()){
                    minCost = costMat[0][state];
                    minPrevState = 0;
                }
                else{
                    for(int prevState : comb){
                        // Copy current combination to avoid modifications
                        Set<Integer> tempComb = new HashSet<>(comb);
                        tempComb.remove(prevState);
                        int cost = getCost(prevState, state, tempComb);
                        if(cost<minCost){
                            minCost = cost;
                            minPrevState = prevState;
                        }
                    }
                }
                minRouteMap.put(new Index(state, comb), new OptState(minCost, minPrevState));
            }
        }

        // Going from full set to zero state
        minCost = Integer.MAX_VALUE;
        for(int prevState : fullSet){
            Set<Integer> tempComb = new HashSet<>(fullSet);
            tempComb.remove(prevState);
            int cost = getCost(prevState, 0, tempComb);
            if(cost<minCost){
                minCost = cost;
                minPrevState = prevState;
            }
        }
        minRouteMap.put(new Index(0, fullSet), new OptState(minCost, minPrevState));
        //printMap(minRouteMap);
    }


    /* Print optimal route */
    private void printOptState(){
        System.out.print(0 + " <- ");
        int cur = minRouteMap.get(new Index(0, fullSet)).getState();
        while(fullSet.size() != 0){
            System.out.print(cur + " <- ");
            fullSet.remove(cur);
            cur = minRouteMap.get(new Index(cur, fullSet)).getState();
        }
        System.out.print(0);
    }


    /* Find and output optimal route */
    public void findOptRoute(int[][] cost){
        this.costMat = cost;
        findOptState();
        printOptState();
    }


    public static void main(String[] args) {
        int[][] cost = new int[][]{ {0, 1, 15, 6},
                                    {2, 0, 7, 3},
                                    {9, 6, 0, 12},
                                    {10, 4, 8, 0} };
        new TravelingSalesman().findOptRoute(cost);
    }
}