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
    int kthToLast(ListNode* head, int k) {
        int len = 0;
        ListNode* ptr = head;
        while (nullptr != ptr) {
            ++len;
            ptr = ptr->next;
        }
        int target = len - k;
        int count = 0;
        ptr = head;
        while (nullptr != ptr) {
            if (target == count) {
                return ptr->val;
            }
            ++count;
            ptr = ptr->next;
        }
        return 0;
    }
};