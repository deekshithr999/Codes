class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count_lst = [1]*len(nums)

        for i in range(len(nums)):
            #get the max of prev nums lower than the curr num
            j=i
            tmp_max = 0
            for j in range(i,-1,-1):
                if nums[j]<nums[i] and tmp_max < count_lst[j]:
                    tmp_max = count_lst[j]
            count_lst[i]=tmp_max+1
        return max(count_lst)
        