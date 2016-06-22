import java.util.Arrays;

/**
 * Created by AminaKeldibek on 5/26/16.
 */
public class CountingSort {

    public CountingSort(){}

    public int[] sort(int [] a, int k){
        int[] c = new int[k+1];
        int [] b = new int[a.length];

        for(int j=0; j<=a.length-1; j++)
            c[a[j]] = c[a[j]] + 1;
        for(int i = 1; i<=k; i++)
            c[i] = c[i] + c[i-1];
        for(int j=a.length-1; j>=0; j--){
            b[c[a[j]]-1]=a[j];
            c[a[j]]=c[a[j]]-1;
        }
        return b;
    }

    public static void main(String[] args){
        int[] sorted = new CountingSort().sort(new int[]{2, 5, 3, 0, 2, 3, 0, 3}, 5);
        int[] sorted2 = new CountingSort().sort(new int[]{4, 1, 3, 2, 16, 9, 10, 14, 8, 7}, 16);

        System.out.println(Arrays.toString(sorted) + '\n' + Arrays.toString(sorted2));
    }
}
