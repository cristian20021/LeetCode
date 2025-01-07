class Solution(object):
    def stringMatching(self, words):
        new_l = []
        sorted_words = sorted(words, key=len)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if sorted_words[i] in sorted_words[j]:
                    new_l.append(sorted_words[i])

        return list(dict.fromkeys(new_l))
        