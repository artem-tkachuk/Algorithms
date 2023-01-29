from typing import List

# given coins of different value and an ammount,
# return the fewest # of coins needed to make amount
# -1 of not possible
# Can reuse any coin any # of times


# Approach 1
def coinChangeTabulationLookFront(coins: List[int], amount: int) -> int:
    # Assertions
    assert all([coin > 0 for coin in coins]), "Coins can't be of negative value"
    assert amount >= 0, "Can't make up negative amount from positive coins"
    
    # our table of size (amount + 1) so that the final answer is at index == amount
    table_len = amount + 1
    # \infty is convenient because min(x, \inty) = x for any x \in \R
    # this indicates that the amount at any index can't be made up
    dp = [float('inf')] * table_len
    # Base case: 0 coins required to make up amount of 0
    dp[0] = 0
    
    # iterate through the dp table and look front
    for i, curr_min in enumerate(dp):
        # use every coin if possible
        for coin in coins:
            # where do we go if we use this coin
            next_index = i + coin
            # are we still within the bounds of our dp table?
            if next_index <= amount:
                next_curr_min = dp[next_index]
                # (possibly) update whichever index we get to by using this coin
                # if the current combination is smaller in quantity than existing
                dp[next_index] = min(curr_min + 1, next_curr_min)
    
    # our final answer is stored at idex == amount
    # we need to return -1 instead of \infty according to our prompt
    return dp[amount] if dp[amount] != float('inf') else -1

def coinChangeTabulationLookBackwards(coins: List[int], amount: int) -> int:
    # Assertions
    assert all([coin > 0 for coin in coins]), "Coins can't be of negative value"
    assert amount >= 0, "Can't make up negative amount from positive coins"
    
    # our table of size (amount + 1) so that the final answer is at index == amount
    table_len = amount + 1
    # \infty is convenient because min(x, \inty) = x for any x \in \R
    # this indicates that the amount at any index can't be made up
    dp = [float('inf')] * table_len
    # Base case: 0 coins required to make up amount of 0
    dp[0] = 0
    
    # iterate through the dp table and look back
    for i in range(1, table_len):
        
        # use every coin if possible
        for coin in coins:
            # where do we go if we use this coin
            prev_index = i - coin
            # are we still within the bounds of our dp table?
            if prev_index >= 0:
                # what is the current value for that index in dp? Initially \infty
                curr_min = dp[i]
                # what is the smallest # of coins that is needed to obtain amount at previous index    
                prev_curr_min = dp[prev_index]
                # (possibly) update the current index by using the current coin
                # if the previous combination + current coin is smaller in quantity than existing at that index
                dp[i] = min(curr_min, prev_curr_min + 1)
    
    # our final answer is stored at idex == amount
    # we need to return -1 instead of \infty according to our prompt
    return dp[amount] if dp[amount] != float('inf') else -1



# Approach 2
def coinChangeMemoization(coins: List[int], amount: int) -> int:
    # our table of size (amount + 1) so that the final answer is at index == amount
    table_len = amount + 1
    # Create the memo array upfront instead of dynamic hash table
    memo = [-1] * table_len
    # run helper function that features memoization and has running sum
    helper_result = coinChangeMemoizationHelperArray(coins, amount, sum=0, memo=memo)
    # we need to return -1 instead of \infty according to our prompt
    return  helper_result if helper_result != float('inf') else -1
    
def coinChangeMemoizationHelperHashMap(coins: List[int], amount: int, sum: int, memo={}) -> int:
    # have we already encountered this problem before?
    if sum in memo:
        return memo[sum]
    # if we exceeded the current amount, return \infty because it will be used in a min one level
    # higher in the recusrsion, and anything else \in R will win over it
    if sum > amount:
        return float('inf')
    # if we arrived exactly at amount, we are done, and we will start going upwards in the tree
    if sum == amount:
        return 0
    # start with \infty so that anything else wins over it in the min comparison
    min_num_coins = float('inf')
    # apply each available coin
    for coin in coins:
        # (potentially) update the minimum if applying any of the coins leads to the smaller answer
        min_num_coins = min(
            coinChangeMemoizationHelperHashMap(coins, amount, sum + coin, memo), 
            min_num_coins
        )

    # the answer we got from the minimum child + the coin that got us to the current node
    answer = min_num_coins + 1
    # memoize the answer to the subproblem for the current sum value
    memo[sum] = answer
    # return the answer to the caller
    return answer

def coinChangeMemoizationHelperArray(coins: List[int], amount: int, sum: int, memo) -> int:
    # if we exceeded the current amount, return \infty because it will be used in a min one level
    # higher in the recusrsion, and anything else \in R will win over it
    if sum > amount:
        return float('inf')
    # if we arrived exactly at amount, we are done, and we will start going upwards in the tree
    if sum == amount:
        return 0
    # have we already encountered this problem before?
    if memo[sum] != -1:
        return memo[sum]
    # start with \infty so that anything else wins over it in the min comparison
    min_num_coins = float('inf')
    # apply each available coin
    for coin in coins:
        # (potentially) update the minimum if applying any of the coins leads to the smaller answer
        min_num_coins = min(
            coinChangeMemoizationHelperArray(coins, amount, sum + coin, memo), 
            min_num_coins
        )

    # the answer we got from the minimum child + the coin that got us to the current node
    answer = min_num_coins + 1
    # memoize the answer to the subproblem for the current sum value
    memo[sum] = answer
    # return the answer to the caller
    return answer
    

print(coinChangeTabulationLookBackwards([186, 419, 83, 408], 6249))



