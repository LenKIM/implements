package archive.leetcode.string;

/**
 * https://leetcode.com/problems/reverse-string
 * In-place Order 테스트하기
 */
public class _344_ReverseString {

    public void reverseString(char[] s) {
        helper(s, 0, s.length - 1);
    }

    public void helper(char[] s, int left, int right) {
        if (left >= right) return;

        char tmp = s[left];

        s[left] = s[right];
        left = left + 1;

        s[right] = tmp;
        right = right - 1;

        helper(s, left, right);
    }

    public void reverseString2(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left++] = s[right];
            s[right--] = tmp;
        }
    }

}
