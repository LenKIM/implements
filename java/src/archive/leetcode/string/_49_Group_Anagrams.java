package archive.leetcode.string;

import java.util.*;

/**
 * https://leetcode.com/problems/group-anagrams/
 * <p>
 * Input: strs = ["eat","tea","tan","ate","nat","bat"]
 * Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 * <p>
 * Input: strs = [""]
 * Output: [[""]]
 * <p>
 * Input: strs = ["a"]
 * Output: [["a"]]
 */
class _49_Group_Anagrams {
    public List<List<String>> groupAnagrams(String[] strs) {

        if (strs.length == 0) {
            return new ArrayList<>();
        }
        Map<String, List<String>> ans = new HashMap<>();

        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String key = String.valueOf(ca);
            if (!ans.containsKey(key)) {
                ans.put(key, new ArrayList<>());
            }
            ans.get(key).add(s);
        }
        return new ArrayList<>(ans.values());
    }
}