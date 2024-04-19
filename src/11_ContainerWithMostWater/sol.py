class Solution:
    def maxArea(self, height: List[int]) -> int:
        # min area to 0
        area = 0
        # left wall and right wall set
        left = 0
        right = len(height) - 1

        while left < right:
            # get height of walls
            lh = height[left]
            rh = height[right]

            h = min(lh, rh)
            w = right - left
            area = max(area, w * h)

            # moving the shorter wall towards the other wall
            if lh <= rh:
                left += 1
            else:
                right -= 1
        return area
        
