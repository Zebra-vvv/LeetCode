from typing import List


# 🧠 【解题思路（双指针）】
# 每根柱子能接的雨水量由其两边的最大高度决定。
# 维护两个指针 left 和 right，分别从两侧向中间推进。
# 每次选择较小的那一侧来移动指针，并更新当前的最大高度和水量。
# 只需一趟扫描，时间效率高。
class Solution:
    def trap(self, height: List[int]):
        """
        LeetCode 42. 接雨水 - 双指针解法
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # 更新左边最大高度
                else:
                    res += left_max - height[left]  # 左边可接的水
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # 更新右边最大高度
                else:
                    res += right_max - height[right]  # 右边可接的水
                right -= 1

        return res


if __name__ == "__main__":
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = solution.trap(height)
    print(res)
