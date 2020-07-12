#include <vector>
using namespace std;

class Solution {
public:
    int minCount(vector<int>& coins) {
        int count = 0;
        for (int i = 0; i < coins.size(); ++i) {
            count += coins[i] / 2 + coins[i] % 2;
        }
        return count;
    }
};