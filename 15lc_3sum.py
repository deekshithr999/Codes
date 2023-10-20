
class Solution:
    '''
    TC: O(nlogn + n^2)
    SC: O(1)
    Combinations of 2 sum 
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r]>0:
                    r -= 1
                elif nums[i]+nums[l]+ nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l]== nums[l-1]:
                        l += 1
                    # while r > l and nums[r] == nums[r+1]:
                    #     r -= 1
        return res



class Solution:
    '''
    TC: O(nlogn + n^2)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            ele = -nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                #print("l,r  ", l, " ",r)
                if nums[l]+nums[r] < ele:
                    l +=1
                elif nums[l]+nums[r] > ele:
                    r -= 1
                else:
                    #print("here :")
                    lst = [nums[i],nums[l],nums[r]]
                    # lst.sort()
                    res.add(tuple(lst))
                    #print("res ", res)
                    l += 1
                    r -= 1
        return res

class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j]== nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k]== nums[k-1]:
                        continue
                    if nums[i]+nums[j]+ nums[k]==0:
                        res.append([nums[i], nums[j], nums[k]])
        return res


class Solution:
    '''
    TC: O(n^2)
    SC: O(n)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        dt = defaultdict(list)
        for i in range(len(nums)):
            dt[nums[i]].append(i)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                lst = dt[-(nums[i]+nums[j])]
                if len(lst)== 0:
                    continue
                for idx in lst:
                    if idx != i and idx != j:
                        tl = [nums[i],nums[j],nums[idx]]
                        tl.sort()
                        res.append(tuple(tl))
        st = list(set(res))
        return st
                

        