class Solution:
    def isPalindrome(self, s: str) -> bool:
      clean_str = ''.join(c for c in s if c.isalnum()).lower() 
      print(f"{clean_str=}")
      s_stack = []
      ptr = 0
      end_ptr = len(clean_str)-1
      while ptr <= end_ptr:
        print(f"{ptr=}")
        print(f"{end_ptr=}")
        if clean_str[ptr] != clean_str[end_ptr]:
          return False
        ptr += 1 
        end_ptr -= 1
      return True

