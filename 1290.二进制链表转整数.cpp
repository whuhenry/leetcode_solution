/*
 * @lc app=leetcode.cn id=1290 lang=cpp
 *
 * [1290] 二进制链表转整数
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        long result = 0;
        if (nullptr == head) {
            return 0;
        }
        while (head != nullptr) {
            result = result * 2 + head->val;
            head = head->next;
        }
        return result;
    }
};
// @lc code=end

