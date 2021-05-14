class Solution {
    public int[] decompressRLElist(int[] nums) {
        int N = 0;
        for (int i = 0; i < nums.length; i += 2) {
            N += nums[i];
        }
        // System.out.println(N);
        int count = 0;
        int[] output = new int[N];
        for (int i = 0; i < nums.length; i += 2) {
            int val = nums[i + 1];
            int freq = nums[i];
            while (freq != 0) {
                output[count++] = val;
                freq -= 1;
            }
        }
        return output;
    }
}