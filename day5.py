from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_item = None  # not item found yet
        duplicated = (
            1  # the times an item is duplicated need to be more than this value
        )
        check_list = []  # temp list to add the items already counted
        for i in nums:
            if i not in check_list:  # if  havent count the item
                print(f"item found: {i}")
                repetitions = nums.count(
                    i
                )  # the result of the item exist in the temp list
                print(f"result repetitions count: {repetitions}")
                if repetitions > duplicated:  # if the item  exist more than 1
                    duplicated = repetitions  # modify the times it exist   ins sted of 1 as before  we add the times exist
                    print(f"duplicated item: {duplicated}")
                    max_item = i  # here i add  it to the max times  it exist
                check_list.append(i)  # we found it and now we add it to the list temp
        return max_item  # returning the item we found that has more repetitions


nums = [3, 2, 3]

solution = Solution()
print(f"result : {solution.majorityElement(nums=nums)}")
