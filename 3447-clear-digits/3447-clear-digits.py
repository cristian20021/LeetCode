class Solution:
    def clearDigits(self, s):
        l = []
        for i in s:
            if i.isdigit():
                l.pop()
            else:
                l.append(i)
        return ''.join(l)