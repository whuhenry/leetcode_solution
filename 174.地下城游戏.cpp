/*
 * @lc app=leetcode.cn id=174 lang=cpp
 *
 * [174] 地下城游戏
 */

#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int rows = dungeon.size();
        if (0 == rows) { return 0; }
        int cols = dungeon[0].size();
        if (0 == cols) { return 0; }
        vector<vector<int>> blood;
        vector<vector<int>> minblood;
        blood.resize(rows);
        for (int i = 0; i < rows; ++i) 
        {
            blood[i].resize(cols);
        }

        for (int i = rows - 1 ; i >= 0; --i) 
        {
            for (int j = cols - 1; j >= 0; --j) 
            {
                if (i < rows - 1 && j < cols - 1) {
                    blood[i][j] = max(min(blood[i + 1][j], blood[i][j + 1]) - dungeon[i][j], 1);
                } else if (i < rows - 1) {
                    blood[i][j] = max(blood[i + 1][j] - dungeon[i][j], 1);
                } else if (j < cols - 1) {
                    blood[i][j] = max(blood[i][j + 1] - dungeon[i][j], 1);
                } else {
                    blood[i][j] = max(1 - dungeon[i][j], 1);
                }
            }
        }

        return blood[0][0];
    }
};
// @lc code=end

