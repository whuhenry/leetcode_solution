#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result;
        if (0 == n) {
            return result;
        }
        result.resize(n);
        for (int i = 0; i < n; ++i) {
            result[i].resize(n);
        }
        int count = n * n;

        int left = 0, right = n - 1, up = 0, down = n - 1;
        pair<int, int> curPos = {0, 0};
        vector<pair<int, int>> direction;
        direction.push_back({0, 1});
        direction.push_back({1, 0});
        direction.push_back({0, -1});
        direction.push_back({-1, 0});
        int directionIdx = 0;
        int curNum = 1;
        while (curNum <= count) {
            while(curPos.first >= up && curPos.first <= down && curPos.second >= left && curPos.second <= right) {
                result[curPos.first][curPos.second] = curNum;
                ++curNum;
                curPos.first += direction[directionIdx].first;
                curPos.second += direction[directionIdx].second;
            }
            curPos.first -= direction[directionIdx].first;
            curPos.second -= direction[directionIdx].second;
            switch (directionIdx)
            {
                case 0:
                    ++up;;
                    break;
                case 1:
                    --right;
                    break;
                case 2:
                    --down;
                    break;
                case 3:
                    ++left;
                    break;
                default:
                    break;
            }
            directionIdx = (directionIdx + 1) % 4;
            curPos.first += direction[directionIdx].first;
            curPos.second += direction[directionIdx].second;
        }

        return result;
    }
};