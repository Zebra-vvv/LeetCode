from typing import List


# 一句话总结：回溯解决组合问题的经典案例 通过路径记录和逐层递增选择数值，枚举出所有从 1 到 n 中选出 k 个数的组合结果。
# “深搜”的取数范围控制是通过startIndex来实现的，通过递归函数传入startIndex = i+1，实现下一层选数范围控制
# “广搜”的取数范围控制通过 for 循环的 i 自增来实现，同层的情况下，因为i增长了，i+1传到下一层自然就增长了，下一层选数的范围自然也就被控制住了
#  深搜靠 +1，广搜靠 i 自增
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path = []
        self.result = []
        self.backtracking(n, k, startIndex=1)
        return self.result

    def backtracking(self, n: int, k: int, startIndex: int):

        # 终止条件
        if len(self.path) == k:

            # 这里一定要注意要拷贝一份，不然后续回溯会影响result里已添加的结果
            self.result.append(self.path[:])
            return

        # 单层递归逻辑
        # 剪枝操作, 不理解就举例：比如n=4，k=3,4-3+2=3，range右边是开区间，表示至多从2开始取
        for i in range(startIndex, n - (k - len(self.path)) + 2):
            self.path.append(i)

            # 通过 backtracking 函数的递归调用来控制 for 循环的层数，每一层递归对应选择一个数，直到选满 k 个数为止。
            self.backtracking(n, k, i+1)
            self.path.pop()


if __name__ == "__main__":
    n = 4
    k = 2
    solution = Solution()
    res = solution.combine(n, k)
    print(res)
