//本来很简单的问题，但是要注意很多细节
//评论区有很多很巧妙和简洁的实现，值得借鉴

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (nullptr == l1) return l2;
        if (nullptr == l2) return l1;
        ListNode *result = nullptr;
        if (l1->val <= l2->val) {
            result = new ListNode(l1->val);
            l1 = l1->next;
        } else {
            result = new ListNode(l2->val);
            l2 = l2->next;
        }
        ListNode *start = result;
        while (nullptr != l1 || nullptr != l2) {
            if (nullptr == l1) {
                result->next = l2;
                l2 = nullptr;
            } else if (nullptr == l2) {
                result->next = l1;
                l1 = nullptr;
            } else if (l1->val <= l2->val) {
                result->next = new ListNode(l1->val);
                result = result->next;
                l1 = l1->next;
            } else {
                result->next = new ListNode(l2->val);
                result = result->next;
                l2 = l2->next;
            }
        }
        return start;
    }
};