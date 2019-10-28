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
    void deleteNode(ListNode* node) {
        ListNode* preNode = node;
        while(node->next != nullptr) {
            int tmp = node->val;
            node->val = node->next->val;
            node->next->val = tmp;
            preNode = node;
            node = node->next;
        }
        preNode->next = nullptr;
    }
};