import math
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        log = round(math.log(abs(n), 3))
        return 3 ** log == n


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(4))
