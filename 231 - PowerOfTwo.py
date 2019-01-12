class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return n&n-1 == 0


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(4))