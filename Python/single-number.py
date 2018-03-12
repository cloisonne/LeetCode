# Time:  O(n)
# Space: O(1)
#
# Given an array of integers, every element appears twice except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

import operator
from functools import reduce

# 使用异或，a^a = 0  0^b = b
class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """
    def _xor(self,a,b):
        return a^b

    def singleNumber(self, A):
        #return reduce(operator.xor, A)
        return reduce(self._xor, A)



if __name__ == '__main__':
    print (Solution().singleNumber([1, 1, 2, 2, 3]))
