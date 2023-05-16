from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        queue = [k]
        num_nodes_at_curr_level = 1
        max_len = -1

        graph = defaultdict(list)

        for time in times:
            source, target, weight = time
            graph[source].append(target)

        while len(queue) > 0:
            max_len += 1
        
            num_nodes_at_next_level = 0

            for _ in range(num_nodes_at_curr_level):
                curr_node = queue.pop(0)
                visited.add(curr_node)

                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        num_nodes_at_next_level += 1

            num_nodes_at_curr_level = num_nodes_at_next_level


        return max_len if len(visited) == n else -1

times = [[1,2,1]]
n = 2
k = 1
print(Solution().networkDelayTime(times, n, k))
