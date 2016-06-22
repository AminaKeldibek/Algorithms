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
public class MergeSort {
        
    public MergeSort(){}
    
    private void merge(float[] array, int p, int q, int r){

        float[] lowHalf = Arrays.copyOfRange(array, p, q+1);
        float[] highHalf = Arrays.copyOfRange(array, q+1, r+1);
        int a=p, l=0, h=0;
        while(a!=r+1){
            if (lowHalf[l] < highHalf[h]){
                array[a] = lowHalf[l];
                a++;
                l++;
                if(l==lowHalf.length){
                    System.arraycopy(highHalf,h,array,a,highHalf.length-1);
                    break;
                }
            }else if (lowHalf[l] > highHalf[h]){
                array[a] = highHalf[h];
                a++;
                h++;
                if(h==highHalf.length){
                    System.arraycopy(lowHalf,l,array,a,lowHalf.length-l);
                    break;
                }
            }else if (lowHalf[l]== highHalf[h]){
                array[a] = lowHalf[l];
                array[a+1] = highHalf[h];
                a = a+2;
                l++;
                h++;
            }
        }
    }

    private void mergeSort(float[] array, int p, int r){
        int q = (int) Math.floor((p+r)/2);
        if (Arrays.copyOfRange(array, p, q+1).length>2){
            mergeSort(array,p,q);
            mergeSort(array, q+1, r);
        }
        merge(array, p, q, r);
    }

    public float[] sort(float[] array){
        float[] inputArray = array;
        mergeSort(inputArray, 0, array.length-1);
        return inputArray;
    }

    public static void main(String[] args){
        float[] sorted = new MergeSort().sort(new float[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7});
        System.out.println(Arrays.toString(sorted));
    }
}
