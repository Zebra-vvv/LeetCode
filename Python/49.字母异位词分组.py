from collections import defaultdict
from typing import List

# 一句话总结：将每个字符串按字母排序后作为哈希表的键，将具有相同排序结果的字符串分组即可。
class Solution:
    def groupAnagrams(self, strs) -> List[List[str]]:

        # defaultdict(list) 能自动给新 key 创建默认的空列表，让我们不用手动判断 key 是否存在，写起来更简洁优雅，特别适合按 key 分组或统计的场景。
        result = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))  # 排序后的字符串作为 key，所以异位词自然而然的就会被加到同一个键中
            result[key].append(s)
        return list(result.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    res = solution.groupAnagrams(strs)
    print(res)
