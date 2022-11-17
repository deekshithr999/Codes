'''

Link : https://leetcode.com/problems/combination-sum/
39. Combination Sum
Medium

10875

236

Add to List

Share
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
Accepted
1,081,177
Submissions
1,647,823

'''
####################################################
'''
Somewhat better than below
without using sum( ) fn

'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates.sort()
        reslst=[]
        tlst=[]
        self.depthSum(candidates,target,0,tlst,reslst)
        return reslst
        
        
    
    def depthSum(self, candidates, target, start, tlst,reslst):
        if start == len(candidates):
            return
        
        for i in range(start,len(candidates)):
            ttlst =tlst[:]
            ttlst.append(candidates[i])
            #target -=candidates[i]
            if target-candidates[i] <0:
                continue
            elif target-candidates[i]>0:
                self.depthSum(candidates,target-candidates[i],i,ttlst,reslst)
            else:
                reslst.append(ttlst)
 

####################################################

'''
TC : O(2^n * target)
SC : O(2^n * target)
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #candidates.sort()
        reslst=[]
        tlst=[]
        self.depthSum(candidates,target,0,tlst,reslst)
        return reslst
        
        
    
    def depthSum(self, candidates, target, start, tlst,reslst):
        if start == len(candidates):
            return
        
        for i in range(start,len(candidates)):
            ttlst =tlst[:]
            ttlst.append(candidates[i])
            s= sum(ttlst)
            if s> target:
                continue
            elif s< target:
                self.depthSum(candidates,target,i,ttlst,reslst)
            else:
                reslst.append(ttlst)
        
        
        