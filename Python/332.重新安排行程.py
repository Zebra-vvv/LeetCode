from typing import List
from collections import defaultdict

# 一句话总结：使用回溯+字典邻接表构建图，通过逆序排序+DFS实现按字典序最小的欧拉路径搜索，并在递归回溯时将路径逆序加入结果中。
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # 表示创建了一个 “默认值是空列表”的字典”，例如：
        # {
        # "JFK": ["SFO", "ATL"],
        # "SFO": ["ATL"],
        # "ATL": ["JFK", "SFO"]
        # }
        targets = defaultdict(list)
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])

        # 按字典序排序到达机场，逆序是为了方便用 pop() 取最小
        for key in targets:
            targets[key].sort(reverse=True)

        self.result = []
        self.backtracking("JFK", targets)
        return self.result[::-1]  # 返回逆序的行程路径

    def backtracking(self, airport, targets):
        while targets[airport]:  # 当机场还有可到达的机场时
            next_airport = targets[airport].pop()  # 弹出下一个机场
            self.backtracking(next_airport, targets)  # 递归调用回溯函数进行深度优先搜索
        self.result.append(airport)


if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    solution = Solution()
    res = solution.findItinerary(tickets)
    print(res)
