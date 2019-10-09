#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		int count = nums.size();
		vector<vector<int>> result;
		if (3 > count) {
			return result;
		}
		sort(nums.begin(), nums.end());

		int lastFirst = nums[0] + 1;
		for (int i = 0; i < count - 2; ++i) {
			if (nums[i] == lastFirst) {
				continue;
			}
			if (nums[i] > 0) {
				break;
			}
			lastFirst = nums[i];
			int firstpos = i + 1;

			while (firstpos < count - 1) {
				int sum = nums[i] + nums[firstpos];
				if (sum > 0) {
					break;
				}
				int searchBegin = firstpos + 1, searchEnd = count - 1;
				while (searchBegin <= searchEnd) {
					int center = (searchBegin + searchEnd) / 2;
					if (0 == sum + nums[center]) {
						result.push_back({ nums[i], nums[firstpos], nums[center] });
						break;
					}
					else if (0 < sum + nums[center]) {
						searchEnd = center - 1;
					}
					else {
						searchBegin = center + 1;
					}
				}

				int curfirst = nums[firstpos];
				++firstpos;
				while (firstpos < count && nums[firstpos] == curfirst) {
					++firstpos;
				}
			}
		}

		return result;
	}
};