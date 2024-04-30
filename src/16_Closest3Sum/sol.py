class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = sys.maxsize
        result = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) -1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                print(sum3)
                if sum3 < target:
                    l += 1
                elif sum3 > target:
                    r -= 1
                else:
                    return sum3
                
                if abs(sum3 - target) < abs(closest - target):
                    closest = sum3
        return closest
