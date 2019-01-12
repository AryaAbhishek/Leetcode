# by doing Xor all the same number will result to zero leaving only the number which appeared once.

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        for i in nums:
            val ^= i
        return val


if __name__ == "__main__":
    s = Solution()
    list1 = [2,2,1]
    print(s.singleNumber(list1))
