package archive.leetcode.string;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.stream.Collectors;

public class _6_ValidPalindrome {

    public boolean isPalindrome(String s) {
        String abc = s.toLowerCase().trim();
        Deque<Character> a = new ArrayDeque<>(abc.length());

        List<Character> result = abc.chars()
                .mapToObj(x -> (char) x)
                .filter(x -> Character.isAlphabetic(x) || Character.isDigit(x))
                .collect(Collectors.toList());

        a.addAll(result);

        while(a.size() > 1) {
            Character last = a.removeLast();
            Character first = a.removeFirst();
            if (!last.equals(first)){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {

    }
}