/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Arrays;

/**
 *
 * @author Amina Keldibek
 */
public class SelectionSort {
    
   
   private int minIdx;
   
   public SelectionSort(){
       minIdx = 0;
   }
   
   private void idxOfMin(float[] inputArray){
       for (int idx=0; idx<inputArray.length; idx++){
           if (inputArray[idx]<inputArray[minIdx]) {
               minIdx = idx;
           }
       }
   } 
   
   private float[] swap (float[] inputArray, int idx1){
       float valReplaced = inputArray[idx1];
       
       inputArray[idx1] = inputArray[minIdx+idx1];
       inputArray[minIdx+idx1] = valReplaced;
       minIdx = 0;
       return inputArray;
   }
           
   public float[] sort (float[] inputArray){ 
       for (int idx=0; idx<inputArray.length; idx++){
           idxOfMin(Arrays.copyOfRange(inputArray, idx, inputArray.length));
           inputArray = swap(inputArray,idx);
       }
       return inputArray;
   }

    public static void main(String[] args){
        float[] sorted = new SelectionSort().sort(new float[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7});
        System.out.println(Arrays.toString(sorted));
    }


}
