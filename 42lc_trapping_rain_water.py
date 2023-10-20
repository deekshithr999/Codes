
class Solution:
    '''
    Two pointer problem **too good**
    TC: O(n)
    SC: O(1)
    '''
    def trap(self, height: List[int]) -> int:
        tot_water = 0
        mx_l, mx_r = 0, 0
        l,r = 0, len(height)-1
        while l<=r:
            if mx_l < mx_r:
                if mx_l>height[l]:
                    tot_water += (mx_l-height[l])
                mx_l = max(mx_l, height[l])
                l += 1
            else :
                if mx_r > height[r]:
                    tot_water += (mx_r - height[r])
                mx_r = max(mx_r, height[r])
                r -= 1
        return tot_water
        

class Solution:
    '''
    TC: O(2n)
    SC: O(n)
    '''
    def trap(self, height: List[int]) -> int:
        tot_water=0
        left_max = [0]*len(height)
        left_max[0]=height[0]
        right_max = height[len(height)-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        
        for i in range(len(height)-2,0,-1):
            storage = min(left_max[i-1], right_max)
            if storage > height[i]:
                tot_water += (storage-height[i])
            right_max = max(right_max, height[i])
        return tot_water
        


class Solution:
    '''
    TC: O(3n)
    SC: O(2n)
    '''
    def trap(self, height: List[int]) -> int:
        res = 0
        left_max, right_max = [0]*len(height), [0]*len(height)
        left_max[0]=height[0]
        right_max[len(height)-1]=height[len(height)-1]
        for i in range(1, len(height)):
            left_max[i]= max(left_max[i-1],height[i])

        for i in range(len(height)-2,-1,-1):
            right_max[i]= max(right_max[i+1],height[i])
        # print("lmax :", left_max)
        # print("rmax :", right_max)
        for i in range(1, len(height)-1):
            storage = min(left_max[i-1],right_max[i+1])
            if storage<=height[i]:
                continue
            # print ("i = ", i, "res : ",res)
            res += (storage-height[i])
        return res


class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def left_max(self, height, idx):
        lmax=0
        for i in range(idx):
            lmax= max(lmax, height[i])
        return lmax
    def right_max(self, height, idx):
        rmax = 0
        for i in range(idx+1, len(height)):
            rmax = max(rmax, height[i])
        return rmax

    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            storage = min(self.left_max(height,i),self.right_max(height,i))
            if storage <= height[i]:
                continue
            res += storage-height[i]
        return res
        