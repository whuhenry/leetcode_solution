#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> pondSizes(vector<vector<int>>& land) {
        vector<int> result;
        int direction[8][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        for (int i = 0; i < land.size(); ++i) {
            for (int j = 0; j < land[i].size(); ++j) {
                if (0 == land[i][j]) {
                    int waterSize = 0;
                    queue<pair<int, int>> bfsList;
                    bfsList.push(make_pair(i, j));
                    land[i][j] = 1;
                    ++waterSize;
                    while(!bfsList.empty()) {
                        auto cell = bfsList.front();
                        bfsList.pop();
                        for (int d = 0; d < 8; ++d) {
                            int ti = cell.first + direction[d][0];
                            int tj = cell.second + direction[d][1];
                            if (ti >= 0 && ti < land.size() && tj >= 0 && tj < land[ti].size() && 0 == land[ti][tj]) {
                                land[ti][tj] = 1;
                                bfsList.push(make_pair(ti, tj));
                                ++waterSize;
                            }
                        }
                    }
                    result.push_back(waterSize);
                }
            }
        }

        sort(result.begin(), result.end());
        return result;
    }
};