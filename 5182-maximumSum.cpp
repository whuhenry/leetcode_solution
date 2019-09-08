#include <vector>
using namespace std;

class Solution {
public:
	int maximumSum(vector<int>& arr) {
		int arrLength = arr.size();

		if (1 == arrLength) {
			return arr[0];
		}
		int result = arr[0];

		int sum, presum, preSumMin, prepreSumMin, preMinMinux, prepreMinMinux;
		presum = arr[0];
		prepreSumMin = 0;
		prepreMinMinux = arr[0];
		int maxContinue = arr[0];
		for (int i = 1; i < arrLength; ++i) {
			sum = presum + arr[i];
			preSumMin = min(prepreSumMin, presum);
			maxContinue = max(maxContinue, sum - preSumMin);

			preMinMinux = min(arr[i] + prepreSumMin, prepreMinMinux);

			if (1 == i) {
				result = max(result, max(sum, maxContinue));
			}
			else {
				result = max(result, max(sum - preMinMinux, maxContinue));
			}

			presum = sum;
			prepreSumMin = preSumMin;
			prepreMinMinux = preMinMinux;
		}

		return result;
	}
};