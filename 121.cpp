#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();
        if (0 == length || 1 == length) {
            return 0;
        }
        int preMin = prices[0];
        int maxEarn = 0;
        for (int i = 1; i < length; ++i) {
            if (prices[i] - preMin > maxEarn) {
                maxEarn = prices[i] - preMin;
            }
            if (prices[i] < preMin) {
                preMin = prices[i];
            }
        }
        return maxEarn;
    }
};