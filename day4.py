from typing import List


class Solution:
    def majorityElement(self, nums: List[int]):
        for num in nums:
            if num < 2 or num != nums[num - 2]:
                print(nums[num])
                nums[num] = num
                num += 1
                print(f"result of i: {num}")
        return nums


nums = [1, 1, 1, 2, 2, 3]

solution = Solution()
print(f"result : {solution.majorityElement(nums=nums)}")
