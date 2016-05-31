import java.util.Arrays;


/**
 * Created by Amina Keldibek on 5/26/16.
 */
public class InsertionSort {
    
    public InsertionSort(){}
    
    private double[] insert(double[] inputArray, int rightIdx, double val){
        for (int idx = rightIdx; idx>=0; idx--){
            if (inputArray[idx] >= val){
                inputArray[idx+1] = inputArray[idx];
                if (idx==0){
                    inputArray[0] = val;
                }
            }else{
                inputArray[idx+1] = val;
                break;
            }
        }
        System.out.println(Arrays.toString(inputArray));
        return inputArray;
    }


    public double[] sort(double[] inputArray){
        for (int i = 0; i< inputArray.length-1; i++) {
            inputArray = insert(inputArray, i, inputArray[i+1]);
        }
        return inputArray;
    }

    public static void main(String[] args){
        double[] sorted = new InsertionSort().sort(new double[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7});
        System.out.println(Arrays.toString(sorted));
    }
    
}
