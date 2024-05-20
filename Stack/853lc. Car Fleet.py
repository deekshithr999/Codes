class Solution:
    '''
    TC: O(n+nlogn)
    SC: O(n)
    '''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort()
        stack = []
        for p,s in pair[::-1]:
            time = (target-p)/s
            if not stack:
                stack.append(time)
            elif stack[-1]<time:
                stack.append(time)
        return len(stack)
        