class Solution(object):
    def flowerGame(self, n, m):
        odd1 = (n + 1) // 2
        even1 = n // 2

        odd2 = (m + 1) // 2
        even2 = m // 2

        return odd1 * even2 + odd2 * even1
