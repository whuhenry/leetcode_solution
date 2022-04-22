/*
 * @lc app=leetcode.cn id=350 lang=cpp
 *
 * [350] 两个数组的交集 II
 */
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> map1, map2;
        for (int i = 0; i < nums1.size(); ++i) {
            if (map1.find(nums1[i]) == map1.end()) {
                map1[nums1[i]] = 1;
            } else {
                map1[nums1[i]]++;
            }
        }

        for (int i = 0; i < nums2.size(); ++i) {
            if (map2.find(nums2[i]) == map2.end()) {
                map2[nums2[i]] = 1;
            } else {
                map2[nums2[i]]++;
            }
        }

        vector<int> result;
        for (auto v : map1) {
            if (map2.find(v.first) != map2.end()) {
                int count = min(v.second, map2[v.first]);
                for (int i = 0; i < count; ++i) {
                    result.push_back(v.first);
                }
            }
        }
        return result;
    }
};
// @lc code=end

