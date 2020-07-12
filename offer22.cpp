/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* cur = head;
        ListNode* pre = head;
        int count = 0;
        while (cur != nullptr) {
            cur = cur->next;
            ++count;
            if (count > k) {
                pre = pre->next;
            }
        }
        return pre;
    }
};