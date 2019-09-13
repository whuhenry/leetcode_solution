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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* headCopy = nullptr;
        ListNode* result = new ListNode(0);
        headCopy = result;
        while(nullptr != head){
            if (nullptr == head->next) {
                result->next = head;
                result = result->next;
            } else if (head->next->val != head->val) {
                result->next = head;
                result = result->next;
            } else {
                //找到下一个不重复
                while(nullptr != head->next && head->next->val == head->val) {
                    head = head->next;
                }
            }
            head = head->next;
        }
        result->next = nullptr;

        return headCopy->next;
    }
};