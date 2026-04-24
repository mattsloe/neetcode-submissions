class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       i_index = None 
       j_index = None
       for i, val in enumerate(nums):
        for j,j_val in enumerate(nums):
            if val + j_val == target and i != j:
                return [i,j]