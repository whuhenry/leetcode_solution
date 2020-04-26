/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] 判断子序列
 */

// @lc code=start
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sptr = 0, tptr = 0;
        while(sptr < s.length() && tptr < t.length()) {
            if (s[sptr] == t[tptr]) {
                ++sptr;
                ++tptr;
            } else {
                ++tptr;
            }
        }
        if (sptr == s.length()) {
            return true;
        } else {
            return false;
        }
    }
};
// @lc code=end

