class Solution:

    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i
            # find the separator '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])     # get length
            word = s[j+1 : j+1+length]  # get the word
            result.append(word)

            i = j + 1 + length       # move to next encoded part

        return result
