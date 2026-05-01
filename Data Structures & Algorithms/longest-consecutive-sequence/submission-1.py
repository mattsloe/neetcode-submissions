class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        longest = 0
        best_start = nums[0] 
        for num in nums_set:
          if num-1 not in nums_set:
            seq_length = 1
            while (num + seq_length) in nums_set:
              seq_length += 1
            if seq_length > longest:
              longest = seq_length
              best_start = num
        
        return longest
