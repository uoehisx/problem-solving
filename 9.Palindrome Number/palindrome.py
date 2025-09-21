class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_str=str(x)
        reversed_str=int_str[::-1]

        if int_str==reversed_str:
            return bool(1)
        else:
            return bool(0)
        #Time complexity: O(n)
        #Space complexity: O(n)