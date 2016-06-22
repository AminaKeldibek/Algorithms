import java.util.Arrays;

/**
 * Created by Amina Keldibek on 5/26/16.
 */
public class HeapSort {

    private double[] a;
    private int heapsize;

    public HeapSort(){}

    private int getLeft(int i){
        return 2*i+1;
    }


    private int getRight(int i){
        return 2*i+2;
    }


    private void exchange(int i1, int i2){
        double temp = a[i1];
        a[i1] = a[i2];
        a[i2] = temp;
    }


    private void maxHeapify(int i){
        int l = getLeft(i);
        int r = getRight(i);
        int largest;
        if (l<=heapsize-1 && a[l]>a[i])
            largest = l;
        else
            largest = i;
        if (r<=heapsize-1 && a[r]>a[largest])
            largest = r;
        if (largest != i){
            exchange(i,largest);
            maxHeapify(largest);
        }
    }


    private void buildMaxHeap(){
        heapsize = a.length;
        for (int i=a.length/2-1; i>=0; i--){
            maxHeapify(i);
        }
    }


    public double[] sort(double [] inputArray){
        this.a = inputArray;
        buildMaxHeap();
        for (int i=a.length-1; i>=1; i--){
            exchange(0, i);
            heapsize --;
            maxHeapify(0);
        }
        return a;
    }

    public static void main(String[] args){
        double[] sorted = new HeapSort().sort(new double[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7});
        System.out.println(Arrays.toString(sorted));
    }
}
