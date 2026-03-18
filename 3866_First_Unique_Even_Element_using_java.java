import java.util.HashMap;
class Solution {
    public int firstUniqueEven(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i< nums.length; i++){
            if (freq.containsKey(nums[i])){
                freq.put(nums[i], freq.get(nums[i]) + 1);
            }
            else{
                freq.put(nums[i], 1);
            }
        }

        for (int j = 0; j < nums.length; j++){
            if (nums[j] % 2 == 0){
                if (freq.get(nums[j]) == 1){
                    return nums[j];
                }
            }
        }
        return -1;
    }
}
