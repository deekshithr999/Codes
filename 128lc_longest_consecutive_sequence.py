class Solution:
    '''
    Sets are Hashed in Python. 
    Any Insertion/deletion/Updation take O(1) time.
    TC: O(n)
    SC: O(n)
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        st= set(nums)
        mx_len = 0

        for i in range(len(nums)):
            if nums[i]-1 in st:
                continue
            length = 0
            while nums[i]+length in st:
                length +=1
            mx_len = max(mx_len, length)
        return mx_len
        

class Solution:
    '''
    TC: O(nlogn + n)
    SC: O(n)
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mx_long = 0
        tmp_long = 0

        for i in range(len(nums)):
            if i == 0:
                mx_long =1
                tmp_long += 1
                continue
            if nums[i]== nums[i-1]+1:
                tmp_long += 1
            elif nums[i]== nums[i-1]:
                pass
            else:
                mx_long = max(mx_long, tmp_long)
                tmp_long = 1
        mx_long = max(mx_long, tmp_long)
        return mx_long

        