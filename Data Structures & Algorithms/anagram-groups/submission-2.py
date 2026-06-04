class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}

        for i in strs:
            key = tuple(sorted(i))   # sorted characters as key

            if key not in a:
                a[key] = []

            a[key].append(i)

        return list(a.values())
