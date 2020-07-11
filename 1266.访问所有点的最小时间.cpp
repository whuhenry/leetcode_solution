#include <vector>
using namespace std;

/*
 * @lc app=leetcode.cn id=1266 lang=cpp
 *
 * [1266] 访问所有点的最小时间
 */

// @lc code=start
class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int n = points.size();
        if (1 == n) {
            return 0;
        }
        int time = 0;
        for (int i = 1; i < n; ++i) {
            int dx = abs(points[i][0] - points[i - 1][0]);
            int dy = abs(points[i][1] - points[i - 1][1]);
            time += dx > dy ? dx : dy;
        }
        return time;
    }
};
// @lc code=end

