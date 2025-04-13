from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)  # how many items ar ein the list
        k = (
            k % n
        )  # we need to neutralize k to tel it that could not be grater than the list  lengh
        nums[:] = (
            nums[-k:] + nums[:-k]
        )  # rotating the list values  taking the last 3 to place in front  taking as a second imput the first elements but not the last3


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
print(f"solution: {solution.rotate(nums=nums, k=k)}")
