class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table_s = {}
        table_t = {}
        for i in s:
            if i in table_s:
                table_s[i] += 1
            else:
                table_s[i] = 1

        for i in t:
            if i in table_t:
                table_t[i] += 1
            else: 
                table_t[i] = 1
        for key in table_s.keys():
            if table_s.get(key) != table_t.get(key):
                return False
        return True
    
    
solution = Solution()

solution.isAnagram(s='anagram', t='nagaram')

