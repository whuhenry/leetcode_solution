#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int rows = matrix.size();
        if (0 == rows) {
            return result;
        }
        int cols = matrix[0].size();
        if (0 == cols) {
            return result;
        }
        int count = rows * cols;

        int left = 0, right = cols - 1, up = 0, down = rows - 1;
        pair<int, int> curPos = {0, 0};
        vector<pair<int, int>> direction;
        direction.push_back({0, 1});
        direction.push_back({1, 0});
        direction.push_back({0, -1});
        direction.push_back({-1, 0});
        int directionIdx = 0;
        while (result.size() < count) {
            while(curPos.first >= up && curPos.first <= down && curPos.second >= left && curPos.second <= right) {
                result.push_back(matrix[curPos.first][curPos.second]);
                curPos.first += direction[directionIdx].first;
                curPos.second += direction[directionIdx].second;
            }
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
        }

        return result;
    }
};