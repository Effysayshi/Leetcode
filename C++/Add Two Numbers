/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;
        
        ListNode* res = new ListNode();
        ListNode* tmp = res;
        
        int carry = 0;
        int sum = 0;
        int c1,c2;
        while ( l1||l2||carry )
        {
            c1 = l1 ? l1->val : 0;
            c2 = l2 ? l2->val : 0;
            sum = c1 + c2 + carry;
            carry = sum / 10;
            tmp->next = new ListNode(sum % 10);
            tmp = tmp->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }

        return res->next;
    }
};
