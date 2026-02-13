#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
            curr = val[s[i]]
            nxt = val[s[i + 1]] if i + 1 < n else 0

            if curr < nxt:
                total -= curr
            else:
                total += curr

        return total
        
# @lc code=end

