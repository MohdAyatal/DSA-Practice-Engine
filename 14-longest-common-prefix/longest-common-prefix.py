class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        for word in strs:
            if len(word) < min_length:
                min_length = len(word)

        for i in range (min_length):
            for j in range (len(strs)):
            
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_length]