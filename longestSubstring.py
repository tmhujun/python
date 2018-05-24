#! python3
# longestSubstring.py - find out longest substring without repeat char

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        for i in range(len(s)):
            uniLst = []
            l = 0
            for j in range(i, len(s)):
                if s[j] in uniLst:
                    break
                else:
                    l += 1
                    uniLst.append(s[j])
            if l > maxlen:
                maxlen = l
        return maxlen

def main():
    result = Solution().lengthOfLongestSubstring('aaaaa')
    print(result)

if __name__ == '__main__':
    main()
