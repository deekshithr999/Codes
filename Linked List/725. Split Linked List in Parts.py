# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodeCnt = self.cntNodes(head)
        baseCnt, rem = nodeCnt//k, nodeCnt%k
        res = []
        curr = head
        for i in range(k):
            res.append(curr)
            for j in range(baseCnt + (1 if rem else 0)-1):
                if not curr: break
                curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            rem -= 1 if rem else 0
        return res


    def cntNodes(self, head):
        if not head :
            return 0
        return 1+self.cntNodes(head.next)

        