class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_value = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                max_value = max(max_value,count)
            else:
                count = 0
        return max_value
