// 注意：官方题解中的Boyer-Moore算法及其牛逼，值得学习
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = nums.size();
        map<int, int> numsCount;
        for (int num : nums) {
            if (numsCount.find(num) == numsCount.end()) {
                numsCount[num] = 1;
            } else {
                numsCount[num] += 1;
            }
        }
        for (auto pair : numsCount) {
            if (pair.second > count / 2) {
                return pair.first;
            }
        }
        return 0;
    }
};