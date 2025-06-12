from typing import List

# 冒泡排序（升序）
def bubble_sort(nums:List[int]):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 -i):
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                swapped = True
        if swapped == False:
            break
    return nums



# 快速排序（升序）
def quick_sort(nums):
    # 基本情况：数组为空或只有一个元素，直接返回
    if len(nums) <= 1:
        return nums

    # 选第一个元素作为基准（pivot）
    pivot = nums[0]

    # 划分为三部分
    left = []   # 小于 pivot 的元素
    mid = []    # 等于 pivot 的元素（包括自己，支持重复元素）
    right = []  # 大于 pivot 的元素

    # 遍历原数组，按大小分类
    for x in nums:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            mid.append(x)

    # 对左右部分递归排序，并拼接
    return quick_sort(left) + mid + quick_sort(right)

# 测试
nums = [5, 2, 4, 1, 6, 16, 19, 7]
result = bubble_sort(nums)
print(result)