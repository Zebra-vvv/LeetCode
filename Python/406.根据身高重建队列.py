from typing import List


# 一句话总结：贪心，先按升高降序排列，再按照k的要求，往前插入（这样并不会破坏原有的顺序，因为越后面的身高越小）
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        result = []

        # 记住这个语法：按多个条件排序，先按 第0个元素 降序，再按 第1个元素 升序
        people.sort(key=lambda x: (-x[0], x[1]))
        
        for i in range(len(people)):
            # 取出k，作为插入的position
            position = people[i][1]
            result.insert(position, people[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    res = solution.reconstructQueue(people)
    print(res)
