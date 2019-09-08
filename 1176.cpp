#include<vector>
using namespace std;

class Solution {
public:
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int result = 0;
        int length = calories.size();
        int sum = 0;
        for (int i = length - 1; i >= 0; --i) {
            if (i + k <= length - 1) {
                sum -= calories[i + k];
            }
            sum += calories[i];
            if (sum < lower) {
                --result;
            }
            if (sum > upper) {
                ++result;
            }
        }

        return result;
    }
};