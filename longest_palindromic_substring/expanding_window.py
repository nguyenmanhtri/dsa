class Solution:
    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        start = 0
        for i in range(len(s)):
            odd_len = self.expand_around_center(s, i, i)
            even_len = self.expand_around_center(s, i, i + 1)
            flen = max(odd_len, even_len)
            if flen > max_length:
                max_length = flen
                start = int(i - (flen - (1 if flen == odd_len else 2)) / 2)
        return s[start : start + max_length]


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("110101"))
print(s.longestPalindrome("aaaa"))
print(s.longestPalindrome(" "))
print(
    s.longestPalindrome(
        "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
    )
)
