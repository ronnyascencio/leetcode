from typing import List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                print(nums[i])
                nums[i] = num
                i += 1
                print(f"result of i: {i}")
        return


nums = [1, 1, 1, 2, 2, 3]

solution = Solution()
print(f"result : {solution.removeDuplicates(nums=nums)}")
