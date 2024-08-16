# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    TC: O(nlogk) k: #lists n: tot no of elems 
    SC: O(n)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists)>1:
            mergedLst = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLst.append(self.merge2Lists(l1, l2))
            lists = mergedLst
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next =l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next


        

class Solution:
    '''
    TC: O(n*m)
    SC: O(1)
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummyNode = ListNode()
        iterNode = dummyNode

        while True:
            minVal = 10001
            minIdx = -1

            for idx, lst in enumerate(lists):
                if lst and lst.val < minVal:
                    minIdx = idx
                    minVal = lst.val
            if minIdx == -1:
                break
            iterNode.next = lists[minIdx]
            iterNode = iterNode.next
            lists[minIdx] = lists[minIdx].next
        return dummyNode.next