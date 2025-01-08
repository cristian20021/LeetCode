class Solution(object):

    def countPrefixSuffixPairs(self,words):
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word_i = words[i]
                word_j = words[j]
                len_i = len(word_i)
                if len_i <= len(word_j):
                    if word_i == word_j[:len_i] and word_i == word_j[-len_i:]:
                        count += 1
        return count