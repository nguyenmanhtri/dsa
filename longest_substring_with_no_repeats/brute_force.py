class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict()
        n = len(s)
        result = 0
        for start in range(n):
            char_map.clear()
            for end in range(start, n):
                char_map[s[end]] = 1 + char_map.get(s[end], 0)
                if char_map[s[end]] > 1:
                    result = max(result, end - start)
                    break
                else:
                    result = max(result, end - start + 1)

        return result


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
print(s.lengthOfLongestSubstring("bbbbb"))  # 1
print(s.lengthOfLongestSubstring("pwwkew"))  # 3
print(s.lengthOfLongestSubstring("abc"))  # 3
print(s.lengthOfLongestSubstring("ab"))  # 2
print(s.lengthOfLongestSubstring("a"))  # 1
print(s.lengthOfLongestSubstring(" "))  # 1
