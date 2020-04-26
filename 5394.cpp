#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        int total = 0;
        int rows = nums.size();
        for (int i = 0; i < nums.size(); ++i) {
            if( i + nums[i].size() > total) {
                total = i + nums[i].size();
            }
        }
        
        vector<int> result;
        vector<int> rowIdxs;
        rowIdxs.push_back(0);
        for (int i = 0; i < total; ++i) {
            vector<int> tmp;
            if (i + 1 < rows) {
                tmp.push_back(i + 1);
            }
            for (int rowIdx : rowIdxs) {
                int colIdx = i - rowIdx;
                if (colIdx < nums[rowIdx].size()) {
                    result.push_back(nums[rowIdx][colIdx]);
                    tmp.push_back(rowIdx);
                }
            }
            rowIdxs.swap(tmp);
        }
        
        return result;
    }
};

int main() {
    Solution s;
    vector<vector<int>> num = {{1,2,3},{4,5,6},{7,8,9}};
    s.findDiagonalOrder(num);
    return 0;
}