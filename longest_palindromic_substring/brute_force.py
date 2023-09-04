class Solution:
    def is_palindrome(self, s: str) -> bool:
        reversed_str = ""
        for i in reversed(s):
            reversed_str += i
        return s == reversed_str

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        palindrome_str = ""
        for start in range(len(s)):
            for end in range(len(s)):
                comb_str = s[start : end + 1]
                if self.is_palindrome(comb_str) and len(comb_str) > max_length:
                    max_length = len(comb_str)
                    palindrome_str = comb_str
        return palindrome_str


s = Solution()
# print(s.longestPalindrome("babad"))
# print(s.longestPalindrome("cbbd"))
# print(s.longestPalindrome("110101"))
# print(s.longestPalindrome("aaaa"))
# print(s.longestPalindrome(" "))
print(
    s.longestPalindrome(
        "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
    )
)
