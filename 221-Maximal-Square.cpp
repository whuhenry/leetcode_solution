#include <vector>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        vector<int> maxSquareSize, maxSquareSizePreRow, maxUpperLength;
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
        for (int j = 0; j < cols; ++j) {
            if ('1' == matrix[0][j]) {
                maxSquareSizePreRow[j] = 1;
                maxUpperLength[j] = 1;
                maxSquare = 1;
            } else {
                maxSquareSizePreRow[j] = 0;
                maxUpperLength[j] = 0;
            }
        }

        for (int i = 1; i < rows; ++i) {
            int maxSquareLine = 0;
            if ('1' == matrix[i][0]) {
                maxSquareSize[0] = 1;
                maxUpperLength[0] += 1;
                maxLeftLength = 1;
                maxSquareLine = 1;
            } else {
                maxSquareSizePreRow[0] = 0;
                maxUpperLength[0] = 0;
                maxLeftLength = 0;
                maxSquareLine = 0;
            }
            for (int j = 1; j < cols; ++j) {
                if ('1' == matrix[i][j]) {
                    maxSquareSize[j] = min(min(maxSquareSizePreRow[j - 1], maxUpperLength[j]), maxLeftLength) + 1;
                    maxUpperLength[j] += 1;
                    maxLeftLength += 1;
                    if (maxSquareSize[j] > maxSquareLine) {
                        maxSquareLine = maxSquareSize[j];
                    }
                } else {
                    maxSquareSize[j] = 0;
                    maxUpperLength[j] = 0;
                    maxLeftLength = 0;
                }
            }
            maxSquare = max(maxSquare, maxSquareLine);
            maxSquareSize.swap(maxSquareSizePreRow);
        }

        return maxSquare * maxSquare;
    }
};