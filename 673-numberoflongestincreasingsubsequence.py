# Time limit exceeded error
class Solution(object):
    def __init__(self):
        self.arr = []
        self.high = 0

    def findtotal(self, nums, arr1):
        # print(nums, arr1)
        if len(nums) == 0:
            self.arr.append(arr1)
            if len(arr1)>self.high:
                self.high = len(arr1)
        elif len(nums) == 1:
            if nums[0] >= arr1[-1]:
                arr1.append(nums[0])
            self.arr.append(arr1)
            if len(arr1)>self.high:
                self.high = len(arr1)
        else:
            for i in range(len(nums)):
                if len(arr1) == 0:
                    self.findtotal(nums[i + 1:], [nums[i]])
                elif nums[i] >= arr1[-1]:
                    arr2 = arr1[:]
                    arr2.append(nums[i])
                    self.findtotal(nums[i + 1:], arr2)
            self.arr.append(arr1)
            if len(arr1)>self.high:
                self.high = len(arr1)

    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is []:
            return 0
        if len(nums) == 1:
            return 1
        self.findtotal(nums, [])
        temp = 0
        # print(self.arr, self.high)
        for i in self.arr:
            if len(i)==self.high:
                temp +=1
        return temp
if __name__ == "__main__":
    s = Solution()
    list1 = [4,3,2,0,3,1,10,2,1,1,9,5,9,6,8,6,5,1,0,10,8,6,-9,0,8,9,5,0,2,2,4,0,9,10,2,0,0,7,10,9,6,0,8,9,10,7,8,8,3,9,5,3,4,6,1,5,4,7,9,2,5,10,4,-3,4,6,4,6,1,1,10,0,9,9,3,5,1,3,3,2,1,3,8,7,1,2,0,7,4]
    print(s.findNumberOfLIS(list1))