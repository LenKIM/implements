package archive.leetcode.ch7_array;

import java.util.HashMap;

/**
 * https://leetcode.com/problems/two-sum/
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Output: Because nums[0] + nums[1] == 9, we return [0, 1].
 * 런타임 - 2 ms
 * 메모리 39.3 MB
 */
public class _1_two_sum {

    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> map = new HashMap<>(); // key - val, value - idx
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
//            map.remove(nums[i]); // 2개 다 사라짐. 하나만 사라지지 않음.
            int val = target - nums[i];
            if (map.containsKey(val) && map.get(val) != i) {
                Integer idx = map.get(val);
                if (i > idx) {
                    result[0] = idx;
                    result[1] = i;
                } else {
                    result[1] = idx;
                    result[0] = i;
                }
                return result;
            }

        }
        return result;
    }

    public static void main(String[] args) {
        _1_two_sum main = new _1_two_sum();
//        int[] nums = {3, 3};
        int[] nums = {-1,-2,-3,-4,-5};
        int target = -8;
//        int target = 6;
        main.twoSum(nums, target);
    }
}
