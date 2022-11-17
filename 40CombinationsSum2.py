'''
Link : https://leetcode.com/problems/combination-sum-ii/

40. Combination Sum II
Medium

5253

137

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
Accepted
553,650
Submissions
1,056,807
'''


##########################################################

'''
TC : O(2^n)+O(nlogn)
SC : O(2^n)

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        reslst=[]
        lst=[]
        self.addsubsets(candidates,target,0,lst,reslst)
        return reslst
    
    
    def addsubsets(self, candidates, target, start,lst,reslst):
        #print("lst ",lst)
        if start ==len(candidates):
            return 
        
        for i in range(start,len(candidates)):
            #print ("i : ",i)
            if (i> 0 and i-1 >= start) and candidates[i]==candidates[i-1]:
                continue
            
            if target-candidates[i]<0:
                break
            ttlst=lst[:]
            ttlst.append(candidates[i])
            if target - candidates[i]==0:
                reslst.append(ttlst)
                break
            else:
                self.addsubsets(candidates,target-candidates[i],i+1,ttlst,reslst)
 
