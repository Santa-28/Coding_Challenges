//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while (t-- > 0) {
            String[] arr1Str = sc.nextLine().split(" ");
            int[] arr = Arrays.stream(arr1Str).mapToInt(Integer::parseInt).toArray();
            Solution ob = new Solution();
            int ans = ob.getSecondLargest(arr);
            System.out.println(ans);

            System.out.println("~");
        }
    }
}

// } Driver Code Ends

// User function Template for Java

class Solution {
    public int getSecondLargest(int[] arr) {
        // Code Here
        // Arrays.sort(arr);
        int n=arr.length;
        int max1 = arr[0];
        int max2 = -1;
        for(int i=0;i<n;i++)
        {
            if(max1<arr[i])
            {
                max2=max1; //-1 =12
                max1=arr[i];//
            }
        }
         for(int i=0;i<n;i++)
         {
             if(max2<arr[i] && arr[i]!=max1)
             {
                 max2=arr[i];
             }
         }
        return max2;
       
    }
}