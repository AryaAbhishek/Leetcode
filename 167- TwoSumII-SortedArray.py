# we will take 2 pointers one at start and other from end and keep on moving left for end pointer and
# right for start pointer until the sum is not equal to target.
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]>target:
                j -= 1
            elif numbers[i] + numbers[j]<target:
                i += 1
            else:
                break
        return [i+1,j+1]


if __name__ == "__main__":
    s = Solution()
    list1 = [1,2,3]
    print(s.twoSum(list1, 4))
