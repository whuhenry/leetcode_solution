/*
 * @lc app=leetcode.cn id=1299 lang=cpp
 *
 * [1299] 将每个元素替换为右侧最大元素
 */

// @lc code=start
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int len = arr.size();
        int maxNum = arr[len - 1];
        arr[len - 1] = -1;
        for (int i = len - 2; i >= 0; --i) {
            int tmp = maxNum;
            if (arr[i] > maxNum) {
                maxNum = arr[i];
            }
            arr[i] = tmp;            
        }
        return arr;
    }
};
// @lc code=end

