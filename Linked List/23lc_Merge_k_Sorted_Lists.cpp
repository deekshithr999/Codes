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
// class Solution {
// public:
//     ListNode* mergeKLists(vector<ListNode*>& lists) {
        
//     }
// };

class Solution {
/* 
* TC: O(n*k)
* SC: O(1)
*/
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *dummyNode = new ListNode();
        ListNode *iter = dummyNode;
        while (true){
            int minIdx = -1;
            int minValue = 10000;
            for (int i = 0; i < lists.size(); i++){
                if (!(lists.empty()) && lists[i] != nullptr && lists[i]-> val < minValue){
                    minValue = lists[i]->val;
                    minIdx = i;
                }
            }
            if(minIdx == -1)break;
            iter->next = lists[minIdx];
            iter= iter->next;
            lists[minIdx] = lists[minIdx]->next;
        }
        return dummyNode->next;

    }
};
