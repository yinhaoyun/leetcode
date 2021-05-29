package Solution;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maximumUniqueSubarray(new int[] {4,2,4,5,6}));
        System.out.println(s.maximumUniqueSubarray(new int[] {5,2,1,2,5,2,1,2,5}));
    }

    public int maximumUniqueSubarray(int[] nums) {
        int currentSum = 0, maxSum = 0;
        Set<Integer> set = new HashSet<>();
        int start = 0;
        for (int n: nums) {
            if (!set.contains(n)) {
                set.add(n);
                currentSum += n;
                maxSum = Math.max(maxSum, currentSum);
                continue;
            }
            
            while (nums[start] != n) {
                currentSum -= nums[start];
                set.remove(nums[start]);
                start++;
            }
            start++;
        }
        return maxSum;
    }
}
