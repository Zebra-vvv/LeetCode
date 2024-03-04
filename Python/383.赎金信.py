class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for i in ransomNote:
            record[ord(i)-ord('a')] += 1
        for j in magazine:
            record[ord(j)-ord('a')] -= 1
        for k in record:
            if k > 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)
    print(result)
