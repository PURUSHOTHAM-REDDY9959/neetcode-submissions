class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in strs:
            key = tuple(sorted(i))   # sorted characters as key

            if key not in groups:
                groups[key] = []

            groups[key].append(i)

        return list(groups.values())
