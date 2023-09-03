class Solution:
    """Sliding window using an integer array."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        int_array = [-1] * 128
        max_length = 0
        for right, char in enumerate(s):
            if int_array[ord(char)] >= left:
                left = int_array[ord(char)] + 1
            else:
                max_length = max(max_length, right - left + 1)
            int_array[ord(char)] = right

        return max_length


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
print(s.lengthOfLongestSubstring("bbbbb"))  # 1
print(s.lengthOfLongestSubstring("pwwkew"))  # 3, wke
print(s.lengthOfLongestSubstring("abc"))  # 3
print(s.lengthOfLongestSubstring("ab"))  # 2
print(s.lengthOfLongestSubstring("a"))  # 1
print(s.lengthOfLongestSubstring(" "))  # 1
print(s.lengthOfLongestSubstring("aab"))  # 2
