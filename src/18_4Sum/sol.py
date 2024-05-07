class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort() # Sort helps for deciding left and right
        result = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: # Stop it from adding duplicate answers
                continue
            
            for j in range (i + 1, n - 1):
                if j > i + 1 and nums[j] == nums[j - 1]: # Stop it from adding duplicate answers
                    continue

                # l is for left and r is for right
                l, r = j + 1, n - 1
                while l < r:
                    sum4 = nums[i] + nums[j] + nums[l] + nums[r]

                    if sum4 == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l - 1]: # Stop it from adding duplicate answers
                            l += 1
                        
                    elif sum4 < target:
                        l += 1
                    else:
                        r -= 1
        return result
