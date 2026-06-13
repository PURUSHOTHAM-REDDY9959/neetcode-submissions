class Solution:
    def groupAnagrams(self, strs):
        a = {}

        for i in strs:
            b = "".join(sorted(i))

            if b not in a:
                a[b] = []

            a[b].append(i)

        return list(a.values())