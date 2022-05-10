'''

link : https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water
Hard

17891

252

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
Accepted
1,090,075
Submissions
1,934,548


'''

################################################################
'''
TC : O(n)
SC : O(1)

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        mxl,mxr=0,0
        l=0
        r=len(height)-1
        mxl=height[0]
        mxr=height[len(height)-1]
        litres=0
        while l<=r:
            #print("l r ",l," ",r)
            if mxl>mxr:
                tres=mxr-height[r]
                if tres>0:
                    litres+=tres
                mxr=max(mxr,height[r])
                r-=1
            else:
                tres=mxl-height[l]
                if tres>0:
                    litres+=tres
                mxl=max(mxl,height[l])
                l+=1
        return litres

################################################################
'''
TC : O(3n)
SC :O(2n)

Approach : Water level at a point = min(max height bw left and right)-block at that point

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        
        mx_hf_left=[0]*len(height)
        mx_hf_right=[0]*len(height)
        mx=0
        if len(height)==0:
            return 0
        mx_hf_left[0]=height[0]
        for i in range(1,len(height)):
            mx_hf_left[i]=max(mx_hf_left[i-1],height[i])
            
        mx_hf_right[len(height)-1]=height[len(height)-1]
        
        for j in range(len(height)-2,0,-1):
            mx_hf_right[j]=max(mx_hf_right[j+1],height[j])
        litres=0
        
        for i in range(1,len(height)-1):
            tres=min(mx_hf_left[i-1],mx_hf_right[i+1])-height[i]
            if tres>0:
                litres+=tres
        
        return litres
            

################################################################
'''
TC : Too much O(sum(list)*n)
SC : O(1)

Approach : removing the brick one by one
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        
        Allzero=False
        
        # i=0
        # j=i+1
        l=len(height)
        litres=0
        while Allzero!=True:
            i=0
            j=i+1
            while True:
                    if i>=l or j>=l:
                        
                        break
                    while i<l-1 and height[i]==0:
                        i+=1

                    j=i+1
                    while j<l and height[j]==0:
                        j+=1
                    if i<j and j<l:
                        if j-i>1:
                            litres+=(j-i-1)
                            i=j
                            j=j+1
                        elif j-i ==1:
                            i=j
                            j=j+1
            for i in range(len(height)):
                if height[i]>0:
                    height[i]-=1
            s=sum(height)
            if s==0:
                Allzero=True
        
        return litres