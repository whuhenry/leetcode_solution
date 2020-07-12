/*
 * @lc app=leetcode.cn id=202 lang=cpp
 *
 * [202] 快乐数
 */

#include <unordered_set>
using namespace std;

// @lc code=start
class Solution {
public:
    unsigned int calc(unsigned int n) {
        unsigned int result = 0;
        unsigned int tmp;
        while (n > 0) {
            tmp = n % 10;
            result += tmp * tmp;
            n /= 10;
        }
        return result;
    }

    bool isHappy(int n) {
        unordered_set<unsigned long> exist;
        unsigned int tmp = n;
        while (1 != tmp && exist.find(tmp) == exist.end()) {
            exist.insert(tmp);
            tmp = calc(tmp);
        }
        if (1 == tmp) {
            return true;
        } else {
            return false;
        }
    }
};
// @lc code=end

int main() {
    Solution s;
    s.isHappy(19);
}