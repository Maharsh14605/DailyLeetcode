#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first = strs[0]
        prefix = []

        for i in range(len(first)):              
            ch = first[i]

            for s in strs[1:]:                   
                if i >= len(s) or s[i] != ch:   
                    return "".join(prefix)

            prefix.append(ch)                    

        return "".join(prefix)
            
        
            
                       
        
# @lc code=end

