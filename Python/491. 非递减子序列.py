from typing import List


# 一句话总结：本题也要对树层进行去重，但是和力扣90题不同的是，本题要在原数组顺序的情况下，求序列，所以不能通过排序原数组的方式去重
# 所以换一种去重方式，通过set的方式去重
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(nums, startIndex=0)
        return self.result

    def backtracking(self, nums, startIndex):

        # 终止条件
        if len(self.path) >= 2:
            self.result.append(self.path[:])
            # 这里不能直接return，因为self.path大于2的节点还要继续收集，也就是要收集所有深度大于等于2的节点
        
        # 每次递归调用时新建一个set（每层都会重新定义一个新的set），只存放当前树层已经用过的数
        uset = set()

        # 单层递归逻辑
        for i in range(startIndex, len(nums)):
            
            # 如果当前遍历的数如果小于path中最后一个数，那就不要，因为要保持递增
            # 如果当前数在set里出现过，也不要，因为要去重
            if (self.path and nums[i] < self.path[-1]) or nums[i] in uset:
                continue

            uset.add(nums[i])  # 记录这个元素在本层用过了，本层后面不能再用了

            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    solution = Solution()
    res = solution.findSubsequences(nums)
    print(res)
