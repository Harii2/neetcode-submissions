from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)

        words = wordList + [beginWord]

        for word in words:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                patterns[pat].append(word)

        queue = deque([beginWord])
        min_length = 1
        visited = {beginWord}

        while queue:

            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()

                if node == endWord:
                    return min_length

                for i in range(len(node)):
                    pattern = node[:i] + "*" + node[i+1:]

                    for neigh in patterns[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)

            min_length += 1

        return 0