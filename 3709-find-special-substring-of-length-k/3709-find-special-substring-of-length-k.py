class Solution(object):
 
    def hasSpecialSubstring(self, s, k):
     
        i, j = 0, 0
        n = len(s) - 1

        while j < len(s):
            if s[j] == s[i]:
                if j - i + 1 == k:
                    if i == 0:
                        if j == n:
                            return True
                        elif j < n and s[j] != s[j + 1]:
                            return True
                    elif i > 0 and s[i - 1] != s[i]:
                        if j == n:
                            return True
                        elif j < n and s[j] != s[j + 1]:
                            return True
                    j += 1
                    i = j
                else:
                    j += 1
            else:
                i = j
                j = i + 1

        return False