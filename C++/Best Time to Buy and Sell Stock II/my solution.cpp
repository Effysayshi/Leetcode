//Say you have an array for which the ith element is the price of a given stock on day i.

//Design an algorithm to find the maximum profit.           ----*----Input: [7,1,5,3,6,4]
//You may complete as many transactions as you like         ----*----Output: 7
//But you must sell the stock before you buy again).

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sum = 0;
        int n = prices.size();
           
        for(int i = 0; i < n - 1; i++)
        {
            if(prices[i+1] - prices[i] > 0)
                sum += prices[i+1] - prices[i];
        }
        return sum;
    }
};
