class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: x[1])
        arr = []
        for i in range(len(people)):
            if len(arr) == 0:
                arr.append(people[i])
            else:
                temp = people[i][1]
                flag = True
                for a in range(len(arr)):
                    if arr[a][0]>=people[i][0]:
                        if temp>0:
                            temp -= 1
                        else:
                            flag = False
                            arr.insert(a, people[i])
                            break
                if flag:
                    arr.append(people[i])
        return arr


if __name__ == "__main__":
    s = Solution()
    arr = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(s.reconstructQueue(arr))