/*
 * @lc app=leetcode.cn id=1436 lang=cpp
 *
 * [1436] 旅行终点站
 */

#include <vector>
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        bool findNext = true;
        string dest = paths[0][1];
        while (findNext) {
            findNext = false;
            for (int i = 0; i < paths.size(); ++i) {
                if (paths[i][0] == dest) {
                    dest = paths[i][1];
                    findNext = true;
                    break;
                }
            }
        }
        return dest;
    }
};
// @lc code=end

