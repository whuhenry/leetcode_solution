#include <vector>
using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        //{横向，竖向}
        vector<pair<int, int>> maxSquareSize, maxSquareSizePreRow;
        vector<pair<int, int>> maxSquareSize, maxSquareSizePreRow;
        vector<int> maxUpperLength;
        int maxLeftLength = 0;
        int rows = matrix.size();
        if (0 == rows) {
            return 0;
        }
        int maxSquare = 0;
        int cols = matrix[0].size();
        maxSquareSize.resize(cols);
        maxSquareSizePreRow.resize(cols);
        maxUpperLength.resize(cols);
        //第一行
        maxLeftLength = 0;
        for (int j = 0; j < cols; ++j) {
            if ('1' == matrix[0][j]) {
                maxSquareSizePreRow[j] = {maxLeftLength + 1, 1};
                maxUpperLength[j] = 1;
                maxSquare = 1;
                maxLeftLength += 1;
                maxSquare = max(maxSquare, maxLeftLength);
            } else {
                maxSquareSizePreRow[j] = {0, 0};
                maxUpperLength[j] = 0;
                maxLeftLength = 0;
            }
        }


        //后面1-n行
        for (int i = 1; i < rows; ++i) {
            int maxSquareLine = 0;
            if ('1' == matrix[i][0]) {
                maxSquareSize[0] = {1, maxUpperLength[0] + 1};
                maxUpperLength[0] += 1;
                maxLeftLength = 1;
                maxSquareLine = maxUpperLength[0];
            } else {
                maxSquareSizePreRow[0] = {0, 0};
                maxUpperLength[0] = 0;
                maxLeftLength = 0;
                maxSquareLine = 0;
            }
            for (int j = 1; j < cols; ++j) {
                if ('1' == matrix[i][j]) {
                    maxSquareSize[j] = { min(maxLeftLength, maxSquareSizePreRow[j - 1].first) +1,
                                         min(maxUpperLength[j], maxSquareSizePreRow[j - 1].second) + 1};
                    maxUpperLength[j] += 1;
                    maxLeftLength += 1;
                    if (maxSquareSize[j].first * maxSquareSize[j].second > maxSquareLine) {
                        maxSquareLine = maxSquareSize[j].first * maxSquareSize[j].second;
                    }
                } else {
                    maxSquareSize[j] = {0, 0};
                    maxUpperLength[j] = 0;
                    maxLeftLength = 0;
                }
            }
            maxSquare = max(maxSquare, maxSquareLine);
            maxSquareSize.swap(maxSquareSizePreRow);
        }

        return maxSquare;
    }
};