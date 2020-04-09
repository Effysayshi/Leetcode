//Given a non-empty,singly linked list with head node head,          ---*---Input: [1,2,3,4,5]
//return a middle node of linked list.                               ---*---Output: Node 3 from this list (Serialization: [3,4,5])
//If there are two middle nodes, return the second middle node.




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
    ListNode* middleNode(ListNode* head) {
        ListNode* fast_p = head;
        ListNode* slow_p = head;
        
        if(head != NULL)
            while(fast_p!=NULL && fast_p->next!=NULL)
            {
                slow_p = slow_p->next;
                fast_p = fast_p->next->next;
            }
      
        return slow_p;
    }
};
