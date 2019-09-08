#include<vector>
using namespace std;

class Solution {
public:
	int minimumTotal(vector<vector<int>>& triangle) {
		int m = triangle.size();
		if (0 == m) { return 0; }
		if (1 == m) { return triangle[0][0]; }
		vector<int> curLine, preLine;
		preLine.resize(m);
		curLine.resize(m);

		preLine[0] = triangle[0][0];
		for (int i = 1; i < m; ++i) {
			curLine[0] = preLine[0] + triangle[i][0];
			for (int j = 1; j < i; ++j) {
				curLine[j] = min(preLine[j], preLine[j - 1]) + triangle[i][j];
			}
			curLine[i] = preLine[i - 1] + triangle[i][i];
			curLine.swap(preLine);
		}

		int minPath = preLine[0];

		for (int i = 1; i < m; ++i) {
			if (preLine[i] < minPath) {
				minPath = preLine[i];
			}
		}

		return minPath;
	}
};