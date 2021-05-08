package archive.leetcode.ch21greedy;

/**
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
 * Input: prices = [7,1,5,3,6,4]
 * Output: 7
 * Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 * Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
 * [7,1,5,3,6,4]
 * [1,5,3,6,4,0]
 */
public class BestTimeToBuyAndSellStock2 {

    public int maxProfit(int[] prices) {
        int[] temp_price = new int[prices.length];
        if (prices.length - 1 >= 0) {
            System.arraycopy(prices, 1, temp_price, 0, prices.length - 1);
        }
        int result = 0;
        for (int i = 0; i < prices.length; i++) {
            int i1 = prices[i] - temp_price[i];
            if (i1 < 0) {
                result += i1;
            }
        }
        return Math.abs(result);
    }
}
