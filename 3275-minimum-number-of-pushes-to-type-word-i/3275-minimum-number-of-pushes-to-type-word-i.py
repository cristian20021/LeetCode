class Solution(object):
    def minimumPushes(self, word):
        return sum(i // 8 + 1 for i in range(len(word)))
        