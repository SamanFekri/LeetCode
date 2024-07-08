class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            k += 1
            nums[k] = nums[i] # swap new number to the correct position

        return k + 1
