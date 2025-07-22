from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 将所有数字放入一个 set 中，方便 O(1) 查询
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            # 如果 num-1 不在集合中，说明 num 是一个序列的起点
            if num - 1 not in num_set:
                current = num
                length = 1

                # 一直查找连续的下一个数字
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # 更新最大长度
                max_len = max(max_len, length)

        return max_len


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    res = solution.longestConsecutive(nums)
    print(res)