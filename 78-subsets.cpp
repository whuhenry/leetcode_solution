#include <vector>
using namespace std;

class Solution {
public:
    void generate(vector<int>& nums, int maxCount, int curIdx) {
        if (maxCount == tmp.size()) {
            result.push_back(tmp);
        } else {
            if (nums.size() - curIdx + tmp.size() < maxCount) {
                return;
            } else {
                for (int i = curIdx; i < nums.size(); ++i) {
                    tmp.push_back(nums[i]);
                    generate(nums, maxCount, i + 1);
                    tmp.pop_back();
                }
            }
        }
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        for (int i = 1; i <= nums.size(); ++i) {
            generate(nums, i, 0);
            tmp.clear();
        }
        result.push_back(tmp);

        return result;
    }

    vector<vector<int>> result;
    vector<int> tmp;
};