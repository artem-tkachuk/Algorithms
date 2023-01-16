from typing import List
from collections import deque

def num_steps(target_combo: str, trapped_combos_set: List[str]) -> int:
    # Turn it into a hash set instead of a list for O(1) lookup
    trapped_combos_set = set(trapped_combos_set)

    def get_next_digit(digit):
        return str((int(digit) + 1) % 10)
        # return '0' if digit == '9' else str(int(digit) + 1)


    def get_previous_digit(digit):
        return str((int(digit) - 1) % 10)
        # return '9' if digit == '0' else str(int(digit) - 1)

    # Get valid combonations helper
    def get_next_safe_combos(curr_combo):
        # length of combination
        n = len(curr_combo)
        # list of next combos we will return (potentially empty)
        next_safe_combos = []
        # change every possible digit
        for i in range(n):
            # for i'th digit we change
            # generate a combo which we obtain from adding 1 to i'th digit
            next_combo = curr_combo[:i] + get_next_digit(curr_combo[i]) + curr_combo[(i + 1):]
            # add only if next_combo is not one of the trapped
            if next_combo not in trapped_combos_set:
                next_safe_combos.append(next_combo)
            # for i'th digit we change
            # generate a combo which we obtain from subtracting 1 from i'th digit
            prev_combo = curr_combo[:i] + get_previous_digit(curr_combo[i]) + curr_combo[(i + 1):]
            # add only if next_combo is not one of the trapped
            if prev_combo not in trapped_combos_set:
                next_safe_combos.append(prev_combo)

        return next_safe_combos

    # BFS Helper
    def bfs(starting_position):
        queue = deque([starting_position])
        # # of steps it takes to open the lock
        # we want to prevent cycles so that we don't visit nodes already visited
        visited = set([starting_position])
        # How far are the combos we currently explore from the starting combo
        level = 0
        # Continue exploring the combonations until we are either stuck
        # or find the path to target combo
        while len(queue) > 0:
            # how many nodes combos are at the next level we are about to explore
            # invariant -- always # of safe combos at the next level we explore
            n = len(queue)
            # Explore all the nodes at the current level
            for _ in range(n):
                # get the next combo we explore
                curr_combo = queue.popleft()
                # if we found what we needed
                if curr_combo == target_combo:
                    return level
                else:
                    # continue the same for the other combos if we didn't find target yet
                    for safe_combo in get_next_safe_combos(curr_combo):
                        # explore only unvisited combos
                        if safe_combo not in visited:
                            # add to queue
                            queue.append(safe_combo)
                            # mark visited
                            visited.add(safe_combo)
            # We now move to the next level
            level += 1
        # We did not return early ==> didn't reach target combo due to constraints
        return -1

    start_combo = "0000"
    
    return bfs(start_combo)

if __name__ == '__main__':
    target_combo = "0202"
    trapped_combos = ["0201","0101","0102","1212","2002"]
    res = num_steps(target_combo, trapped_combos)
    print(res)

