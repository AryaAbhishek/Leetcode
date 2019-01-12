class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num & num-1 == 0:
            # right shift the given value
            while num>0:
                if num == 1:
                    return True
                num >>= 2
            # or left shift 1 util equal to given value
            # temp = 1
            # while temp<=num:
                # if temp == num:
                #     return True
                # temp <<= 2
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(4))
