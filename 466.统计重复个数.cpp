/*
 * @lc app=leetcode.cn id=466 lang=cpp
 *
 * [466] 统计重复个数
 */
#include<string>
#include<map>
#include<iostream>
using namespace std;

// @lc code=start
class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        // find first
        int s1Count = 0, s2Count = 0, s1Idx = 0, s2Idx = 0;
        map<int, pair<int, int>> recall;
        int repeatlength = -1, s2RepeatCount = -1;
        while(s1Count <= n1) {
            while(true) {
                if (s1[s1Idx] == s2[s2Idx]) {
                    ++s2Idx;
                    if (s2Idx >= s2.length()) {
                        break;
                    }                    
                }
                ++s1Idx;
                if (s1Idx >= s1.length()) {
                    s1Idx = 0;
                    ++s1Count;
                }
            }

            if (recall.find(s1Idx) != recall.end()) {
                repeatlength = (s1Count - recall[s1Idx].first) * s1.length();
                s2RepeatCount = s2Count - recall[s1Idx].second;
                break;
            } else {
                recall[s1Idx] = make_pair(s1Count, s2Count);
            }

            ++s2Count;
            ++s1Idx;
            s2Idx = 0;
        }

        if (repeatlength == -1){
            if (s2Count < 1) {
                return 0;
            } else {
                return s2Count / n2;
            }
        }

        int s1RepeatCount = n1 * s1.length() / repeatlength;
        int remains2Count = 0;




        int s2CountInS1 = s1RepeatCount * repeatlength / s2.length() + remains2Count + 1;

        
        return s2CountInS1 / n2;

        // find second
        
    }
};
// @lc code=end

int main() {
    Solution s;
    cout << s.getMaxRepetitions("aaa", 3, "aa", 1) << endl;
}