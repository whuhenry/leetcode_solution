#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        vector<double> mulResult;
        if (0 == n) {
            return 1;
        }
        uint64_t count = 1;
        if (n < 0) {
            x = 1 / x;
        }
        uint64_t newN = n;
        if (n < 0) {
            newN = -newN;
        }

        mulResult.push_back(x);
        while(count <= newN / 2) {
            count *= 2;
            mulResult.push_back(mulResult[mulResult.size() - 1] * mulResult[mulResult.size() - 1]);
        }

        int cur = mulResult.size() - 1;
        double result = 1;
        while (newN > 0 && cur >= 0) {
            if (newN >= count) {
                newN -= count;
                result *= mulResult[cur];
            }
            count /= 2;
            --cur;
        }
        return result;
    }
};