class Solution:
    def __init__(self):
        self.memo = {}

    def dfs(self, index, s, char_mask, can_change, k):
        if index == len(s):
            return 0

        key = (index << 27) | (char_mask << 1) | (1 if can_change else 0)
        if key in self.memo:
            return self.memo[key]

        current_bit = 1 << (ord(s[index]) - ord('a'))
        updated_mask = char_mask | current_bit

        if bin(updated_mask).count('1') > k:
            max_partitions = 1 + self.dfs(index + 1, s, current_bit, can_change, k)
        else:
            max_partitions = self.dfs(index + 1, s, updated_mask, can_change, k)

        if can_change:
            for c in range(26):
                new_bit = 1 << c
                new_mask = char_mask | new_bit
                if bin(new_mask).count('1') > k:
                    partitions = 1 + self.dfs(index + 1, s, new_bit, False, k)
                else:
                    partitions = self.dfs(index + 1, s, new_mask, False, k)
                if partitions > max_partitions:
                    max_partitions = partitions

        self.memo[key] = max_partitions
        return max_partitions

    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        return 1 + self.dfs(0, s, 0, True, k)