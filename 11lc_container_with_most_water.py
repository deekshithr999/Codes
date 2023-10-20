
class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0, len(height)-1
        while l<r:
            area= (r-l)*min(height[l],height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        

class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for l1 in range(len(height)):
            for l2 in range(l1+1, len(height)):
                max_area = max(max_area, (l2-l1)*min(height[l1],height[l2]))
        return max_area

        