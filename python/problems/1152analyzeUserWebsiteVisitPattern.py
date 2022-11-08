from collections import defaultdict

# TODO implement a solution with LinkedLists that sorts on insertion right away
def mostVisitedPattern(usernames: list[str], timestamps: list[int], websites: list[str]) -> list[str]:
    # total # of items tacked
    n = len(websites)
    # eliminates the need for handling the non-existing key in HashMap
    browsing_histories = defaultdict(list)
    # Create browsing histories for every user
    for i in range(n):
        browsing_histories[usernames[i]].append((websites[i], timestamps[i]))
    # Debugging
    # print(f"Browsing histories: {browsing_histories}")
    pattern_scores = defaultdict(int)
    # Analyze every user's browsing history 
    # and accumulate total counters for all possible patterns
    for user in browsing_histories:
        # get user's history
        history = browsing_histories[user]
        # Sort the browsing history by the timestamps to account for order
        # # Debugging
        # print(f"Browsing history of user {user} (NOT sorted): {history}")
        history.sort(key=lambda x: x[1])
        # Only keep the websites and not the timestamps since the list is sorted now
        # And info from timestamps are included in the order, thus we don't need timestamps anymore
        history = list(map(lambda x: x[0], history))
        # # Debugging
        # print(f"Browsing history of user {user} (sorted): {history}")
        history_len = len(history)
        # captured patterns for the specific user
        captured = set()
        # Count all patterns for a user
        for i in range(0, history_len - 2):
            for j in range(i + 1, history_len - 1):
                for k in range(j + 1, history_len):
                    pattern = (history[i], history[j], history[k])
                    if not pattern in captured:
                        pattern_scores[pattern] += 1
                        captured.add(pattern)

    # Debugging
    # print(f"Pattern scores: {pattern_scores}")
    # find the pattern with the largest score
    lexico_smallest_pattern = '' # TODO how to initialize?
    max_score = 0
    # Go over each pattern and find the most commong one
    for pattern in pattern_scores:
        if pattern_scores[pattern] > max_score:
            max_score = pattern_scores[pattern]
            lexico_smallest_pattern = pattern
        # "<"" operator here compares all 3 elements of each list and returns the list that is 
        # smaller in terms of each string from left to right
        # e.g. ["aba", "bde", "fgh"] < ["abc", "bde", "fgh"]
        # and ["abc", "bde", "fgh"] < ["abc", "bde", "fgi"],
        # but ["abc", "bde", "fgh"] < ["abc", "bde", "fgh"]
        elif pattern_scores[pattern] == max_score and pattern < lexico_smallest_pattern:  
            lexico_smallest_pattern = pattern
    
    return lexico_smallest_pattern




# Testing
print(mostVisitedPattern(
    ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"], 
    [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930], 
    ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"])
    )