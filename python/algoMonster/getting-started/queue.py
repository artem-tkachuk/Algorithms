from collections import deque

def rotate_left_till_zero(nums):
    queue = deque(nums)

    while queue[0] != 0:
        # queue.rotate(-1)
        queue.append(queue.popleft())

    return queue



    # # initialize a new deque out of nums
    # queue = deque(nums)
    # # continue the loop till front of queue is 0
    # while queue[0] != 0:
    #     # remove the front of the queue and add it to the end
    #     queue.append(queue.popleft())
    # return queue

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = rotate_left_till_zero(nums)
    print(' '.join(map(str, res)))
