from typing import List

def phoneNumberPath(phone_number: str) -> List[str]:
    # Assume there can be phone numbers of arbitrary length, but usually it is 10
    n = len(phone_number)
    # Error handling
    assert n > 0, "empty phone number!"
    # keypad model
    keypad_no_zero = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
    # final result we need to return - steps to dial the number on the keypad
    steps = []
    # loop through every digit but last
    # and consider (n - 1) pairs (from, to)
    for i in range(n - 1):
        steps.append(f"Press {phone_number[i]}")
        # parse out actual digits we want to get from and to
        from_digit, to_digit = phone_number[i], phone_number[i + 1]
        # do we even need to do any action at all? If not, go to next digits
        if to_digit == from_digit:
            continue
        else:
            # prepend tail_action to the combination later in case to or from is 0
            start_action, end_action = None, None   
            # check whether we start from 0
            if to_digit == '0':
                # going to 0 is the same as going to 8 and then going "down" one more step
                end_action = "down"
                to_digit = '8'
            # check whether we want to go to 0
            elif from_digit == '0':
                # going from 0 is the same as going from 8 and going "up" one more step before that
                start_action = "up"
                from_digit = '8'
            # find coordinates of the digit we are starting from on the keypad
            (from_i, from_j) = find(keypad_no_zero, from_digit)
            # find coordinates of the digit we are goin to on the keypad
            (to_i, to_j) = find(keypad_no_zero, to_digit)
            # find difference
            (row_diff, col_diff) = (to_i - from_i, to_j - from_j)
            # get corresponding actions for the obtained differences
            row_action, col_action = get_row_action(row_diff), get_col_action(col_diff)
            # handle additional start action
            if start_action is not None:
                steps.append(start_action)
            # append the corresponding # of actions to get from_digit -> to_digit path
            # add row actions
            steps += [row_action] * abs(row_diff)
            # add col actions
            steps += [col_action] * abs(col_diff)
            # handle additional end action
            if end_action is not None:
                steps.append(end_action)

    # Press the last digit after we arrive at it
    steps.append(f"Press {phone_number[-1]}")
    # return the final action combination to dial the phone_number
    return steps

# lambda functions to return the proper actions
def get_row_action(row_diff):
    if row_diff > 0:
        return "down" 
    elif row_diff < 0:
        return "up"
    else:
        return ""

def get_col_action(col_diff):
    if col_diff > 0:
        return "right" 
    elif col_diff < 0:
        return "left"
    else:
        return ""

# find coordinates of the digit on the keypad, does not work on 0 because we handle it in a separate place
def find(keypad, digit):
    # error handling
    assert \
        digit in ["1", "2", "3", "4", "5", "6", "7", "8", "9"], \
        "Can't find this symbol! It is not a digit!"
    # dimensions of the keypad
    m, n = len(keypad), len(keypad[0])
    # should always be 3x3
    assert \
        m == 3 and n == 3, \
            "Wrong keypad!"
    # go over each row 
    for i in range(m):
        # go over each column
        for j in range(n):
            # if found
            if keypad[i][j] == digit:
                # return index on the keypad
                return (i, j)
    
# DEBUGGING Testing of find
# for i in range(1, 10):
#     print(f'Index of {i} is {find(keypad_no_zero, str(i))}')

# Testing
phone_number = "65008420527"
for action in phoneNumberPath(phone_number):
    print(action)