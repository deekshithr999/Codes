class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        timeTaken = 0
        for i, ele in enumerate(tickets):
            if i <= k:
                timeTaken += min(tickets[k], tickets[i])
            else:
                timeTaken += min(tickets[k]-1, tickets[i])
        return timeTaken