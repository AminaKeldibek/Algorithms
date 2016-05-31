/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Arrays;

/**
 *
 * @author amina
 */
public class QuickSort {
    
    public QuickSort(){}
    
    private void swap (float[] array, int idx1, int idx2){
        float el1 = array[idx1];
        array[idx1] = array[idx2];
        array[idx2] = el1;        
    }
    
    private int partition(float[] array, int p, int r){
        int q = p; int j = p;

        while(j!=r){
            if (array[j]>array[r]){
                j++;
            }else if (array[j]<=array[r]){
                swap(array, j, q);
                j++;
                q++;                    
            }
        }
        swap(array, r,q);

        return q; 
    }
    
    private void quickSort(float[] array, int p, int r){
        if(Arrays.copyOfRange(array,p,r+1).length >= 2){
            int q = partition(array, p, r);
            quickSort(array, p, q-1);
            quickSort(array, q+1, r);            
        }
    }   
    
    public float[] sort(float[] array){
        float[] inputArray = array;
        quickSort(inputArray, 0, array.length-1);
        return inputArray;
    }

    public static void main(String[] args){
        float[] sorted = new QuickSort().sort(new float[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7});
        System.out.println(Arrays.toString(sorted));
    }

}
