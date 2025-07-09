from typing import List


# 一句话总结：贪心，两次遍历，分别考虑右大于左和左大于右，返回两者的较大值
class Solution:
    def candy(self, ratings: List[int]) -> int:

        candy = [1] * len(ratings)

        # 从左往右遍历：如果右边孩子评分高，糖果数要比左边多
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # 从右往左遍历：如果左边孩子评分高，糖果数也要比右边多
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)


if __name__ == "__main__":
    solution = Solution()
    ratings = [1, 0, 2]
    res = solution.candy(ratings)
    print(res)
