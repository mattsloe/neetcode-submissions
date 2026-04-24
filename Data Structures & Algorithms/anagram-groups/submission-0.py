class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # create dictionary
        for word in strs:
            key = ''.join(sorted(word))
            if key not in groups: # create a blank array as the pair
                groups[key] = []
            groups[key].append(word)

        # now you have a dict[str,list[str]]
        # use Python to cast your dict to list
        return list(groups.values()) 