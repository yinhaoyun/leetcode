package com.haoyun.leetcode;

public class MaximumSwap {
    public int maximumSwap(int num) {
        String strNum = Integer.toString(num);
        int[] nums = new int[strNum.length()];
        int maxNum = 0;
        int maxIndex = 0;
        for (int i = 0; i < nums.length; i ++) {
            nums[i] = Integer.parseInt(String.valueOf(strNum.charAt(i)));
            if (nums[i] >= maxNum) {
                maxNum = nums[i];
                maxIndex = i;
            }
        }

        for (int i = 0; i < maxIndex; i ++) {
            if (nums[i] != maxNum) {
                nums[maxIndex] = nums[i];
                nums[i] = maxNum;
                break;
            }
        }
        return arrayToNum(nums);
    }

    private int arrayToNum(int[] nums) {
        int num = 0;
        for (int i : nums) {
            num = num * 10 + i;
        }
        return num;
    }
}
