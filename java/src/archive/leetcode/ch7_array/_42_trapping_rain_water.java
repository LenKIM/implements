package archive.leetcode.ch7_array;

/**
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
 */
public class _42_trapping_rain_water {

    public static void main(String[] args) {
        _42_trapping_rain_water a = new _42_trapping_rain_water();
        int[] aa = {0, 1, 0, 2, 1};
        a.trap(aa);

    }

    public int trap(int[] height) {

        if (height.length == 0) {
            return 0;
        }

        int left = 0, right = height.length - 1;
        int volumn = 0;

        int left_max = height[left];
        int right_max = height[right];

        while (left < right) {
            left_max = Math.max(height[left], left_max);
            right_max = Math.max(height[right], right_max);

            // 더 높은 쪽을 향해 포인터 이동
            if (left_max <= right_max) {
                volumn += left_max - height[left];
                left += 1;
            } else {
                volumn += right_max - height[right];
                right -= 1;
            }
        }
        return volumn;
    }
}
