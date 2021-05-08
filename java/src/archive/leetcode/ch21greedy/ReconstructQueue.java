package archive.leetcode.ch21greedy;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class ReconstructQueue {


    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (o1, o2) -> {
            int compare = Integer.compare(o2[0], o1[0]);
            if (compare == 0) {
                return Integer.compare(o1[1], o2[1]);
            }
            return compare;
        });

        List<int[]> result = new LinkedList<>();

        for (int[] person : people) {
            int height = person[0];
            int tallerCount = person[1];

            result.add(tallerCount, new int[]{height, tallerCount});
        }
        int[][] ints = result.stream().toArray(int[][]::new);
        // List to Array
//        return ints;
        return ints;
    }

    public static void main(String[] args) {
        int[][] temp = {{7, 0}, {4, 4}, {7, 1}, {5, 0}, {6, 1}, {5, 2}};
        ReconstructQueue reconstructQueue = new ReconstructQueue();
        reconstructQueue.reconstructQueue(temp);

    }
}
