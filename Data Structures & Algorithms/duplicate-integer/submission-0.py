class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # default false, flag true if duplicate found
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False