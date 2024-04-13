class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        fast = fast
        while True:
            if slow == fast:
                return slow
            slow = nums[slow]
            fast = nums[fast]