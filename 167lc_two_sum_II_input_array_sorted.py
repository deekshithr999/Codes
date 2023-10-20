'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''

class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            tmp = numbers[l]+numbers[r]
            if tmp == target:
                return l+1,r+1
            elif tmp < target:
                l += 1
            elif tmp > target:
                r -= 1
        return -1,-1

        

class Solution:
    '''
    TC: O(nlogn)
    SC: O(1)
    '''

    def binarySearch(self, numbers, target, left, right):
        while left <= right:
            middle = left + (right-left)//2
            if numbers[middle]==target:
                return middle
            elif target < numbers[middle]:
                right = middle-1
            elif target > numbers[middle]:
                left = middle+1
            # print("l,r,m ", left, " ", right, " ", middle)
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            req= target-numbers[i]
            req_idx = self.binarySearch(numbers, req,0, i-1)
            if req_idx != -1:
                return req_idx+1, i+1

        
class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return i+1, j+1
                    
        