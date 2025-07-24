from typing import List

class Solution:
    def maxArea(self, height:List[int]):
        # 初始化左右指针
        left, right = 0, len(height) - 1
        max_area = 0  # 最大面积初始化为0

        # 开始双指针向中间靠拢
        while left < right:
            # 计算当前面积：高度取决于较短的一侧，宽度是两指针之间距离
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            # 更新最大面积
            max_area = max(max_area, area)

            # 谁矮谁移动（因为想找到更高的木板来增加可能的面积）
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = solution.maxArea(height)
    print(res)