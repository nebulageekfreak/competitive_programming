# link to this problem: https://leetcode.com/problems/find-words-containing-character/description/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, v in enumerate(words):
            if x in v:
                result.append(i)
        return result
