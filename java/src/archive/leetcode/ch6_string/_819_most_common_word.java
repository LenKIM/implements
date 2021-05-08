package archive.leetcode.ch6_string;

import java.util.*;

/**
 *
 * https://leetcode.com/problems/most-common-word
 *
 */
public class _819_most_common_word {

    public String mostCommonWord(String paragraph, String[] banned) {

        String normalizedStr = paragraph.replaceAll("[^a-zA-Z0-9 ]", " ").toLowerCase();

        String[] words = normalizedStr.split("\\s+");

        Set<String> bannedWords = new HashSet();
        bannedWords.addAll(Arrays.asList(banned));

        Map<String, Integer> wordCount = new HashMap();

        for (String word : words) {
            if (!bannedWords.contains(word))
                wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        return Collections.max(wordCount.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}
