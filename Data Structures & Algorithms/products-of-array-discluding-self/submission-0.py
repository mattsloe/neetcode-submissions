class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      pre_product = []
      post_product = []

      for i, val in enumerate(nums):
        if i != 0:
          pre_product.append(pre_product[i-1] * nums[i-1])
        else: 
          pre_product.append(1)

      post_product = [1] * len(nums)

      for i in range(len(nums) - 2, -1, -1):
        post_product[i] = post_product[i + 1] * nums[i + 1]
        
      return [x * y for x, y in zip(pre_product, post_product)]