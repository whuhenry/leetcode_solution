#include <vector>
using namespace std;
class Solution {
public:
    vector<int> printNumbers(int n) {
        vector<int> result;
        int maxN = int(pow(10, n));
        for (int i = 1; i < maxN; ++i) {
            result.push_back(i);
        }
        return result;
    }
};