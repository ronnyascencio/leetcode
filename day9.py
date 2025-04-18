from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = nums[0]
        for i in range(1, n):
            if i > max_reach:
                print(f"max reach: {max_reach}")
                return False
            max_reach = max(max_reach, i + nums[i])
            print(f"max reach: {max_reach}")
            if max_reach >= n - 1:
                print(f"max reach: {max_reach}")
                return True
        return max_reach >= n - 1


nums = [3, 2, 1, 0, 4]
solution = Solution()
print(f"solution result: {solution.canJump(nums=nums)}")
