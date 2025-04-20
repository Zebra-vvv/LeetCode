class Solution:
    def canConstruct(self, ransom:str, magazine:str) -> bool:
        # 和 242.有效字母的异位词 思路几乎一样
        record = [0] * 26
        for i in magazine:
            record[ord(i)-ord('a')] += 1 
        for j in ransom:
            record[ord(j)-ord('a')] -= 1
        for val in record:
            if val < 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    print(result)
