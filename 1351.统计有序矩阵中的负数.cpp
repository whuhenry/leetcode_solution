/*
 * @lc app=leetcode.cn id=1351 lang=cpp
 *
 * [1351] 统计有序矩阵中的负数
 */

#include <vector>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int result = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j =0; j < cols; ++j) {
                if (grid[i][j] < 0) {
                    result += cols - j;
                    break;
                }
            }
        }
        return result;
    }
};
// @lc code=end

